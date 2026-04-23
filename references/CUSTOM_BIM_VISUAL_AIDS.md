# Custom BIM Visual Aids — Agent Reference

This document explains how to create custom BIM geometry objects (lines, meshes, text labels) and attach them to citations as visual aids. These "floating" objects appear in the 3D viewer alongside the real BIM model, helping users understand derived or computed results — escape routes, measurement lines, highlight zones, labels, etc.

---

## Overview

```
1. Get a Speckle template (mesh, line, or text)
2. Modify the template JSON (position, geometry, colour, material)
3. Upload via create_bim_object_from_json → get content-hashed object ID
4. Attach to a BIM citation as a bim_annotation
```

Custom BIM objects are **standalone** — they are not part of any BIM project. They exist independently and are referenced by their content-hashed ID. When attached to a citation via `bim_annotations`, the viewer renders them alongside the cited BIM elements, giving the user a visual overlay that explains the agent's analysis.

### Use cases

- **Escape routes** — draw line segments tracing the shortest path from a room to an exit
- **Measurement indicators** — place a line between two points with a text label showing the distance
- **Highlight zones** — create a semi-transparent mesh marking an area of concern (fire risk, structural weakness)
- **Labels and callouts** — place floating text at specific 3D coordinates to annotate elements
- **Clash indicators** — draw a mesh or marker at the location of a detected clash between elements

---

## Step 1 — Get a Speckle template

The template endpoint returns a Speckle-compatible JSON object for one of three geometry types. The returned JSON has all required fields pre-populated with example values — modify the values to create your custom geometry.

```python
from tektome.endpoints.api.bim import get_bim_speckle_template

resp = get_bim_speckle_template.sync_detailed(
    object_type="line",   # "mesh", "line", or "text"
    client=client,
)
template = resp.parsed.to_dict()  # plain dict — modify and re-serialize
```

The response is a `GetBimSpeckleTemplateResponse` whose actual data lives in `additional_properties`. Calling `.to_dict()` gives you the full Speckle JSON as a Python dict.

### Available geometry types

| Type | `speckle_type` | Default template | Best for |
|---|---|---|---|
| `"mesh"` | `Objects.Geometry.Mesh` | 1000 mm cube at origin | Highlight zones, markers, custom 3D shapes |
| `"line"` | `Objects.Geometry.Line` | Line from origin to (5000, 5000, 0) mm | Routes, measurements, connections |
| `"text"` | `Objects.Other.Text` | "hello, world" at origin | Labels, callouts, distance annotations |

---

## Step 2 — Modify the template

### Colour convention — signed 32-bit ARGB

All colours in Speckle JSON are **signed 32-bit ARGB integers**: `(A << 24) | (R << 16) | (G << 8) | B`. Values >= `0x80000000` wrap negative in Python (signed int32).

```python
import struct

def argb_color(a: int, r: int, g: int, b: int) -> int:
    """Convert ARGB channels (0-255 each) to a signed 32-bit integer."""
    unsigned = (a << 24) | (r << 16) | (g << 8) | b
    return struct.unpack("i", struct.pack("I", unsigned))[0]

RED_OPAQUE = argb_color(255, 255, 0, 0)       # -65536
GREEN_SEMI = argb_color(128, 0, 255, 0)       # semi-transparent green
BLUE_OPAQUE = argb_color(255, 0, 0, 255)      # -16776961
BLACK = argb_color(255, 0, 0, 0)              # -16777216
```

### Material priority by geometry type

| Geometry | 1st choice | 2nd choice | 3rd choice |
|---|---|---|---|
| mesh | vertex `colors` | `renderMaterial` | `displayStyle` |
| line | `displayStyle` | `renderMaterial` | — |
| text | `displayStyle` | — | — |

When a mesh has **both** `colors` and `renderMaterial`, vertex colours replace the diffuse colour in the shader while PBR properties (opacity, roughness, metalness) still come from `renderMaterial`. To use only PBR material colour, set `colors` to `[]`.

