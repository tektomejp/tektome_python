# BIM Data and Tools — Agent Reference

This document explains how to query, retrieve, and analyse BIM (Building Information Modeling) data using the Tektome Python SDK. It covers element search, batch retrieval, spatial queries, clash detection, and key-value statistics.

---

## Overview

BIM data in Tektome is organised into **BIM projects** containing three element types:

| Element type | What it represents | SDK path constant |
|---|---|---|
| **BIM Object** | 3D geometry with properties (walls, beams, columns, slabs, etc.) | `StreamBimElementKeyValueSearchBimElementTypeV2Path.OBJECT` |
| **BIM View** | Named camera viewpoints with viewport ranges | `StreamBimElementKeyValueSearchBimElementTypeV2Path.VIEW` |
| **BIM Sheet** | 2D drawing sheets containing view references | `StreamBimElementKeyValueSearchBimElementTypeV2Path.SHEET` |

A BIM project is linked to a **resource** (the uploaded IFC/Revit file). The typical flow for working with BIM data is:

```
resolve BIM project from resource → explore KV stats → KV search for element IDs → batch fetch full elements → extract data → (optional: spatial query / clash check)
```

All BIM endpoints live under `tektome.endpoints.api.bim`.

---

## Step 1 — Resolve the BIM project from a resource

Every BIM workflow starts by finding the BIM project UUID linked to a resource. A resource can have multiple BIM projects (e.g. after re-upload); use `page_size=1` to get the most recent.

```python
from tektome.endpoints.api.bim import list_bim_projects_by_resource

bim_projects_resp = list_bim_projects_by_resource.sync_detailed(
    client=client,
    resource_id=resource_uuid,
    page=1,
    page_size=1,
)
if bim_projects_resp.status_code.value != 200 or not bim_projects_resp.parsed:
    raise RuntimeError(f"No BIM projects for resource {resource_uuid}")

bim_project_id = bim_projects_resp.parsed[0].id
```

Alternatively, via the Lawtalk resource endpoint:

```python
from tektome.endpoints.api.resource import get_lawtalk_resource_bim_project

bim_resp = get_lawtalk_resource_bim_project.sync(
    resource_id=str(resource_uuid),
    client=client,
)
bim_project_id = bim_resp.id
```

---

## Step 2 — Explore available properties (KV Stats)

Before searching, discover what key-value properties exist on elements in a BIM project. Stats are pre-computed and cached in Elasticsearch.

### Generate stats (first time or refresh)

```python
from tektome.endpoints.api.bim import generate_bim_key_value_stats

generate_bim_key_value_stats.sync_detailed(
    bim_project_id=bim_project_id,
    client=client,
    refresh=True,       # force regeneration
    limit_keys=1000,    # max distinct keys to return
    limit_values=50,    # max distinct values per key
)
```

### Retrieve stats

```python
from tektome.endpoints.api.bim import get_bim_key_value_stats

stats = get_bim_key_value_stats.sync(bim_project_id=bim_project_id, client=client)
```

The response contains a summary of all property keys and their most common values, useful for understanding what data is available before writing search queries.

---

## Step 3 — Search for elements by key-value pairs

The primary search mechanism for BIM objects. Returns element IDs as an NDJSON stream.

```python
import json
from tektome.endpoints.api.bim import stream_bim_element_key_value_search
from tektome.endpoints.models.bim_key_value_search_post_v2_request import BimKeyValueSearchPostV2Request
from tektome.endpoints.models.stream_bim_element_key_value_search_bim_element_type_v2_path import (
    StreamBimElementKeyValueSearchBimElementTypeV2Path,
)

kv_resp = stream_bim_element_key_value_search.sync_detailed(
    bim_element=StreamBimElementKeyValueSearchBimElementTypeV2Path.OBJECT,
    bim_project_id=bim_project_id,
    client=client,
    body=BimKeyValueSearchPostV2Request(key="Category", value="Walls"),
)

matched_ids = parse_ndjson_ids(kv_resp.content.decode("utf-8"))
```

### Wildcard support

Both `key` and `value` support `*` wildcards:

| Pattern | Matches |
|---|---|
| `key="Category", value="Walls"` | Exact match |
| `key="Category", value="Wall*"` | Values starting with "Wall" |
| `key="*", value="IfcBeam"` | Any key with value "IfcBeam" |
| `key="Name", value="*Concrete*"` | Names containing "Concrete" |

