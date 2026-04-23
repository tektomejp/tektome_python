# BIM Spatial Analysis Playbook -- Agent Reference

Use this playbook when an OpenFlow must answer spatial BIM questions:

- "Which rooms are bedrooms, and how many doors does each bedroom have?"
  → [Recipe: bedrooms and doors](#recipe-bedrooms-and-doors)
- "Where is this object located?"
  → [Recipe: where is this object located?](#recipe-where-is-this-object-located)
- "Which elements are inside this room or area?"
  → [Recipe: which objects are inside this room or area?](#recipe-which-objects-are-inside-this-room-or-area)
  (use prism for irregular footprints)
- "What is the distance between these two elements?"
  → [Recipe: distance between elements](#recipe-distance-between-elements)
- "Which nearby objects match this name/type?" / "within X metres"
  → [Recipe: nearby objects by radius (sphere search)](#recipe-nearby-objects-by-radius-sphere-search)

This is a workflow guide, not an endpoint index. For endpoint details, see
[BIM_DATA_AND_TOOLS.md](BIM_DATA_AND_TOOLS.md). For writing attributes,
citations, and approval tickets, see
[MANUAL_ATTRIBUTES_AND_CITATIONS.md](MANUAL_ATTRIBUTES_AND_CITATIONS.md). For
labels, route lines, and other visual overlays, see
[CUSTOM_BIM_VISUAL_AIDS.md](CUSTOM_BIM_VISUAL_AIDS.md).

---

## Default posture

You are usually blind to the BIM model's naming conventions. Do not assume a
model uses `Category == Rooms`, `ifcType == IfcSpace`, or English names. Start
by discovering keys and values, then write the final OpenFlow around what the
model actually contains.

The safe order is:

```text
resolve BIM project
-> discover keys/values with semantic KV query and/or KV stats
-> search candidate element IDs with KV/expression search
-> fetch light metadata/properties only
-> use topology search / bboxes for spatial tests
-> fetch full JSON only for fallback or final evidence
-> write table/value + BIM citations + approval ticket
```

Do not start by loading every full BIM object JSON body. BIM elements can be
large. Prefer ID searches, trimmed fetches, stored bounding boxes, and topology
tools.

---

## Invariants (read once, hold them the whole flow)

These assumptions are load-bearing for every recipe below. Verify them the
first time you touch a model; trust them afterwards.

- **IDs are Speckle hashes.** Every BIM search/fetch endpoint returns Speckle
  element hashes. Citations (`create_attribute_bim_citation`,
  `BIMElementRequest.bim_element_id`) require the same Speckle hashes. Do not
  pass Revit GUIDs, IFC GlobalIds, or numeric element IDs — the backend
  validates against Speckle hashes.
- **Coordinates are in the model's native unit system**, not a fixed unit.
  `Point3D`/`Point2D`/bbox values are whatever the Speckle model was authored
  in — typically millimetres for Japanese Revit/IFC exports, sometimes metres
  for other models. Sample one bbox magnitude before hard-coding a unit:
  a residential room with `BBoxMax.x - BBoxMin.x` around `3000` is
  millimetres; around `3.0` is metres. Record the inferred unit in the
  output `notes` column.
- **Bbox frame is world, not local.** `bboxes` on a trim-fetched element are
  already in the model's world coordinates. No transform composition is
  needed before topology search or distance math.
- **Bbox payload shape is `{BBoxMin:{x,y,z}, BBoxMax:{x,y,z}}`** — always
  three axes, even for flat elements. If only two axes appear, the element
  is degenerate; treat it as `no_bbox`.
- **Guarded `Context` fields raise on `None`.** `ctx.system_chatroom_id`,
  `ctx.system_execution_id`, `ctx.system_dataspace_id`,
  `ctx.system_project_id`, `ctx.system_resource_id` raise `AttributeError`
  when unset rather than returning `None`. Wrap access in `try/except
  AttributeError` if the flow can run in multiple modes.
- **Topology search is always async.** Box, prism, and sphere all return a
  `process_id`; you must poll `get_celery_task`. There is no sync variant.
- **Celery status set is fixed.** The `/api/core/tasks/{task_id}/` endpoint
  returns `{"status": str, "result": any}` where `status` is one of
  `PENDING | RECEIVED | STARTED | SUCCESS | FAILURE | REVOKED | REJECTED |
  RETRY | IGNORED`. Only `SUCCESS` carries a result. There is no `state`
  key, no `COMPLETED`, no `FAILED` — code that checks for those will
  timeout against a task that has already succeeded.

---

## Sibling references (must be loaded alongside this playbook)

This playbook references four siblings. If only this file is in the agent
context, the last-mile steps (citations, approval tickets, visual aids,
resource resolution) have no template. Confirm these are present:

- `BIM_DATA_AND_TOOLS.md` — endpoint index, KV stats details, full element
  JSON shape.
- `MANUAL_ATTRIBUTES_AND_CITATIONS.md` — attribute instance creation, BIM
  citation payload, approval-ticket submission. Required for every flow
  that writes results back.
- `CUSTOM_BIM_VISUAL_AIDS.md` — text labels, highlight colors, overlay
  geometry.
- `DATASPACES_PROJECTS_AND_RESOURCES.md` — the `Context` field matrix by
  `system_flow_type`, and how to list/resolve project resources.

---

## OpenFlow starting point

Most spatial OpenFlows start from an injected `Context`. In a
`resource_attr_extraction` flow, `ctx.system_resource_id` is usually the BIM
resource or a resource linked to a BIM project. In a `project_attr_extraction`
flow, you may need to list project resources and choose the BIM resource first.

```python
# requirements:
# git+https://github.com/tektomejp/tektome_python.git@<VERSION>

from pydantic import BaseModel, Field

from tektome import Context
from tektome.decorators import parseio


class Output(BaseModel):
    rows: list[dict]
    notes: list[str] = Field(default_factory=list)


@parseio
def main(ctx: Context) -> Output:
    # For production attribute extraction flows, context IDs are injected.
    # During development, you may need to pass resource/project IDs manually.
    resource_id = ctx.system_resource_id

    with ctx.client() as client:
        rows = run_spatial_analysis(client=client, resource_id=resource_id)
    return Output(rows=rows)
```

Resolve the BIM project from the resource before any BIM search:

```python
from tektome.endpoints.api.bim import list_bim_projects_by_resource


def resolve_bim_project_id(client, resource_id):
    resp = list_bim_projects_by_resource.sync_detailed(
        client=client,
        resource_id=resource_id,
        page=1,
        page_size=1,
    )
    if resp.status_code.value != 200 or not resp.parsed:
        raise RuntimeError(f"No BIM project found for resource {resource_id}")
    return resp.parsed[0].id
```

For exploratory development, write a small script that resolves the BIM project,
runs semantic KV probes, fetches 5-20 sample elements, and prints their key
paths. Then use those observations in the final OpenFlow.

### Project-flow variant: pick the BIM resource first

In a `project_attr_extraction` flow, `ctx.system_resource_id` is not set and
accessing it raises `AttributeError`. List the project's resources, keep only
the IFC ones, and resolve each to a `bim_project_id`:

```python
import json

from tektome.endpoints.api.bim import get_bim_project
from tektome.endpoints.api.dataspace import list_dataspace_project_resources


def list_bim_resources_in_project(client, project_id):
    resp = list_dataspace_project_resources.sync_detailed(
        client=client,
        project_id=project_id,
    )
    if resp.status_code.value != 200 or not resp.content:
        raise RuntimeError(
            f"list_dataspace_project_resources failed: {resp.status_code.value}"
        )
    items = json.loads(resp.content).get("items", [])
    # core_attributes.kind is lowercase in the API payload.
    return [r for r in items if (r.get("core_attributes") or {}).get("kind", "").lower() == "ifc"]


def resolve_bim_project_for_resource(client, resource_id):
    resp = get_bim_project.sync_detailed(client=client, resource_id=resource_id)
    if resp.parsed is None:
        return None
    return resp.parsed.id


# In main() for project_attr_extraction:
# resources = list_bim_resources_in_project(client, ctx.system_project_id)
# for r in resources:
#     bim_project_id = resolve_bim_project_for_resource(client, r["id"])
#     if bim_project_id is None:
#         continue  # IFC not converted yet — skip or mark needs_review
#     ...
```

If the spatial question is scoped to one IFC file, pick the single resource
explicitly (user picks from a UI, or it is the only IFC in the project). If
the question spans multiple IFCs, iterate and merge — but cite back to each
source resource so the user can trace which file every row came from.

If this is a `resource_attr_extraction` or `project_attr_extraction` flow, follow
the production BIM templates' setup pattern before writing results: read
`ctx.system_attribute_definition_ids[0]`, list the dataspace attribute configs
to resolve the configured `attribute_name` and schema, find or create the
attribute instance, write the value/table, create BIM citations, then submit an
approval ticket. Do not create completed attributes directly.

---

## Common discovery targets

Use these as search hints, not as hard-coded truth. Confirm with KV stats,
semantic KV query, and sample fetched elements.

| User concept | Try these values/terms | Notes |
|---|---|---|
| Room / space | `IfcSpace`, `Room`, `Rooms`, `Space`, `Spaces`, `OST_Rooms`, `OST_MEPSpaces` | Revit rooms and IFC spaces may appear under different keys. |
| Bedroom | `Bedroom`, `bedroom`, `Bed Room`, `寝室`, `主寝室`, `洋室`, `個室` | In Japanese apartment models, `洋室` can be a bedroom-like private room; confirm with user/domain context if needed. |
| Door | `IfcDoor`, `Door`, `Doors`, `OST_Doors`, `ドア`, `扉`, `建具` | `建具` can include doors/windows/fixtures; narrow further when possible. |
| Window | `IfcWindow`, `Window`, `Windows`, `OST_Windows`, `窓`, `サッシ` | Useful for facade/opening questions. |
| Wall | `IfcWall`, `IfcWallStandardCase`, `Wall`, `Walls`, `OST_Walls`, `壁` | Doors often spatially overlap walls more than rooms. |
| Storey / level | `Building Storey`, `Level`, `Base Level`, `Base Constraint`, `Story`, `Floor`, `階` | Use storey filtering before spatial grouping. |
| Name-like fields | `Name`, `name`, `Type`, `Family`, `ObjectType`, `LongName`, `Category` | Inspect actual stats before choosing fields. |

---

## Core helpers

Use these helpers in exploratory scripts and OpenFlows.

```python
import json
import math
import time
from typing import Any


def parse_ndjson_ids(content: str) -> list[str]:
    ids: list[str] = []
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            ids.append(line.strip('"'))
            continue
        if isinstance(obj, str):
            ids.append(obj)
        elif isinstance(obj, dict) and "id" in obj:
            ids.append(str(obj["id"]))
        else:
            ids.append(str(obj))
    return ids


def parse_streamed_elements(content: bytes) -> list[dict[str, Any]]:
    elements: list[dict[str, Any]] = []
    for raw_line in content.decode("utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        wrapper = json.loads(line)
        if isinstance(wrapper, dict) and wrapper.get("found") is False:
            continue
        data = wrapper.get("data", wrapper) if isinstance(wrapper, dict) else wrapper
        if isinstance(data, str):
            data = json.loads(data)
        if isinstance(data, dict):
            props = data.get("properties")
            if isinstance(props, str):
                data["properties"] = json.loads(props)
            elements.append(data)
    return elements


def get_nested(obj: Any, *path: str) -> Any:
    cur = obj
    for part in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur


def as_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, dict) and "value" in value:
        value = value["value"]
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
```

---

## Discover keys and values

Semantic KV query is the fastest way to discover likely keys/values from natural
language. KV stats is the fallback when embeddings are unavailable or too vague.

```python
from tektome.endpoints.api.bim import search_kv_embeddings_from_query
from tektome.endpoints.models.bim_query_to_keys_values_request import (
    BimQueryToKeysValuesRequest,
)


def semantic_kv_probe(client, bim_project_id, query: str) -> dict[str, Any]:
    resp = search_kv_embeddings_from_query.sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=BimQueryToKeysValuesRequest(query=query),
        limit=50,
    )
    data = json.loads(resp.content.decode("utf-8", errors="replace"))
    if resp.status_code.value != 200:
        return {"keys": [], "values": [], "error": data}
    return data


room_hints = semantic_kv_probe(client, bim_project_id, "bedrooms rooms spaces")
door_hints = semantic_kv_probe(client, bim_project_id, "doors door openings")
storey_hints = semantic_kv_probe(client, bim_project_id, "floor level building storey")
```

Convert probe output into an expression automatically so the weakest part of
the flow (hand-writing an OR string) is not a judgement call:

```python
def kv_hints_to_expression(hints: dict[str, Any], extras: list[str] | None = None) -> str:
    """
    Build an expression-search query from a semantic_kv_probe result plus any
    domain terms the probe did not surface (common when the model uses
    Japanese-only labels but the user asked in English).
    """
    terms: list[str] = []
    seen: set[str] = set()
    for bucket in ("values", "keys"):
        for item in hints.get(bucket, []) or []:
            text = item if isinstance(item, str) else (item.get("value") or item.get("key"))
            if not text:
                continue
            key = text.lower().strip()
            if key in seen:
                continue
            seen.add(key)
            # Quote anything with whitespace or non-ASCII (Japanese, punctuation).
            needs_quote = any(c.isspace() for c in text) or any(ord(c) > 127 for c in text)
            terms.append(f'"{text}"' if needs_quote else text)
    for extra in extras or []:
        key = extra.lower().strip()
        if key and key not in seen:
            seen.add(key)
            needs_quote = any(c.isspace() for c in extra) or any(ord(c) > 127 for c in extra)
            terms.append(f'"{extra}"' if needs_quote else extra)
    return "(" + " OR ".join(terms) + ")" if terms else ""


# Always top up with domain-specific extras the probe may have missed.
bedroom_expression = kv_hints_to_expression(
    room_hints,
    extras=["IfcSpace", "Rooms", "Bedroom", "寝室", "主寝室", "洋室"],
)
door_expression = kv_hints_to_expression(
    door_hints,
    extras=["IfcDoor", "Doors", "Door", "ドア", "扉"],
)
```

If semantic query is not useful, call `generate_bim_key_value_stats` and
`get_bim_key_value_stats`, then inspect the available keys and common values.
Use that to build search expressions.

---

## Search element IDs

Use expression search when you need combinations, alternatives, or exclusions.

```python
from tektome.endpoints.api.bim import stream_bim_element_value_expression_search
from tektome.endpoints.models.bim_value_expression_search_post_in import (
    BimValueExpressionSearchPostIn,
)


def search_ids_by_expression(client, bim_project_id, expression: str) -> list[str]:
    resp = stream_bim_element_value_expression_search.sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=BimValueExpressionSearchPostIn(query=expression),
    )
    if resp.status_code.value != 200:
        raise RuntimeError(
            f"BIM expression search failed: {resp.status_code.value} "
            f"{resp.content.decode('utf-8', errors='replace')}"
        )
    return parse_ndjson_ids(resp.content.decode("utf-8", errors="replace"))


bedroom_ids = search_ids_by_expression(
    client,
    bim_project_id,
    '(IfcSpace OR Rooms OR Spaces OR Bedroom OR "寝室" OR "主寝室" OR "洋室")',
)
door_ids = search_ids_by_expression(
    client,
    bim_project_id,
    '(IfcDoor OR Doors OR Door OR "ドア" OR "扉")',
)
```

Use key-value search when you already know the exact key/value pair.

```python
from tektome.endpoints.api.bim import stream_bim_element_key_value_search
from tektome.endpoints.models.bim_key_value_search_post_v2_request import (
    BimKeyValueSearchPostV2Request,
)
from tektome.endpoints.models.stream_bim_element_key_value_search_bim_element_type_v2_path import (
    StreamBimElementKeyValueSearchBimElementTypeV2Path,
)


def search_ids_by_kv(client, bim_project_id, key: str, value: str) -> list[str]:
    resp = stream_bim_element_key_value_search.sync_detailed(
        bim_element=StreamBimElementKeyValueSearchBimElementTypeV2Path.OBJECT,
        bim_project_id=bim_project_id,
        client=client,
        body=BimKeyValueSearchPostV2Request(key=key, value=value),
    )
    if resp.status_code.value != 200:
        raise RuntimeError(
            f"BIM KV search failed: {resp.status_code.value} "
            f"{resp.content.decode('utf-8', errors='replace')}"
        )
    return parse_ndjson_ids(resp.content.decode("utf-8", errors="replace"))
```

After searching, fetch a few samples and inspect them. If the candidates are
wrong, adjust the query. Do not keep building spatial logic on bad IDs.

---

## Fetch light metadata first

For spatial OpenFlows, you usually need names, types, storeys, properties, and
bboxes. Try trimmed fetch first. If the model does not return bboxes through the
trim query, use full fetch only for the small candidate sets you need.

```python
from tektome.endpoints.api.bim import stream_trim_batch_bim_elements
from tektome.endpoints.models.bim_trim_query_item import BimTrimQueryItem
from tektome.endpoints.models.create_bim_batch_trim_element_request_request import (
    CreateBimBatchTrimElementRequestRequest,
)
from tektome.endpoints.models.stream_trim_batch_bim_elements_bim_element_type_path import (
    StreamTrimBatchBimElementsBimElementTypePath,
)


def fetch_light_elements(client, ids: list[str]) -> list[dict[str, Any]]:
    if not ids:
        return []
    resp = stream_trim_batch_bim_elements.sync_detailed(
        bim_type=StreamTrimBatchBimElementsBimElementTypePath.OBJECT,
        client=client,
        body=CreateBimBatchTrimElementRequestRequest(
            ids=ids,
            trim_query=BimTrimQueryItem(
                fields=[
                    "id",
                    "name",
                    "ifcType",
                    "bboxes",
                    "properties",
                    "properties.Building Storey",
                    "properties.Property Sets.Other.Category",
                    "properties.Property Sets.Other.Family",
                    "properties.Property Sets.Other.Type",
                ],
                any_level=True,
                max_depth=12,
            ),
        ),
    )
    if resp.status_code.value != 200:
        raise RuntimeError(
            f"BIM trim fetch failed: {resp.status_code.value} "
            f"{resp.content.decode('utf-8', errors='replace')}"
        )
    return parse_streamed_elements(resp.content)
```

For very large result sets, sample first:

```python
sample_rooms = fetch_light_elements(client, bedroom_ids[:20])
sample_doors = fetch_light_elements(client, door_ids[:20])
```

Check whether sample names, categories, and storeys match the user's request.

---

## Bboxes and centroids

Many spatial tasks only need bboxes and centroids. Prefer stored bboxes when
available. A bbox usually has this shape:

```json
{
  "BBoxMin": {"x": 0.0, "y": 0.0, "z": 0.0},
  "BBoxMax": {"x": 1000.0, "y": 2000.0, "z": 3000.0}
}
```

Use robust extraction because the exact payload shape can vary.

```python
Point = dict[str, float]
BBox = dict[str, Point]


def normalize_point(point: Any) -> Point | None:
    if not isinstance(point, dict):
        return None
    x = as_float(point.get("x"))
    y = as_float(point.get("y"))
    z = as_float(point.get("z"))
    if x is None or y is None or z is None:
        return None
    return {"x": x, "y": y, "z": z}


def normalize_bbox(raw: Any) -> BBox | None:
    if not isinstance(raw, dict):
        return None
    min_pt = normalize_point(raw.get("BBoxMin") or raw.get("min") or raw.get("Min"))
    max_pt = normalize_point(raw.get("BBoxMax") or raw.get("max") or raw.get("Max"))
    if not min_pt or not max_pt:
        return None
    return {"min": min_pt, "max": max_pt}


def extract_bboxes(element: dict[str, Any]) -> list[BBox]:
    candidates: list[Any] = []
    for key in ("bboxes", "bbox", "boundingBox", "bounding_box"):
        value = element.get(key)
        if value:
            candidates.append(value)
    props = element.get("properties")
    if isinstance(props, dict):
        for key in ("bboxes", "bbox", "Bounding Box", "Element Bounding Boxes"):
            value = props.get(key)
            if value:
                candidates.append(value)

    out: list[BBox] = []
    for candidate in candidates:
        if isinstance(candidate, list):
            out.extend(b for item in candidate if (b := normalize_bbox(item)))
        else:
            bbox = normalize_bbox(candidate)
            if bbox:
                out.append(bbox)
    return out


def bbox_centroid(bbox: BBox) -> Point:
    return {
        "x": (bbox["min"]["x"] + bbox["max"]["x"]) / 2,
        "y": (bbox["min"]["y"] + bbox["max"]["y"]) / 2,
        "z": (bbox["min"]["z"] + bbox["max"]["z"]) / 2,
    }


def expand_bbox(bbox: BBox, xy: float = 0.0, z: float = 0.0) -> BBox:
    return {
        "min": {
            "x": bbox["min"]["x"] - xy,
            "y": bbox["min"]["y"] - xy,
            "z": bbox["min"]["z"] - z,
        },
        "max": {
            "x": bbox["max"]["x"] + xy,
            "y": bbox["max"]["y"] + xy,
            "z": bbox["max"]["z"] + z,
        },
    }
```

If an element has multiple bboxes, either keep all of them or combine them into
one envelope:

```python
def combine_bboxes(bboxes: list[BBox]) -> BBox | None:
    if not bboxes:
        return None
    return {
        "min": {
            "x": min(b["min"]["x"] for b in bboxes),
            "y": min(b["min"]["y"] for b in bboxes),
            "z": min(b["min"]["z"] for b in bboxes),
        },
        "max": {
            "x": max(b["max"]["x"] for b in bboxes),
            "y": max(b["max"]["y"] for b in bboxes),
            "z": max(b["max"]["z"] for b in bboxes),
        },
    }
```

---

## Topology search is the default spatial test

Topology search runs on the backend. Use it to ask "which of these candidate
objects overlap this box/sphere/prism?" It is the right default because it can
use stored bboxes and backend geometry handling.

Topology search is async. It returns a `process_id`, then you poll the background
task endpoint.

```python
from tektome.endpoints.api.bim import bim_topology_search_box
from tektome.endpoints.api.tasks import get_celery_task
from tektome.endpoints.models.bim_topology_search_box_post_in import (
    BimTopologySearchBoxPostIn,
)
from tektome.endpoints.models.boundary import Boundary


# Authoritative celery status set (from /api/core/tasks/{task_id}/):
#   PENDING | RECEIVED | STARTED | SUCCESS | FAILURE | REVOKED | REJECTED
#   | RETRY | IGNORED
# Payload shape: {"status": str, "result": any}. There is no "state" key,
# no "COMPLETED", no "FAILED".
IN_FLIGHT_TASK_STATUSES = {"PENDING", "RECEIVED", "STARTED", "RETRY"}
TERMINAL_FAIL_TASK_STATUSES = {"FAILURE", "REVOKED", "REJECTED", "IGNORED"}


def task_payload(task) -> dict[str, Any]:
    # GetCeleryTaskResponse stores the raw dict under additional_properties;
    # to_dict() returns it verbatim.
    if task is None:
        return {}
    if hasattr(task, "to_dict"):
        return task.to_dict()
    if isinstance(task, dict):
        return task
    return {}


def poll_process_result(client, process_id: str, timeout_s: int = 180) -> Any:
    deadline = time.time() + timeout_s
    last_status: str | None = None
    while time.time() < deadline:
        resp = get_celery_task.sync_detailed(task_id=process_id, client=client)
        data = task_payload(resp.parsed)
        status = data.get("status")
        if status == "SUCCESS":
            return data.get("result")
        if status in TERMINAL_FAIL_TASK_STATUSES:
            raise RuntimeError(f"BIM async task failed ({status}): {data}")
        if status not in IN_FLIGHT_TASK_STATUSES and status is not None:
            # Unknown status — fail loud rather than spin forever.
            raise RuntimeError(f"Unexpected celery task status: {status!r} ({data})")
        last_status = status
        time.sleep(3)
    raise TimeoutError(
        f"BIM async task did not finish in {timeout_s}s "
        f"(process_id={process_id}, last_status={last_status!r})"
    )


def topology_box_ids(
    client,
    bim_project_id,
    candidate_ids: list[str],
    bbox: BBox,
    *,
    strict_contains: bool = False,
    use_vertices: bool = False,
) -> list[str]:
    resp = bim_topology_search_box.sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=BimTopologySearchBoxPostIn(
            bim_object_ids=candidate_ids,
            min_boundary=Boundary(**bbox["min"]),
            max_boundary=Boundary(**bbox["max"]),
            strict_contains=strict_contains,
            use_vertices=use_vertices,
        ),
    )
    if resp.status_code.value != 200 or not resp.parsed:
        raise RuntimeError(
            f"Topology search failed to start: {resp.status_code.value} "
            f"{resp.content.decode('utf-8', errors='replace')}"
        )
    result = poll_process_result(client, resp.parsed.process_id)
    if isinstance(result, list):
        return [str(x) for x in result]
    if isinstance(result, dict):
        ids = result.get("ids") or result.get("bim_object_ids") or result.get("result")
        if isinstance(ids, list):
            return [str(x) for x in ids]
    raise RuntimeError(f"Unexpected topology result shape: {result}")
```

Use `strict_contains=False` for most "near/in/touching" questions. Use
`strict_contains=True` only when the user explicitly asks for elements fully
inside a volume. Keep `use_vertices=False` by default. Vertex mode is more
precise, but heavier.

---

## Storey filtering

Always try to group spatial analysis by storey/floor before doing 3D checks.
This prevents accidentally matching objects above or below the target space.

```python
STOREY_KEYS = [
    ("properties", "Building Storey"),
    ("properties", "Building Storey", "name"),
    ("properties", "Building Storey", "value"),
    ("properties", "Property Sets", "Constraints", "Level"),
    ("properties", "Property Sets", "Constraints", "Base Constraint"),
    ("properties", "Property Sets", "Other", "Level"),
]


def text_value(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, dict):
        for key in ("value", "name", "displayValue"):
            if key in value:
                return text_value(value[key])
        return None
    text = str(value).strip()
    return text or None


def element_storey(element: dict[str, Any]) -> str | None:
    for path in STOREY_KEYS:
        value = text_value(get_nested(element, *path))
        if value:
            return value
    return None
```

If storey is not available, use `z` ranges from bboxes as the fallback.

---

## Recipe: bedrooms and doors

Use this recipe for "find all bedrooms and count doors for each bedroom."

1. Discover room/door/storey keys with semantic KV query and/or KV stats.
2. Search bedroom/room IDs and door IDs.
3. Fetch light room and door metadata.
4. Reject obvious false positives by name/type/category.
5. For each bedroom, get its bbox envelope.
6. Expand the bbox by 300-500 mm in X/Y so boundary doors can match.
7. Limit candidate doors to the same storey if possible.
8. Run topology box search against the door candidates.
9. If a door matches multiple rooms, keep both or mark the association as
   ambiguous. Do not silently pretend it is exact.
10. Output a table and cite the room and matched doors.

```python
def is_probable_bedroom(element: dict[str, Any]) -> bool:
    text = " ".join(
        str(x or "")
        for x in [
            element.get("name"),
            element.get("ifcType"),
            get_nested(element, "properties", "Name"),
            get_nested(element, "properties", "LongName"),
            get_nested(element, "properties", "Property Sets", "Other", "Category"),
        ]
    ).lower()
    raw = text + " " + str(element)
    return any(
        term.lower() in raw.lower()
        for term in ["bedroom", "bed room", "寝室", "主寝室", "洋室"]
    )


def is_probable_door(element: dict[str, Any]) -> bool:
    raw = " ".join(
        str(x or "")
        for x in [
            element.get("name"),
            element.get("ifcType"),
            get_nested(element, "properties", "Property Sets", "Other", "Category"),
            get_nested(element, "properties", "Property Sets", "Other", "Family"),
            get_nested(element, "properties", "Property Sets", "Other", "Type"),
        ]
    ).lower()
    return any(term.lower() in raw for term in ["ifcdoor", "door", "doors", "ドア", "扉"])


rooms = [e for e in fetch_light_elements(client, bedroom_ids) if is_probable_bedroom(e)]
doors = [e for e in fetch_light_elements(client, door_ids) if is_probable_door(e)]
door_by_id = {str(d.get("id")): d for d in doors if d.get("id")}

rows: list[dict[str, Any]] = []
for room in rooms:
    room_id = str(room.get("id"))
    room_bbox = combine_bboxes(extract_bboxes(room))
    if not room_bbox:
        rows.append({
            "room_id": room_id,
            "room_name": room.get("name"),
            "status": "no_bbox",
            "door_count": None,
        })
        continue

    room_storey = element_storey(room)
    same_storey_door_ids = [
        door_id
        for door_id, door in door_by_id.items()
        if not room_storey or not element_storey(door) or element_storey(door) == room_storey
    ]

    search_bbox = expand_bbox(room_bbox, xy=500.0, z=100.0)
    matched_door_ids = topology_box_ids(
        client,
        bim_project_id,
        same_storey_door_ids,
        search_bbox,
        strict_contains=False,
        use_vertices=False,
    )

    rows.append({
        "room_id": room_id,
        "room_name": room.get("name"),
        "storey": room_storey,
        "room_centroid": bbox_centroid(room_bbox),
        "room_bbox_min": room_bbox["min"],
        "room_bbox_max": room_bbox["max"],
        "door_count": len(matched_door_ids),
        "door_ids": matched_door_ids,
        "door_centroids": [
            bbox_centroid(b)
            for door_id in matched_door_ids
            for b in [combine_bboxes(extract_bboxes(door_by_id.get(door_id, {})))]
            if b
        ],
        "status": "ok",
    })
```

Persist `rows` as a table attribute. Cite each row's room and matched door
elements with BIM citations. If you create visual aids, place a text label at
`room_centroid` with the door count.

---

## Recipe: where is this object located?

Use this for "where is the pump?", "where is wall W1?", or "where are the fire
doors?"

1. Use semantic KV query for the object name/type.
2. Search element IDs.
3. Fetch light metadata and bboxes.
4. Report name, type, storey, bbox, and centroid.
5. Optionally cite the element and create a text label at the centroid.

```python
def describe_location(element: dict[str, Any]) -> dict[str, Any]:
    bbox = combine_bboxes(extract_bboxes(element))
    return {
        "element_id": element.get("id"),
        "name": element.get("name"),
        "ifc_type": element.get("ifcType"),
        "storey": element_storey(element),
        "bbox_min": bbox["min"] if bbox else None,
        "bbox_max": bbox["max"] if bbox else None,
        "centroid": bbox_centroid(bbox) if bbox else None,
        "status": "ok" if bbox else "no_bbox",
    }
```

If multiple objects match, return a table sorted by storey, name, then element
ID. If the user gave an ambiguous name, do not collapse results into one object.

---

## Recipe: which objects are inside this room or area?

Use this for "find furniture in room 101", "list equipment in this room", or
"which objects are in this zone?"

1. Search and fetch the room/zone element.
2. Search target object candidates by type/name.
3. Build an expanded room bbox or prism.
4. Run topology search against target candidates.
5. Return matched objects with locations and citations.

For room-like elements, use an expanded bbox first. If you have a reliable
polygon footprint, use prism search instead of box search. Prism search is
better for irregular rooms, but only if the footprint is trustworthy.

---

## Recipe: nearby objects by radius (sphere search)

Use this for "find objects within 2m of the column", "which fire extinguishers
are near this door?", or any "nearby / within X distance" question where the
user's mental model is a radius, not an axis-aligned box.

1. Resolve the anchor element and get its centroid.
2. Search the candidate pool by name/type (the things you want to find near
   the anchor).
3. Run `bim_topology_search_sphere` with `center_point=Point3D(...)` and
   `radius` in the model's native unit.
4. Poll the celery task and return hits.

```python
from tektome.endpoints.api.bim import bim_topology_search_sphere
from tektome.endpoints.models.bim_topology_search_sphere_post_in import (
    BimTopologySearchSpherePostIn,
)
from tektome.endpoints.models.point_3d import Point3D


def topology_sphere_ids(
    client,
    bim_project_id,
    candidate_ids: list[str],
    center: Point,
    radius: float,
    *,
    strict_contains: bool = False,
    use_vertices: bool = False,
) -> list[str]:
    """
    radius is in the model's native unit. For a millimetre model, 2 metres
    == 2000.0. Verify the unit with a sample bbox before picking the number.
    """
    resp = bim_topology_search_sphere.sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=BimTopologySearchSpherePostIn(
            bim_object_ids=candidate_ids,
            center_point=Point3D(x=center["x"], y=center["y"], z=center["z"]),
            radius=radius,
            strict_contains=strict_contains,
            use_vertices=use_vertices,
        ),
    )
    if resp.status_code.value != 200 or not resp.parsed:
        raise RuntimeError(
            f"Sphere topology search failed to start: {resp.status_code.value} "
            f"{resp.content.decode('utf-8', errors='replace')}"
        )
    result = poll_process_result(client, resp.parsed.process_id)
    if isinstance(result, list):
        return [str(x) for x in result]
    if isinstance(result, dict):
        ids = result.get("ids") or result.get("bim_object_ids") or result.get("result")
        if isinstance(ids, list):
            return [str(x) for x in ids]
    raise RuntimeError(f"Unexpected sphere topology result shape: {result}")
```

Anchor the sphere on the anchor element's bbox centroid, not its raw origin.
For elongated anchors (walls, beams) a sphere is a poor shape — use box or
prism instead.

---

## Recipe: prism search (irregular footprints)

Use prism search when the area you want to test is a non-rectangular polygon
— L-shaped rooms, apartment units with alcoves, zones defined by a plan
drawing. Prism = 2D polygon extruded vertically between optional `z_min`
and `z_max`.

The polygon must be **ordered**, **non-self-intersecting**, have **≥3
distinct points**, and **non-zero area**. The backend rejects payloads that
violate any of these.

```python
from tektome.endpoints.api.bim import bim_topology_search_prism
from tektome.endpoints.models.bim_topology_search_prism_post_in import (
    BimTopologySearchPrismPostIn,
)
from tektome.endpoints.models.point_2d import Point2D


def topology_prism_ids(
    client,
    bim_project_id,
    candidate_ids: list[str],
    outline_xy: list[tuple[float, float]],
    *,
    z_min: float | None = None,
    z_max: float | None = None,
    strict_contains: bool = False,
    use_vertices: bool = False,
) -> list[str]:
    body_kwargs: dict[str, Any] = {
        "bim_object_ids": candidate_ids,
        "base_outline": [Point2D(x=x, y=y) for x, y in outline_xy],
        "strict_contains": strict_contains,
        "use_vertices": use_vertices,
    }
    if z_min is not None:
        body_kwargs["z_min"] = z_min
    if z_max is not None:
        body_kwargs["z_max"] = z_max

    resp = bim_topology_search_prism.sync_detailed(
        bim_project_id=bim_project_id,
        client=client,
        body=BimTopologySearchPrismPostIn(**body_kwargs),
    )
    if resp.status_code.value != 200 or not resp.parsed:
        raise RuntimeError(
            f"Prism topology search failed to start: {resp.status_code.value} "
            f"{resp.content.decode('utf-8', errors='replace')}"
        )
    result = poll_process_result(client, resp.parsed.process_id)
    if isinstance(result, list):
        return [str(x) for x in result]
    if isinstance(result, dict):
        ids = result.get("ids") or result.get("bim_object_ids") or result.get("result")
        if isinstance(ids, list):
            return [str(x) for x in ids]
    raise RuntimeError(f"Unexpected prism topology result shape: {result}")
```

### Where to get the polygon

In descending order of preference:

1. **Real room footprint** from the element's geometry (`vertices`, outer
   boundary of `displayValue`). This is what makes prism worth the extra
   effort.
2. **Bbox corners as a last-resort rectangle.** If you do not have a
   footprint, prism degrades into box search — use box search directly
   instead; prism adds nothing here.
3. **Hand-specified polygon from the user** (e.g. they dragged a zone in a
   plan). Validate winding order and non-self-intersection before sending.

Pick `z_min`/`z_max` from the room's bbox with a small slack (e.g.
`bbox.min.z - 50` to `bbox.max.z + 50` in millimetres) so elements just
above the floor slab or just below the ceiling are not missed. Leave both
as `None` only when you truly want an unbounded vertical sweep.

---

## Recipe: distance between elements

Use centroid distance for a quick answer. Use bbox distance when the user cares
about nearest physical separation. If bboxes overlap, physical separation is
zero or the elements intersect.

```python
def point_distance(a: Point, b: Point) -> float:
    return math.sqrt(
        (a["x"] - b["x"]) ** 2
        + (a["y"] - b["y"]) ** 2
        + (a["z"] - b["z"]) ** 2
    )


def bbox_distance(a: BBox, b: BBox) -> float:
    dx = max(a["min"]["x"] - b["max"]["x"], b["min"]["x"] - a["max"]["x"], 0.0)
    dy = max(a["min"]["y"] - b["max"]["y"], b["min"]["y"] - a["max"]["y"], 0.0)
    dz = max(a["min"]["z"] - b["max"]["z"], b["min"]["z"] - a["max"]["z"], 0.0)
    return math.sqrt(dx * dx + dy * dy + dz * dz)
```

Return the unit with the value. Coordinates are in the model's native unit
system (see Invariants); most Japanese Revit/IFC exports are millimetres, but
confirm against a known real-world dimension before converting. Example
millimetre case:

```python
# Assumes you verified the model is in millimetres from a sample element.
distance_mm = bbox_distance(a_bbox, b_bbox)
distance_m = distance_mm / 1000.0
```

If unit is ambiguous, return the raw value plus an `assumed_unit` column
(`"mm"`, `"m"`, or `"unknown"`) so the user can interpret. Do not silently
divide by 1000.

Do not call this a route distance or walking distance. It is geometric distance
between element bboxes or centroids.

---

## Raw geometry fallback

Only use full JSON geometry parsing when bboxes/topology are missing,
ambiguous, or insufficient for the user's question.

Fallback order:

1. Check fetched `bboxes` or bbox-like fields.
2. If absent, inspect one full element JSON sample to find geometry shape.
3. Look for `displayValue`, `definition.displayValue`, nested `elements`,
   `vertices`, `faces`, and `transform`.
4. Apply transforms before computing bboxes or distances.
5. Use `numpy` if available; otherwise compute min/max with plain Python.
6. Record that the result was derived from fallback geometry.

Plain Python bbox from flat vertices:

```python
def bbox_from_vertices(vertices: list[float]) -> BBox | None:
    if not vertices or len(vertices) < 3:
        return None
    points = list(zip(vertices[0::3], vertices[1::3], vertices[2::3]))
    if not points:
        return None
    return {
        "min": {
            "x": min(p[0] for p in points),
            "y": min(p[1] for p in points),
            "z": min(p[2] for p in points),
        },
        "max": {
            "x": max(p[0] for p in points),
            "y": max(p[1] for p in points),
            "z": max(p[2] for p in points),
        },
    }
```

This fallback is intentionally incomplete. Speckle-style BIM JSON can contain
nested definitions and transforms. If you cannot prove your fallback handles the
sample correctly, prefer topology search and mark unresolved cases instead of
pretending exact coordinates are known.

---

## Output schema for spatial tables

For table attributes, use stable columns. A good default for room/object spatial
analysis:

| Column | Type | Meaning |
|---|---|---|
| `element_id` | string | BIM object Speckle hash. |
| `name` | string | Element display name. |
| `ifc_type` | string | IFC/Revit type if available. |
| `storey` | string | Floor/level if available. |
| `bbox_min` | string/json | Minimum bbox point. |
| `bbox_max` | string/json | Maximum bbox point. |
| `centroid` | string/json | Bbox centroid. |
| `matched_element_ids` | string/json | Related objects, such as doors in a room. |
| `count` | integer | Count of matched objects. |
| `method` | string | `topology_bbox`, `topology_vertices`, `stored_bbox`, or `raw_geometry_fallback`. |
| `notes` | string | Ambiguity, missing bbox, multiple rooms, etc. |

For bedroom-door counts, use columns such as:

```text
room_id, room_name, storey, room_centroid, room_bbox_min, room_bbox_max,
door_count, door_ids, door_centroids, method, notes
```

Keep raw lists as JSON strings if the table column type cannot store structured
objects directly.

---

## Citation and visual-aid guidance

Every spatial result should be traceable.

- Cite the source BIM elements used for the result.
- For a room-door row, cite the room and all matched doors when practical.
- If there are too many matched elements, cite the room and a representative
  subset, then store the full ID list in the table.
- Use custom BIM text labels for concise visual summaries, such as `Doors: 2`
  at the room centroid.
- Use highlight colors on cited elements when the viewer supports it.

Do not create completed attributes directly. For extraction flows, leave results
pending approval and submit approval-ticket candidates as described in
[MANUAL_ATTRIBUTES_AND_CITATIONS.md](MANUAL_ATTRIBUTES_AND_CITATIONS.md).

---

## Common mistakes

| Mistake | Why it fails | Better approach |
|---|---|---|
| Hard-coding `Category == Rooms` | Models vary. Rooms may be `IfcSpace`, `Spaces`, Japanese names, or custom values. | Probe KV stats/query first. |
| Fetching every full BIM object | Payloads are large and slow. | Search IDs, trimmed fetch, topology/bbox first. |
| Treating topology `process_id` as results | Box/prism/sphere topology are all async. | Poll `get_celery_task`; treat only `status=="SUCCESS"` as done. |
| Polling for `status in {"COMPLETED","FAILED"}` or `data["state"]` | Those keys/values do not exist. The real set is `PENDING/RECEIVED/STARTED/SUCCESS/FAILURE/REVOKED/REJECTED/RETRY/IGNORED` with key `"status"`. | Use `IN_FLIGHT_TASK_STATUSES` / `TERMINAL_FAIL_TASK_STATUSES` from this playbook. |
| Hard-coding millimetres for every model | Some models are authored in metres. A `radius=2000` in a metre model searches a 2km sphere. | Sample a known bbox and pick the unit before sending any `radius`/`expand_bbox` value. |
| Checking `if ctx.system_resource_id is None` | Guarded fields raise `AttributeError` when unset, not return `None`. | `try: rid = ctx.system_resource_id / except AttributeError: ...`, or dispatch on `ctx.system_flow_type`. |
| Counting only doors whose centroid is inside a room | Doors often sit in wall thickness at the room boundary. | Expand the room bbox/prism and use overlap. |
| Ignoring storey/floor | Objects above/below can spatially overlap in X/Y. | Filter by storey or z range. |
| Using Revit IDs for citations | BIM citations expect Speckle hash element IDs. | Use IDs returned by BIM search/fetch. |
| Calling bbox distance a route distance | It is straight-line geometry, not pathfinding. | Say "geometric distance" unless you compute a route. |
| Pretending ambiguous matches are exact | BIM models are messy. | Return notes/status for ambiguous rows. |

---

## What to do when blocked

If you cannot confidently identify elements or geometry:

1. Return a diagnostic table of candidate keys/values and sample elements.
2. Mark rows as `needs_review`, `no_bbox`, or `ambiguous`.
3. Store enough evidence for a human to inspect: element IDs, names, storeys,
   and the query used.
4. Do not fabricate coordinates or exact relationships.

The useful OpenFlow is the one that exposes uncertainty cleanly and leaves a
reviewable trail.