---

### Line geometry

A line segment between two 3D points. Each point has `x`, `y`, `z` floats and its own `units` field.

```python
import copy

template = resp.parsed.to_dict()
line = copy.deepcopy(template)

line["start"]["x"] = 1000.0
line["start"]["y"] = 2000.0
line["start"]["z"] = 0.0
line["start"]["units"] = "mm"

line["end"]["x"] = 5000.0
line["end"]["y"] = 8000.0
line["end"]["z"] = 0.0
line["end"]["units"] = "mm"

line["displayStyle"]["diffuse"] = RED_OPAQUE
line["displayStyle"]["lineweight"] = 5.0
line["displayStyle"]["units"] = "mm"

line["units"] = "mm"
line["name"] = "Escape route segment 1"
```

**Fields:**

| Field | Type | Description |
|---|---|---|
| `start` | object | `{x, y, z, units}` — start point |
| `end` | object | `{x, y, z, units}` — end point |
| `displayStyle.diffuse` | int | Stroke colour (signed 32-bit ARGB) |
| `displayStyle.lineweight` | float | Stroke width in `displayStyle.units` |
| `displayStyle.units` | str | Unit for lineweight |
| `units` | str | Coordinate unit system (`mm`, `m`, `cm`, `ft`, `in`) |
| `name` | str | Optional display name in object inspector |
| `id` | str | Unique ID (will be recalculated on upload) |
| `speckle_type` | str | Must be `Objects.Geometry.Line` |

---

### Mesh geometry

A triangulated mesh defined by flat vertex and face arrays, with optional per-vertex colours and PBR material.

```python
template = resp.parsed.to_dict()
mesh = copy.deepcopy(template)

# A simple triangle
mesh["vertices"] = [
    0.0, 0.0, 0.0,       # vertex 0
    1000.0, 0.0, 0.0,    # vertex 1
    500.0, 1000.0, 0.0,  # vertex 2
]
mesh["faces"] = [3, 0, 1, 2]  # one triangle: 3 vertices, indices 0, 1, 2

# Use renderMaterial for uniform colour (clear vertex colors)
mesh["colors"] = []
mesh["renderMaterial"]["diffuse"] = RED_OPAQUE
mesh["renderMaterial"]["opacity"] = 0.5       # semi-transparent
mesh["renderMaterial"]["roughness"] = 1.0     # matte
mesh["renderMaterial"]["metalness"] = 0.0     # dielectric
mesh["renderMaterial"]["emissive"] = BLACK
mesh["renderMaterial"]["name"] = "Highlight zone"
mesh["renderMaterial"]["speckle_type"] = "Objects.Other.RenderMaterial"

mesh["units"] = "mm"
mesh["name"] = "Fire risk zone"
```

**Geometry fields:**

| Field | Type | Description |
|---|---|---|
| `vertices` | `list[float]` | Flat `[x0,y0,z0, x1,y1,z1, ...]` — every 3 floats is one vertex position |
| `faces` | `list[int]` | Run-length encoded triangles: each face starts with vertex count (`3`), then that many indices into `vertices` |
| `colors` | `list[int]` | One signed 32-bit ARGB int per vertex. Length must be `len(vertices) // 3`. Set to `[]` to use only `renderMaterial` |

**renderMaterial fields:**

| Field | Type | Description |
|---|---|---|
| `renderMaterial.diffuse` | int | Surface colour (signed 32-bit ARGB) |
| `renderMaterial.emissive` | int | Emissive colour (usually black = `−16777216`) |
| `renderMaterial.opacity` | float | `0.0`–`1.0` (1 = opaque, 0.25 = glass-like) |
| `renderMaterial.roughness` | float | `0.0`–`1.0` (1 = matte, 0 = mirror) |
| `renderMaterial.metalness` | float | `0.0`–`1.0` (0 = dielectric, 1 = metal) |
| `renderMaterial.name` | str | Human-readable material label |
| `renderMaterial.speckle_type` | str | Must be `Objects.Other.RenderMaterial` |