### Boolean expression search

For complex queries combining multiple conditions, use `stream_bim_element_value_expression_search`:

```python
from tektome.endpoints.api.bim import stream_bim_element_value_expression_search
from tektome.endpoints.models.bim_value_expression_search_post_in import BimValueExpressionSearchPostIn

resp = stream_bim_element_value_expression_search.sync_detailed(
    bim_project_id=bim_project_id,
    client=client,
    body=BimValueExpressionSearchPostIn(query='Category:"Walls" AND Name:"*Concrete*"'),
)
```

Supports `AND`, `OR`, `NOT`, quoted phrases, and wildcards. Max 150,000 results.

### Parsing NDJSON responses

All streaming BIM endpoints return NDJSON (newline-delimited JSON). Use this helper:

```python
def parse_ndjson_ids(content: str) -> list[str]:
    ids = []
    for line in content.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            if isinstance(obj, str):
                ids.append(obj)
            elif isinstance(obj, dict) and "id" in obj:
                ids.append(obj["id"])
            else:
                ids.append(str(obj))
        except json.JSONDecodeError:
            ids.append(line.strip('"'))
    return ids
```

---

## Step 4 — Batch fetch full element data

Once you have element IDs from search, retrieve full element data (properties, geometry, metadata) via streaming.

```python
from tektome.endpoints.api.bim import stream_batch_bim_elements
from tektome.endpoints.models.stream_batch_bim_elements_bim_element_type_path import (
    StreamBatchBimElementsBimElementTypePath,
)
from tektome.endpoints.models.create_bim_batch_element_request_request import (
    CreateBimBatchElementRequestRequest,
)

batch_resp = stream_batch_bim_elements.sync_detailed(
    bim_type=StreamBatchBimElementsBimElementTypePath.OBJECT,
    client=client,
    body=CreateBimBatchElementRequestRequest(ids=matched_ids),
)
```

### Processing the NDJSON response

Each line is a JSON object with `found` (bool) and `data` (the element):

```python
elements = []
for line in batch_resp.content.decode("utf-8").strip().split("\n"):
    line = line.strip()
    if not line:
        continue
    obj = json.loads(line)
    if not obj.get("found", True):
        continue
    data = obj.get("data", {})
    if isinstance(data, str):
        data = json.loads(data)
    properties = data.get("properties", {})
    if isinstance(properties, str):
        properties = json.loads(properties)
    elements.append({"data": data, "properties": properties})
```

### Limits

| Endpoint | Max IDs per request |
|---|---|
| `get_batch_bim_elements` | 50 (non-streaming, returns parsed models) |
| `stream_batch_bim_elements` | 50,000 (NDJSON stream) |
| `stream_bim_element_key_value_search` | 150,000 results |

Always prefer the streaming variants for large datasets.

### Trimmed fetch (select specific fields)

When you only need certain fields, use `stream_trim_batch_bim_elements` to reduce payload size:

```python
from tektome.endpoints.api.bim import stream_trim_batch_bim_elements
from tektome.endpoints.models.create_bim_batch_trim_element_request_request import (
    CreateBimBatchTrimElementRequestRequest,
)
from tektome.endpoints.models.stream_trim_batch_bim_elements_bim_element_type_path import (
    StreamTrimBatchBimElementsBimElementTypePath,
)

from tektome.endpoints.models.bim_trim_query_item import BimTrimQueryItem

resp = stream_trim_batch_bim_elements.sync_detailed(
    bim_type=StreamTrimBatchBimElementsBimElementTypePath.OBJECT,
    client=client,
    body=CreateBimBatchTrimElementRequestRequest(
        ids=matched_ids,
        trim_query=BimTrimQueryItem(
            fields=["id", "name", "ifcType", "properties.Quantities"],
        ),
    ),
)
```

---

## BIM element data structure

Each BIM object has this structure when fetched:

```
data["id"]           — 32-char Speckle hash (element's unique ID)
data["name"]         — display name (e.g. "Basic Wall:200mm RC:2753095")
data["ifcType"]      — IFC classification (e.g. "IfcWall", "IfcBeam")
data["properties"]   — nested dict of all property sets:

    properties["Attributes"]
        IFC entity attributes

    properties["Quantities"]["BaseQuantities"]
        Measured values with units:
        {"Height": {"name": "Height", "value": 2850.0, "units": "Millimetre"}}

    properties["Property Sets"]["Other"]
        Category, Family, Type

    properties["Property Sets"]["Dimensions"]
        Area, Length, Volume

    properties["Property Sets"]["Constraints"]
        Offsets, Height constraints

    properties["Property Sets"]["Structural"]
        Structural usage, rebar cover

    properties["Building Storey"]
        Floor/level name
```

### Element ID format

BIM element IDs are **32-character Speckle hashes** (deterministic SHA-256 derived), not UUIDs. Example: `"a1b2c3d4e5f6789012345678abcdef01"`. This is the value returned by KV search and expected by citation endpoints. Do not confuse with:
- Resource UUIDs (standard UUID format)
- Revit element IDs (numeric, e.g. `"2753095"`)
- BIM project IDs (standard UUID format)

---

## Step 5 — Validate element IDs

Before creating BIM citations, validate that element IDs exist in the project's index. The citation API rejects IDs that are not in the BIM project.

```python
from tektome.endpoints.api.bim import validate_bim_element_ids
from tektome.endpoints.models.bim_validate_ids_request import BimValidateIdsRequest
from tektome.endpoints.models.validate_bim_element_ids_bim_element_type_v2_path import (
    ValidateBimElementIdsBimElementTypeV2Path,
)

validate_resp = validate_bim_element_ids.sync(
    bim_element=ValidateBimElementIdsBimElementTypeV2Path.OBJECT,
    bim_project_id=bim_project_id,
    client=client,
    body=BimValidateIdsRequest(ids=element_ids),
)
```

Max 500 IDs per request. The response indicates which IDs are valid vs missing.

An alternative validation approach is to stream all project element IDs and filter locally:

```python
from tektome.endpoints.api.bim import stream_bim_elements_by_project
from tektome.endpoints.models.stream_bim_elements_by_project_bim_element_type_v2_path import (
    StreamBimElementsByProjectBimElementTypeV2Path,
)

all_resp = stream_bim_elements_by_project.sync_detailed(
    bim_project_id=bim_project_id,
    bim_type=StreamBimElementsByProjectBimElementTypeV2Path.OBJECT,
    client=client,
    id_only=True,
)

valid_ids = parse_id_response(all_resp.content.decode("utf-8"))
filtered = [eid for eid in element_ids if eid in valid_ids]
```

Where `parse_id_response` handles both `{"ids": [...]}` and NDJSON formats:

```python
def parse_id_response(content: str) -> set[str]:
    try:
        parsed = json.loads(content)
        if isinstance(parsed, dict) and "ids" in parsed:
            return set(parsed["ids"])
        if isinstance(parsed, list):
            return set(parsed)
    except json.JSONDecodeError:
        pass
    return set(parse_ndjson_ids(content))
```

---

## Spatial queries — Topology Search

Find BIM objects within a defined 3D region. Three geometry types are supported:

### Box search (axis-aligned)

```python
from tektome.endpoints.api.bim import bim_topology_search_box
from tektome.endpoints.models.bim_topology_search_box_post_in import BimTopologySearchBoxPostIn
from tektome.endpoints.models.boundary import Boundary

result = bim_topology_search_box.sync(
    bim_project_id=bim_project_id,
    client=client,
    body=BimTopologySearchBoxPostIn(
        bim_object_ids=element_ids,  # list of element IDs to test
        min_boundary=Boundary(x=0.0, y=0.0, z=0.0),
        max_boundary=Boundary(x=10000.0, y=10000.0, z=3000.0),
    ),
)
```

### Sphere search (radial)

```python
from tektome.endpoints.api.bim import bim_topology_search_sphere
from tektome.endpoints.models.bim_topology_search_sphere_post_in import BimTopologySearchSpherePostIn
from tektome.endpoints.models.point_3d import Point3D

result = bim_topology_search_sphere.sync(
    bim_project_id=bim_project_id,
    client=client,
    body=BimTopologySearchSpherePostIn(
        bim_object_ids=element_ids,  # list of element IDs to test
        center_point=Point3D(x=5000.0, y=5000.0, z=1500.0),
        radius=2000.0,
    ),
)
```

### Prism search (vertical column)