---

### Text geometry

SDF text rendered by the viewer's built-in troika-three-text engine. No mesh geometry needed.

```python
template = resp.parsed.to_dict()
text = copy.deepcopy(template)

text["value"] = "Distance: 4.2m"
text["height"] = 500.0           # font size in world units (mm)
text["maxWidth"] = 5000.0        # line-wrap width
text["alignmentH"] = 1           # 0=left, 1=centre, 2=right
text["alignmentV"] = 1           # 0=top, 1=middle, 2=bottom
text["screenOriented"] = True    # billboard mode — always faces camera

# Position via plane.origin
text["plane"]["origin"]["x"] = 3000.0
text["plane"]["origin"]["y"] = 5000.0
text["plane"]["origin"]["z"] = 1000.0

text["displayStyle"]["diffuse"] = BLACK
text["displayStyle"]["lineweight"] = 0   # required but not applicable to text
text["displayStyle"]["units"] = "mm"

text["units"] = "mm"
text["name"] = "Distance label"
```

**Text fields:**

| Field | Type | Description |
|---|---|---|
| `value` | str | The text string to display |
| `height` | float | Font size in world units |
| `maxWidth` | float | Line-wrapping width in world units |
| `alignmentH` | int | Horizontal: `0`=left, `1`=centre, `2`=right |
| `alignmentV` | int | Vertical: `0`=top, `1`=middle, `2`=bottom |
| `screenOriented` | bool | `true` = billboard (faces camera); `false` = fixed in world space |
| `plane.origin` | object | `{x, y, z}` — position of the text |
| `plane.xdir` | object | `{x, y, z}` — unit vector for horizontal axis |
| `plane.ydir` | object | `{x, y, z}` — unit vector for vertical axis |
| `plane.normal` | object | `{x, y, z}` — perpendicular to text plane (xdir × ydir) |

When `screenOriented=true`, the `plane` only determines position (via `origin`); orientation is ignored since the text always faces the camera. When `screenOriented=false`, the full plane orientation controls how the text is rendered in world space.

---

## Step 3 — Upload the custom object

Serialize the modified template to a JSON file and upload it via `create_bim_object_from_json`. The server recalculates the object ID from the JSON content using the Speckle hashing algorithm (SHA-256 truncated to 32 hex characters), so the ID is a deterministic content hash.

```python
import json
import io
from tektome.endpoints.api.bim import create_bim_object_from_json
from tektome.endpoints.models.create_bim_object_from_json_file_params import (
    CreateBimObjectFromJsonFileParams,
)
from tektome.endpoints.types import File

json_bytes = json.dumps(line).encode("utf-8")

upload_resp = create_bim_object_from_json.sync_detailed(
    client=client,
    body=CreateBimObjectFromJsonFileParams(
        file=File(
            payload=io.BytesIO(json_bytes),
            file_name="escape_route_segment.json",
        ),
    ),
)
if upload_resp.status_code.value != 201:
    raise RuntimeError(
        f"BIM object upload failed: {upload_resp.status_code.value} "
        f"{upload_resp.content.decode()}"
    )

object_id = upload_resp.parsed.id  # 32-char hex string (content hash)
```

The response is a `BimObjectFromJsonResponse` with:
- `id` — the content-derived Speckle ID (32 hex characters)
- `message` — human-readable confirmation

**The returned `id` is what you pass as `bim_object_id` in the citation's `bim_annotations` list.**

### Uploading multiple objects

Each call to `create_bim_object_from_json` uploads one object. For a multi-segment route, upload each segment separately and collect the IDs:

```python
annotation_ids = []
for i, segment in enumerate(route_segments):
    json_bytes = json.dumps(segment).encode("utf-8")
    resp = create_bim_object_from_json.sync_detailed(
        client=client,
        body=CreateBimObjectFromJsonFileParams(
            file=File(
                payload=io.BytesIO(json_bytes),
                file_name=f"route_segment_{i}.json",
            ),
        ),
    )
    if resp.status_code.value != 201:
        raise RuntimeError(f"Upload failed for segment {i}: {resp.content.decode()}")
    annotation_ids.append(resp.parsed.id)
```

---

## Step 4 — Attach to a BIM citation

Custom objects are attached to a BIM citation via the `bim_annotations` field on `CreateBIMCitationRequest`. Each annotation references a standalone BIM object by its `bim_object_id` (the 32-char content hash from Step 3).

The citation also requires `bim_elements` (at least one `BIMElementRequest` referencing a real BIM project/element pair) and `bim_resource_id` (the BIM resource UUID). The annotations overlay on top of the cited BIM context.

```python
from tektome.endpoints.api.dataspace_attributes_citations import create_attribute_bim_citation
from tektome.endpoints.models.create_bim_citation_request import CreateBIMCitationRequest
from tektome.endpoints.models.bim_element_request import BIMElementRequest
from tektome.endpoints.models.bim_annotation_request import BIMAnnotationRequest
from tektome.endpoints.models.attribute_type import AttributeType
from tektome.endpoints.models.create_attribute_bim_citation_dataspace_entity_type import (
    CreateAttributeBimCitationDataspaceEntityType,
)

citation_resp = create_attribute_bim_citation.sync_detailed(
    dataspace_id=dataspace_uuid,
    attribute_category=CreateAttributeBimCitationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,
    client=client,
    body=CreateBIMCitationRequest(
        title="Shortest escape route",
        attribute_type=AttributeType.STRING_ATTRIBUTES,
        bim_resource_id=bim_resource_uuid,
        bim_elements=[
            BIMElementRequest(
                bim_project_id=bim_project_uuid,
                bim_element_id="abc123...",         # optional: specific element
            ),
        ],
        bim_annotations=[
            BIMAnnotationRequest(bim_object_id=oid)
            for oid in annotation_ids               # from Step 3
        ],
        keywords=["escape", "route"],
    ),
)
if citation_resp.status_code.value != 201:
    raise RuntimeError(
        f"BIM citation failed: {citation_resp.status_code.value} "
        f"{citation_resp.content.decode()}"
    )
```

### BIMAnnotationRequest

| Field | Type | Description |
|---|---|---|
| `bim_object_id` | `str` | The 32-char content-hashed ID returned by `create_bim_object_from_json` |

### BIMElementRequest

| Field | Type | Description |
|---|---|---|
| `bim_project_id` | `UUID` | The BIM project containing the cited element |
| `bim_element_id` | `None \| str \| Unset` | Optional: the 32-char Speckle hash of a specific element. Leave as `UNSET` (default) to cite the whole project |
| `highlight_color` | `None \| str \| Unset` | Optional: highlight colour for the element in the viewer. Leave as `UNSET` (default) to omit |

---

## Complete example — Escape route visualisation

This example shows the full workflow: creating line segments for an escape route, a text label for the distance, and attaching them to a citation.