```python
from tektome.endpoints.api.bim import bim_topology_search_prism
from tektome.endpoints.models.bim_topology_search_prism_post_in import BimTopologySearchPrismPostIn
from tektome.endpoints.models.point_2d import Point2D

result = bim_topology_search_prism.sync(
    bim_project_id=bim_project_id,
    client=client,
    body=BimTopologySearchPrismPostIn(
        bim_object_ids=element_ids,  # list of element IDs to test
        base_outline=[
            Point2D(x=0.0, y=0.0), Point2D(x=10000.0, y=0.0),
            Point2D(x=10000.0, y=10000.0), Point2D(x=0.0, y=10000.0),
        ],
        z_min=0.0,
        z_max=3000.0,
    ),
)
```

All coordinates are in **millimetres**. Results return element IDs that intersect with or are contained within the search region.

---

## Clash detection

Check for geometric collisions between BIM objects. Uses a two-phase approach: fast bounding-box overlap, then precise ray-casting penetration detection.

```python
from tektome.endpoints.api.bim import bim_clash_check
from tektome.endpoints.models.create_bim_clash_check_request import CreateBimClashCheckRequest

resp = bim_clash_check.sync_detailed(
    bim_project_id=bim_project_id,
    client=client,
    body=CreateBimClashCheckRequest(
        bim_object_ids=element_ids,  # list of element IDs to check (min 2, max 1000)
    ),
)
```

This is an **async operation** — the response contains a task ID. Poll with `get_bim_task`:

```python
from tektome.endpoints.api.bim import get_bim_task
import time

task_id = UUID(resp.parsed.process_id)
while True:
    task = get_bim_task.sync(bim_task_id=task_id, client=client)
    if task.status in ("COMPLETED", "FAILED"):
        break
    time.sleep(3)
```

---

## Views and sheets

### List views in a project

```python
from tektome.endpoints.api.bim import list_bim_views_in_project
from tektome.endpoints.models.create_retrieve_bim_views_in_project_request import (
    CreateRetrieveBimViewsInProjectRequest,
)

views = list_bim_views_in_project.sync(
    client=client,
    body=CreateRetrieveBimViewsInProjectRequest(
        bim_project_id=bim_project_id,
        page=1,
        page_size=100,
    ),
)
```

### List sheets in a project

```python
from tektome.endpoints.api.bim import list_bim_sheets_in_project
from tektome.endpoints.models.create_retrieve_bim_sheet_request import CreateRetrieveBimSheetRequest

sheets = list_bim_sheets_in_project.sync(
    client=client,
    body=CreateRetrieveBimSheetRequest(
        bim_project_id=bim_project_id,
        page=1,
        page_size=100,
    ),
)
```

### List objects in a specific view

```python
from tektome.endpoints.api.bim import list_bim_objects_in_view
from tektome.endpoints.models.create_retrieve_bim_objects_in_view_request import (
    CreateRetrieveBimObjectsInViewRequest,
)

objects = list_bim_objects_in_view.sync(
    bim_view_id=view_id,
    client=client,
    body=CreateRetrieveBimObjectsInViewRequest(
        page=1,
        page_size=100,
    ),
)
```

---

## Semantic search (KV Embeddings)

Search BIM properties using natural language queries rather than exact key-value matches:

```python
from tektome.endpoints.api.bim import search_kv_embeddings_from_query
from tektome.endpoints.models.bim_query_to_keys_values_request import BimQueryToKeysValuesRequest

result = search_kv_embeddings_from_query.sync(
    bim_project_id=bim_project_id,
    client=client,
    body=BimQueryToKeysValuesRequest(query="structural load-bearing walls"),
    limit=100,
)
```

Returns matching key-value pairs ranked by semantic similarity. Useful for discovering relevant properties when you don't know the exact key names.

---

## BIM task polling

Several BIM operations (IFC conversion, clash detection, reindexing) are async. Poll their status:

```python
from tektome.endpoints.api.bim import get_bim_task

task = get_bim_task.sync(bim_task_id=task_uuid, client=client)
```

| Status | Meaning |
|---|---|
| `PENDING` | Queued, not yet started |
| `PROCESSING` | Currently running |
| `COMPLETED` | Finished successfully |
| `FAILED` | Failed — check error details |

---

## Key rules