```python
import copy
import io
import json
import struct
from tektome.endpoints.api.bim import get_bim_speckle_template, create_bim_object_from_json
from tektome.endpoints.api.dataspace_attributes_citations import create_attribute_bim_citation
from tektome.endpoints.models.create_bim_object_from_json_file_params import (
    CreateBimObjectFromJsonFileParams,
)
from tektome.endpoints.models.create_bim_citation_request import CreateBIMCitationRequest
from tektome.endpoints.models.bim_element_request import BIMElementRequest
from tektome.endpoints.models.bim_annotation_request import BIMAnnotationRequest
from tektome.endpoints.models.attribute_type import AttributeType
from tektome.endpoints.models.create_attribute_bim_citation_dataspace_entity_type import (
    CreateAttributeBimCitationDataspaceEntityType,
)
from tektome.endpoints.types import File


def argb_color(a: int, r: int, g: int, b: int) -> int:
    unsigned = (a << 24) | (r << 16) | (g << 8) | b
    return struct.unpack("i", struct.pack("I", unsigned))[0]


RED = argb_color(255, 255, 0, 0)
BLACK = argb_color(255, 0, 0, 0)

# --- 1. Get templates ---
line_template = get_bim_speckle_template.sync_detailed(
    object_type="line", client=client,
).parsed.to_dict()

text_template = get_bim_speckle_template.sync_detailed(
    object_type="text", client=client,
).parsed.to_dict()

# --- 2. Build route segments ---
waypoints = [
    (1000.0, 2000.0, 0.0),
    (3000.0, 2000.0, 0.0),
    (3000.0, 5000.0, 0.0),
    (5000.0, 5000.0, 0.0),  # exit
]

segments = []
for i in range(len(waypoints) - 1):
    seg = copy.deepcopy(line_template)
    seg["start"]["x"], seg["start"]["y"], seg["start"]["z"] = waypoints[i]
    seg["start"]["units"] = "mm"
    seg["end"]["x"], seg["end"]["y"], seg["end"]["z"] = waypoints[i + 1]
    seg["end"]["units"] = "mm"
    seg["displayStyle"]["diffuse"] = RED
    seg["displayStyle"]["lineweight"] = 5.0
    seg["displayStyle"]["units"] = "mm"
    seg["units"] = "mm"
    seg["name"] = f"Escape route segment {i + 1}"
    segments.append(seg)

# --- 3. Build distance label ---
label = copy.deepcopy(text_template)
midpoint = waypoints[len(waypoints) // 2]
label["value"] = "Route: 7.0m"
label["height"] = 300.0
label["maxWidth"] = 3000.0
label["alignmentH"] = 1
label["alignmentV"] = 2
label["screenOriented"] = True
label["plane"]["origin"]["x"] = midpoint[0]
label["plane"]["origin"]["y"] = midpoint[1]
label["plane"]["origin"]["z"] = midpoint[2] + 500.0  # slightly above route
label["displayStyle"]["diffuse"] = BLACK
label["displayStyle"]["lineweight"] = 0
label["displayStyle"]["units"] = "mm"
label["units"] = "mm"
label["name"] = "Route distance"

# --- 4. Upload all objects ---
all_objects = segments + [label]
annotation_ids = []

for i, obj in enumerate(all_objects):
    json_bytes = json.dumps(obj).encode("utf-8")
    resp = create_bim_object_from_json.sync_detailed(
        client=client,
        body=CreateBimObjectFromJsonFileParams(
            file=File(payload=io.BytesIO(json_bytes), file_name=f"visual_aid_{i}.json"),
        ),
    )
    if resp.status_code.value != 201:
        raise RuntimeError(f"Upload {i} failed: {resp.content.decode()}")
    annotation_ids.append(resp.parsed.id)

# --- 5. Attach to citation ---
citation_resp = create_attribute_bim_citation.sync_detailed(
    dataspace_id=dataspace_uuid,
    attribute_category=CreateAttributeBimCitationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,
    client=client,
    body=CreateBIMCitationRequest(
        title="Shortest escape route",
        attribute_type=AttributeType.STRING_ATTRIBUTES,
        bim_resource_id=bim_resource_uuid,
        bim_elements=[
            BIMElementRequest(bim_project_id=bim_project_uuid),
        ],
        bim_annotations=[
            BIMAnnotationRequest(bim_object_id=oid)
            for oid in annotation_ids
        ],
        keywords=["escape", "route", "egress"],
    ),
)
if citation_resp.status_code.value != 201:
    raise RuntimeError(f"Citation failed: {citation_resp.content.decode()}")
```