| Rule | Detail |
|---|---|
| BIM element IDs are Speckle hashes | 32-char hex strings, not UUIDs. Use the `id` returned by KV search — not Revit element IDs or resource UUIDs |
| Always prefer streaming endpoints | `stream_batch_bim_elements` (50K IDs) over `get_batch_bim_elements` (50 IDs) for anything beyond trivial lookups |
| Coordinates are in millimetres | All spatial queries (topology search) use mm as the unit |
| KV search returns IDs only | You must batch-fetch to get full element data (properties, geometry) |
| NDJSON responses need manual parsing | Streaming endpoints return `Response[Any]` — parse `.content.decode()` line by line as JSON |
| `properties` may be a string | Some elements return `properties` as a JSON string rather than a dict — always check and `json.loads()` if needed |
| `data` may be a string | Same as above — the `data` field in batch responses may need an extra `json.loads()` |
| Validate IDs before citations | The BIM citation API rejects element IDs not found in the project. Always validate with `validate_bim_element_ids` or `stream_bim_elements_by_project(id_only=True)` |
| Stats require generation first | `get_bim_key_value_stats` returns 404 if stats have never been generated. Call `generate_bim_key_value_stats` first |
| Async operations need polling | IFC conversion, clash detection, and reindexing return task IDs — poll with `get_bim_task` |
| KV search max 150K results | If your search exceeds this, narrow the query with more specific key-value patterns |
| `bim_resource_id` in citations ≠ document `resource_id` | When creating BIM citations, `bim_resource_id` is the IFC/BIM file resource UUID, not the PDF or document resource |

---

## Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Using Revit element IDs instead of Speckle hashes | Citation creation fails (400/404) | Use the `id` field from KV search or batch fetch — it's a 32-char hex hash |
| Passing resource UUID as `bim_project_id` | 404 or wrong project | Use `list_bim_projects_by_resource` to resolve the BIM project UUID from a resource |
| Not parsing `properties` as string | `KeyError` when accessing property paths | Check `isinstance(properties, str)` and `json.loads()` if true |
| Using `get_batch_bim_elements` for large ID lists | Request fails or is truncated at 50 IDs | Use `stream_batch_bim_elements` (supports up to 50,000 IDs) |
| Calling `get_bim_key_value_stats` before generation | 404 response | Call `generate_bim_key_value_stats` first, then retrieve |
| Not handling `found: false` in batch responses | Processing non-existent elements | Check `obj.get("found", True)` and skip false entries |
| Skipping ID validation before citation | BIM citation creation fails silently or returns 400 | Validate against project IDs using `validate_bim_element_ids` or `stream_bim_elements_by_project(id_only=True)` |
| Using `sync()` for streaming endpoints | Returns `None` because streaming responses don't parse | Always use `sync_detailed()` and read `.content.decode()` for streaming endpoints |
| Forgetting that topology search uses mm | Search region is too small or too large | Convert to mm: 1 metre = 1000 mm |

---

## Endpoint reference

| Operation | Endpoint function | Method |
|---|---|---|
| Get BIM project for resource | `bim.list_bim_projects_by_resource` | GET |
| Generate KV stats | `bim.generate_bim_key_value_stats` | POST |
| Get KV stats | `bim.get_bim_key_value_stats` | GET |
| KV search (stream IDs) | `bim.stream_bim_element_key_value_search` | POST |
| Boolean expression search | `bim.stream_bim_element_value_expression_search` | POST |
| Semantic KV search | `bim.search_kv_embeddings_from_query` | POST |
| Batch fetch (stream) | `bim.stream_batch_bim_elements` | POST |
| Trimmed batch fetch | `bim.stream_trim_batch_bim_elements` | POST |
| Single element fetch | `bim.get_bim_element` | GET |
| Stream project elements | `bim.stream_bim_elements_by_project` | GET |
| Validate IDs | `bim.validate_bim_element_ids` | POST |
| Topology search (box) | `bim.bim_topology_search_box` | POST |
| Topology search (sphere) | `bim.bim_topology_search_sphere` | POST |
| Topology search (prism) | `bim.bim_topology_search_prism` | POST |
| Clash detection | `bim.bim_clash_check` | POST |
| List views | `bim.list_bim_views_in_project` | POST |
| List sheets | `bim.list_bim_sheets_in_project` | POST |
| Objects in view | `bim.list_bim_objects_in_view` | POST |
| Poll async task | `bim.get_bim_task` | GET |
| IFC to BIM conversion | `bim.convert_ifc_to_bim_elements` | POST |