---

## Key rules

| Rule | Detail |
|---|---|
| Three geometry types available | `mesh`, `line`, `text` — passed as `object_type` to `get_bim_speckle_template` |
| Colours are signed 32-bit ARGB | `(A<<24)\|(R<<16)\|(G<<8)\|B` — use `struct.unpack("i", struct.pack("I", val))` to handle the sign |
| Object IDs are content hashes | `create_bim_object_from_json` recalculates all `id` fields using SHA-256 truncated to 32 hex chars. The `id` you set in the template JSON is overwritten |
| Objects are standalone | Created objects are not attached to any BIM project — they exist independently |
| Upload one object per call | `create_bim_object_from_json` accepts a single JSON file. For multiple objects, call it once per object |
| `bim_annotations` is optional on the citation | If you have no custom visual aids, omit it. The citation still works with just `bim_elements` |
| `bim_elements` is required on the citation | At least one `BIMElementRequest` must be provided, even when the main purpose is to show annotations |
| Citation `title` max 32 characters | The database column is `varchar(32)` — longer titles cause 400 errors |
| `file_name` is informational | The name passed to `File(file_name=...)` is for debugging/logging only — it does not affect the stored object |
| Template `.to_dict()` returns the full JSON | `GetBimSpeckleTemplateResponse` stores all data in `additional_properties`; `.to_dict()` unpacks it |
| Coordinates use the `units` field | The viewer multiplies all coordinates by the conversion factor for the declared unit. Use the same unit system as the existing BIM model |
| `deepcopy` the template for each object | Templates are dicts — modifying in place affects all references. Always `copy.deepcopy()` before editing |
| Use `sync_detailed` for uploads and citations | `sync()` silently returns error objects without raising — always check status codes |

---

## Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Modifying the template dict in place for multiple objects | All objects have the same geometry (the last one edited) | Use `copy.deepcopy(template)` for each object |
| Passing unsigned colour integers | Colours render incorrectly or cause errors | Use `struct.unpack("i", struct.pack("I", unsigned))` to get the signed 32-bit value |
| Setting `colors` on a mesh when you want uniform `renderMaterial` colour | Per-vertex colours override `renderMaterial.diffuse` | Set `colors` to `[]` to use only `renderMaterial` |
| Wrong `colors` array length on mesh | Rendering artefacts or errors | Must have exactly `len(vertices) // 3` entries (one per vertex) |
| Forgetting to set `units` on nested point objects | Points render at wrong scale or position | Set `units` on `start`, `end`, and `plane.origin` — not just the top-level `units` |
| Using `create_bim_element` instead of `create_bim_object_from_json` | `create_bim_element` requires a `bim_project_id` and is for uploading elements into an existing BIM project | Use `create_bim_object_from_json` for standalone annotation objects |
| Passing a UUID as `bim_object_id` in `BIMAnnotationRequest` | 400 error — the ID must be a 32-char Speckle hash | Use the `id` string returned by `create_bim_object_from_json`, not a UUID |
| Omitting `bim_elements` from the citation | Validation error — `bim_elements` is required | Always provide at least one `BIMElementRequest`, even if the visual aids are the main content |
| Exceeding 32-char citation title | 400 error | Keep titles under 32 characters |
| Confusing `bim_resource_id` with the document resource ID | 400/404 — wrong resource type | `bim_resource_id` must be the UUID of the BIM resource (IFC file), not the PDF or document resource |

---

## Endpoint reference

| Operation | Endpoint function | Method |
|---|---|---|
| Get Speckle template | `bim.get_bim_speckle_template` | GET |
| Create standalone BIM object | `bim.create_bim_object_from_json` | POST |
| Create BIM citation (with annotations) | `dataspace_attributes_citations.create_attribute_bim_citation` | POST |
| Upload elements to BIM project | `bim.create_bim_element` | POST |
