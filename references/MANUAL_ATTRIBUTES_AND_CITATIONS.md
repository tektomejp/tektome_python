# Manual Attributes and Citations — Agent Reference

This document explains how to manually create typed attributes on a resource or project, and then attach source citations to them, using the Tektome Python SDK.

---

## Overview

```
declare attribute config → create attribute → get attribute_id → create citation(s)
```

Attributes store typed values (float, string, boolean, etc.) on a resource or project within a dataspace. Citations link an attribute's value back to the source evidence — a PDF page region, an image bounding box, a BIM element, raw text, or another attribute.

**Attribute configs must be declared before writing attribute data.** A config registers the attribute name, type, and (for tables) column schema on the dataspace. Attempting to write an attribute that has no config will fail.

---

## Step 0 — Declare an attribute config

### For resource attributes

```python
from tektome.endpoints.api.dataspace import create_dataspace_resource_attribute_config
from tektome.endpoints.models.dataspace_project_attribute_post_in import DataspaceProjectAttributePostIn
from tektome.endpoints.models.dataspace_project_attribute_post_in_attribute_metadata_type_0 import (
    DataspaceProjectAttributePostInAttributeMetadataType0,
)

# Primitive attribute (float, string, boolean, etc.)
create_dataspace_resource_attribute_config.sync(
    dataspace_id=dataspace_uuid,
    client=client,
    body=DataspaceProjectAttributePostIn(
        attribute_label="wall_thickness",
        attribute_type="float_attributes",
        enabled=True,
    ),
)

# Table attribute — pass column schema in attribute_metadata
metadata = DataspaceProjectAttributePostInAttributeMetadataType0()
metadata.additional_properties = {
    "columns": [
        {"name": "element_id", "type": "string"},
        {"name": "type",       "type": "string"},
        {"name": "thickness",  "type": "float"},
    ]
}
create_dataspace_resource_attribute_config.sync(
    dataspace_id=dataspace_uuid,
    client=client,
    body=DataspaceProjectAttributePostIn(
        attribute_label="bim_objects",
        attribute_type="table_attributes",
        attribute_metadata=metadata,
        enabled=True,
    ),
)
```

### For project attributes

Use `create_dataspace_project_attribute_config` instead — same model, different URL (`/projects/attribute-configs/` vs `/resources/attribute-configs/`).

> **Note:** despite the model being named `DataspaceProjectAttributePostIn`, it is used for both resource and project configs.

---

## Step 1 — Create an attribute

Use `post_general_dataspace_attribute` to create an attribute instance on a resource. This returns `AttributeResponse` with the attribute's `id`, which is required for citation creation.

> **Do not use** `upsert_general_attributes` for this purpose — it returns `204` with no body, so you cannot retrieve the attribute ID.

```python
from tektome.endpoints.api.dataspace import post_general_dataspace_attribute
from tektome.endpoints.models.create_attribute_request import CreateAttributeRequest
from tektome.endpoints.models.attribute_type import AttributeType
from tektome.endpoints.models.post_general_dataspace_attribute_dataspace_entity_type import (
    PostGeneralDataspaceAttributeDataspaceEntityType,
)

attr = post_general_dataspace_attribute.sync(
    dataspace_id=dataspace_uuid,
    attribute_category=PostGeneralDataspaceAttributeDataspaceEntityType.RESOURCE,
    client=client,
    body=CreateAttributeRequest(
        name="wall_thickness",
        value=0.3,
        type_=AttributeType.FLOAT_ATTRIBUTES,
    ),
)

attribute_id = attr.id   # UUID — needed for all citation calls
```

For a project-level attribute, use the same endpoint with `PostGeneralDataspaceAttributeDataspaceEntityType.PROJECT` as `attribute_category`.

### Attribute types

```python
class AttributeType(str, Enum):
    BOOLEAN_ATTRIBUTES       = "boolean_attributes"
    COORDINATE_ATTRIBUTES    = "coordinate_attributes"
    DATETIME_ATTRIBUTES      = "datetime_attributes"
    DATE_ATTRIBUTES          = "date_attributes"
    FLOAT_ATTRIBUTES         = "float_attributes"
    INTEGER_ATTRIBUTES       = "integer_attributes"
    JSON_ATTRIBUTES          = "json_attributes"
    LIST_OBJECT_ATTRIBUTES   = "list_object_attributes"
    MULTI_SELECT_ATTRIBUTES  = "multi_select_attributes"
    POLYGON_ATTRIBUTES       = "polygon_attributes"
    SINGLE_SELECT_ATTRIBUTES = "single_select_attributes"
    STRING_ATTRIBUTES        = "string_attributes"
    TABLE_ATTRIBUTES         = "table_attributes"
    TIME_ATTRIBUTES          = "time_attributes"
```

### `attribute_category` — resource vs project

All citation endpoints require an `attribute_category` parameter indicating whether the attribute belongs to a resource or a project:

```python
from tektome.endpoints.models.create_attribute_bim_citation_dataspace_entity_type import (
    CreateAttributeBimCitationDataspaceEntityType,
)

# For resource attributes:
attribute_category = CreateAttributeBimCitationDataspaceEntityType.RESOURCE

# For project attributes:
attribute_category = CreateAttributeBimCitationDataspaceEntityType.PROJECT
```

Each citation type has its own enum for this (`CreateAttributePdfCitationDataspaceEntityType`, `CreateAttributeImageCitationDataspaceEntityType`, etc.), but they all have the same two values: `RESOURCE` and `PROJECT`.

---

## Table attributes

Table attributes require a config to be declared first (Step 0) with the column schema in `attribute_metadata`. Once the config exists, write data directly via `upsert_dataspace_table_attributes`.

> **Do NOT call `post_general_dataspace_attribute` for table attributes — before or after upsert.** These endpoints operate on different underlying attribute representations. Calling it before the upsert creates a conflicting empty attribute instance. Calling it after (even with `value=[]`) overwrites the populated table with an empty `[]`, destroying your rows. To get the attribute ID for citations, read it from `get_dataspace_project_resource` instead — see "Getting the `attribute_id`" below.

### Write the table data

`upsert_dataspace_table_attributes` replaces the **entire table** in one call. Send a flat list of `TableCellUpdate` objects — one per cell — using `row_index` and `column` to address each cell. This implicitly defines the table's rows and columns.

```python
from tektome.endpoints.api.dataspace import upsert_dataspace_table_attributes
from tektome.endpoints.models.update_dataspace_table_attribute_request import UpdateDataspaceTableAttributeRequest
from tektome.endpoints.models.table_cell_update import TableCellUpdate
from tektome.endpoints.models.upsert_dataspace_table_attributes_dataspace_entity_type import (
    UpsertDataspaceTableAttributesDataspaceEntityType,
)

rows = [
    {"element_id": "wall-001", "type": "IfcWall", "thickness": 0.3},
    {"element_id": "wall-002", "type": "IfcWall", "thickness": 0.25},
    {"element_id": "slab-001", "type": "IfcSlab", "thickness": 0.2},
]

cells = [
    TableCellUpdate(row_index=i, column=col, value=val)
    for i, row in enumerate(rows)
    for col, val in row.items()
]

# Read current version from resource metadata before upserting (see "Version handling" below)
if current_version is not None:
    body = UpdateDataspaceTableAttributeRequest(cells=cells, version=current_version)
else:
    body = UpdateDataspaceTableAttributeRequest(cells=cells)  # UNSET — omits version field

upsert_resp = upsert_dataspace_table_attributes.sync_detailed(
    dataspace_id=dataspace_uuid,
    attribute_category=UpsertDataspaceTableAttributesDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,    # attribute CONFIG ID — from config response or resource metadata
    client=client,
    body=body,
)
if upsert_resp.status_code.value != 204:
    raise RuntimeError(f"upsert_dataspace_table_attributes failed: {upsert_resp.content.decode()}")
```

### Version handling for `upsert_dataspace_table_attributes`

> **Do NOT pass `version=None`.** `None` serializes as `"version": null` in the JSON body, which the server interprets as a version mismatch and returns **409 Table has been modified**.

The `version` field uses `UNSET` semantics (see "UNSET vs None" below):
- **New table (first write):** leave `version` as the default `UNSET` — it is omitted from the request body entirely.
- **Existing table (re-run/update):** read the current version from the resource metadata and pass it explicitly.

```python
from tektome.endpoints.api.dataspace import get_dataspace_project_resource

res_resp = get_dataspace_project_resource.sync_detailed(
    resource_id=resource_uuid, client=client,
)
res_data = json.loads(res_resp.content.decode())

attr_entry = res_data.get("core_attributes_metadata", {}).get(attr_name)
current_version = None
if attr_entry:
    val = attr_entry.get("value")
    if isinstance(val, dict) and "version" in val:
        current_version = val["version"]  # nested at core_attributes_metadata.<name>.value.version

if current_version is not None:
    body = UpdateDataspaceTableAttributeRequest(cells=cells, version=current_version)
else:
    body = UpdateDataspaceTableAttributeRequest(cells=cells)  # UNSET — omitted
```

### Getting the `attribute_id` for a table attribute (needed for citations)

> **Do NOT use `post_general_dataspace_attribute(value=[])` to retrieve the attribute ID.** Even when called *after* `upsert_dataspace_table_attributes`, this call overwrites the populated table with an empty `[]` instance in the database. The table appears empty despite a successful upsert.

After upserting, read the attribute ID back from the resource metadata:

```python
from tektome.endpoints.api.dataspace import get_dataspace_project_resource

res_resp = get_dataspace_project_resource.sync_detailed(
    resource_id=resource_uuid, client=client,
)
res_data = json.loads(res_resp.content.decode())
attribute_id = UUID(res_data["core_attributes_metadata"][attr_name]["id"])
```

The resource response structure is:
```json
{
  "core_attributes_metadata": {
    "<attr_name>": {
      "id": "uuid-string",
      "is_locked": false,
      "citations_count": 0,
      "value": {
        "rows": [...],
        "columns": [...],
        "version": 0
      }
    }
  }
}
```

You can combine the version-read and attribute-ID-read steps: read the resource once **before** the upsert (to get the version), then read it again **after** (to get the attribute ID). Or, if you know the table is new, skip the pre-read and do a single read after.

### Table behaviour

- **Full replace**: every call to `upsert_dataspace_table_attributes` replaces the entire table. To add a row to an existing table, read the current data first, append to it, and send the complete set.
- **Columns must match the config**: column names in `TableCellUpdate` must match the names declared in `attribute_metadata.columns` when the config was created.
- **Sparse cells**: rows that are missing a column get `None` for that column.
- **`version`**: used for optimistic concurrency control. Pass the version number from `core_attributes_metadata.<name>.value.version` when updating an existing table. Leave as `UNSET` (the default) for a first write — do **not** pass `None`, which serializes as `null` and causes a 409.
- **`insert_dataspace_table_attribute_row`**: inserts a blank row at a given `row_index`, shifting existing rows down. Use this when you need to splice a row into the middle of an existing table rather than replacing everything.

### Config idempotency

`create_dataspace_resource_attribute_config` returns **400** (not 409) when the config already exists. When handling re-runs, treat 400 as "already exists". When the config already exists and you cannot read the `attribute_name` from the response, derive it: the server-generated `attribute_name` is the label lowercased with spaces and hyphens replaced by underscores (e.g. `"Non-AKT Foundations Table"` → `"non_akt_foundations_table"`).

```python
config_resp = create_dataspace_resource_attribute_config.sync_detailed(...)
if config_resp.status_code.value == 201:
    attr_name = config_resp.parsed.attribute_name
elif config_resp.status_code.value == 400:
    attr_name = attr_label.lower().replace(" ", "_").replace("-", "_")
else:
    raise RuntimeError(f"Config failed: {config_resp.content.decode()}")
```

### UNSET vs None

Throughout the Tektome SDK, `UNSET` (from `tektome.endpoints.types`) means "omit this field from the request body entirely". `None` means "include as `null`". The server treats these differently:
- `version=UNSET` (the default) → field absent from JSON → no concurrency check
- `version=None` → `"version": null` in JSON → server sees a version mismatch → **409**
- `version=0` → `"version": 0` → server validates against stored version → **409 if stale**

When in doubt, leave optional fields as their default `UNSET` rather than explicitly passing `None`.

### Column types in `attribute_metadata`

The `columns` list in `attribute_metadata` uses plain string type names (not `AttributeType` enum values):

```python
{"name": "start_date", "type": "date"}
{"name": "element_id", "type": "string"}
{"name": "thickness",  "type": "float"}
{"name": "count",      "type": "integer"}
{"name": "is_active",  "type": "boolean"}
```

---

## Step 2 — Create a BIM citation

Links the attribute to one or more BIM elements (project/object pairs).

> **`bim_resource_id` is the BIM resource (IFC file), not the resource the attribute belongs to.** These are always different UUIDs. A common mistake is passing the document/PDF resource ID here — this will cause the server to reject the citation (400/404). Always pass a dedicated `bim_resource_id` parameter; never reuse `resource_id`.

> **Always use `sync_detailed` for citations and check the status code.** The `sync()` shortcut silently returns `ErrorOut` on failure without raising — errors are invisible unless you inspect the response. A script can increment a `citations_created` counter and return apparent success while every citation has actually failed.

```python
from tektome.endpoints.api.dataspace_attributes_citations import create_attribute_bim_citation
from tektome.endpoints.models.create_bim_citation_request import CreateBIMCitationRequest
from tektome.endpoints.models.bim_element_request import BIMElementRequest
from tektome.endpoints.models.create_attribute_bim_citation_dataspace_entity_type import (
    CreateAttributeBimCitationDataspaceEntityType,
)

resp = create_attribute_bim_citation.sync_detailed(
    dataspace_id=dataspace_uuid,
    attribute_category=CreateAttributeBimCitationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,
    client=client,
    body=CreateBIMCitationRequest(
        title="Walls from structural IFC",
        attribute_type=AttributeType.FLOAT_ATTRIBUTES,   # must match the attribute's type
        bim_resource_id=bim_resource_uuid,               # the BIM resource (IFC) — NOT the document resource
        bim_elements=[                                   # required — at least one element
            BIMElementRequest(
                bim_project_id=bim_project_uuid,
                bim_element_id="element-123",             # optional: omit to cite the whole project
            ),
            BIMElementRequest(
                bim_project_id=bim_project_uuid,
                bim_element_id="element-456",
            ),
        ],
        keywords=["structural", "wall"],                 # optional
    ),
)
if resp.status_code.value != 201:
    raise RuntimeError(f"Citation failed: {resp.status_code.value} {resp.content.decode()}")
```

---

### Upserting a BIM citation (create or update)

Only one BIM citation is allowed per resource-attribute pair. To handle re-runs gracefully, POST first and PATCH if already exists:

```python
from tektome.endpoints.api.dataspace_attributes_citations import (
    create_attribute_bim_citation,
    update_attribute_bim_citation,
    get_attribute_citations,
)
from tektome.endpoints.models.update_bim_citation_request import UpdateBIMCitationRequest
from tektome.endpoints.models.update_attribute_bim_citation_dataspace_entity_type import (
    UpdateAttributeBimCitationDataspaceEntityType,
)
from tektome.endpoints.models.get_attribute_citations_dataspace_entity_type import (
    GetAttributeCitationsDataspaceEntityType,
)

bim_elements = [
    BIMElementRequest(
        bim_project_id=bim_project_uuid,
        bim_element_id=eid,  # 32-char Speckle hash (the `id` from KV search) — NOT UUID, NOT Revit Tag
    )
    for eid in element_ids
]

resp = create_attribute_bim_citation.sync_detailed(
    dataspace_id=dataspace_uuid,
    attribute_category=CreateAttributeBimCitationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,
    client=client,
    body=CreateBIMCitationRequest(
        title="My citation",           # max 32 characters
        attribute_type=AttributeType.INTEGER_ATTRIBUTES,
        bim_resource_id=bim_resource_uuid,
        bim_elements=bim_elements,
    ),
)

if resp.status_code.value == 201:
    pass  # created
elif resp.status_code.value == 400 and "already cited" in resp.content.decode().lower():
    # Find the existing citation ID then PATCH it
    # get_attribute_citations returns a mixed PagedCitations list — all citation types
    # (BIM, PDF, image, attribute-to-attribute) are interleaved. Filter by citation_type == "bim"
    # to find the BIM citation. Note: the POST response uses citation_type="bim_citation" (schema
    # field), but the list response uses the shorter "bim" value.
    list_resp = get_attribute_citations.sync_detailed(
        dataspace_id=dataspace_uuid,
        attribute_category=GetAttributeCitationsDataspaceEntityType.RESOURCE,
        attribute_id=attribute_id,
        client=client,
        page_size=100,
    )
    citations_data = json.loads(list_resp.content.decode())
    bim_citation_id = next(
        UUID(c["id"]) for c in citations_data.get("items", []) if c.get("citation_type") == "bim"
    )
    update_attribute_bim_citation.sync_detailed(
        dataspace_id=dataspace_uuid,
        attribute_category=UpdateAttributeBimCitationDataspaceEntityType.RESOURCE,
        attribute_id=attribute_id,
        bim_citation_id=bim_citation_id,
        client=client,
        body=UpdateBIMCitationRequest(bim_elements=bim_elements),
    )
```

All elements go in a **single citation** — do not batch across multiple POST calls.

---

## Step 2 (alternative) — Create a PDF citation

Links the attribute to a region of a PDF resource, optionally with polygon annotations.

```python
from tektome.endpoints.api.dataspace_attributes_citations import create_attribute_pdf_citation
from tektome.endpoints.models.create_pdf_citation_request import CreatePDFCitationRequest
from tektome.endpoints.models.create_attribute_pdf_citation_dataspace_entity_type import (
    CreateAttributePdfCitationDataspaceEntityType,
)

create_attribute_pdf_citation.sync(
    dataspace_id=dataspace_uuid,
    attribute_category=CreateAttributePdfCitationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,
    client=client,
    body=CreatePDFCitationRequest(
        title="Section 4.2 of specification",
        attribute_type=AttributeType.FLOAT_ATTRIBUTES,
        resource_id=pdf_resource_uuid,   # the PDF resource
        polygons=[...],                  # optional: list[PDFPolygonSchemaRequest] page regions
        keywords=["thickness"],          # optional
    ),
)
```

---

## Step 2 (alternative) — Create an image citation

Links the attribute to a polygon region within an image resource. `bounding_geometry` is required (unlike PDF polygons which are optional).

```python
from tektome.endpoints.api.dataspace_attributes_citations import create_attribute_image_citation
from tektome.endpoints.models.create_image_citation_request import CreateImageCitationRequest
from tektome.endpoints.models.create_attribute_image_citation_dataspace_entity_type import (
    CreateAttributeImageCitationDataspaceEntityType,
)

create_attribute_image_citation.sync(
    dataspace_id=dataspace_uuid,
    attribute_category=CreateAttributeImageCitationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,
    client=client,
    body=CreateImageCitationRequest(
        title="Floor plan detail",
        attribute_type=AttributeType.FLOAT_ATTRIBUTES,
        image_resource_id=image_resource_uuid,
        bounding_geometry=[                # required: list[list[list[float]]] — polygon coords
            [[100.0, 200.0], [300.0, 200.0], [300.0, 400.0], [100.0, 400.0]]
        ],
        keywords=["plan"],                 # optional
    ),
)
```

---

## Step 2 (alternative) — Create an attribute-to-attribute citation

Links one attribute's value to another attribute as its source (e.g. a derived or aggregated value).

```python
from tektome.endpoints.api.dataspace_attributes_citations import create_attribute_attribute_citation
from tektome.endpoints.models.create_attribute_citation_request import CreateAttributeCitationRequest
from tektome.endpoints.models.create_attribute_attribute_citation_dataspace_entity_type import (
    CreateAttributeAttributeCitationDataspaceEntityType,
)

create_attribute_attribute_citation.sync(
    dataspace_id=dataspace_uuid,
    attribute_category=CreateAttributeAttributeCitationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,             # the attribute being cited
    client=client,
    body=CreateAttributeCitationRequest(
        title="Derived from area calculation",
        attribute_type=AttributeType.FLOAT_ATTRIBUTES,        # type of the citing attribute
        cited_attribute_type=AttributeType.FLOAT_ATTRIBUTES,  # type of the source attribute
        cited_attribute_id=source_attribute_uuid,             # UUID of the source attribute
    ),
)
```

---

## Key rules

| Rule | Detail |
|---|---|
| Declare config before writing | Both primitive and table attributes require a config registered on the dataspace first |
| Table config needs column schema | Pass `attribute_metadata` with a `columns` list when declaring a table config |
| `attribute_type` in config is a plain string | Use `"float_attributes"`, `"table_attributes"` etc. — not the `AttributeType` enum |
| Use `post_general_dataspace_attribute` to get `attribute_id` | Returns `AttributeResponse` with `id` — needed for citations |
| `attribute_type` in citation body | Must match the type of the attribute you're citing |
| `attribute_category` | `RESOURCE` or `PROJECT` — matches where the attribute lives |
| `dataspace_id` required | All citation endpoints operate within a dataspace context |
| BIM `bim_elements` is required | Must include at least one `BIMElementRequest`; `bim_element_id` is optional (omit to cite the whole project) |
| `bim_element_id` is the 32-char Speckle hash | Not the UUID, not the Revit Tag — use the `id` returned by the KV search endpoint |
| Citation `title` max 32 characters | The database column is `varchar(32)` — longer titles cause a 400 error |
| One BIM citation per resource-attribute pair | POSTing a second citation returns 400 "already cited" — use PATCH to update the existing one |
| Image `bounding_geometry` is required | Must always be provided for image citations |
| PDF `polygons` is optional | Can be omitted if you only need to cite the resource without a specific region |
| Citations attach to the attribute, not individual rows | For table attributes, all citations link to the table attribute UUID as a whole |
| Get table `attribute_id` from resource metadata | After `upsert_dataspace_table_attributes`, read `get_dataspace_project_resource` → `core_attributes_metadata.<name>.id` — never use `post_general_dataspace_attribute` for this |
| `version` for tables: `UNSET` for new, integer for updates | `version=None` serializes as `null` → 409. Read from `core_attributes_metadata.<name>.value.version` |

---

## Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Calling `post_general_dataspace_attribute(value=[])` for a table at all — before or after upsert | Table attribute value reads back as `[]`; citations reference empty attribute | Never call `post_general_dataspace_attribute` for table attributes. Get the attribute ID from `get_dataspace_project_resource` → `core_attributes_metadata.<name>.id` |
| Passing `version=None` to `upsert_dataspace_table_attributes` | Server returns **409 Table has been modified** | Leave `version` as `UNSET` (default) for a new table; pass the integer version for updates |
| Passing the document `resource_id` as `bim_resource_id` in a BIM citation | Server returns 400/404; no citations created | `bim_resource_id` must be the BIM resource (IFC file) UUID — always a separate parameter |
| Using `sync()` instead of `sync_detailed()` for citations | Script reports success but no citations exist | Use `sync_detailed()` and check `resp.status_code.value == 201` |
| Using `attribute_label` instead of `attribute_name` as the attribute `name` | `upsert_dataspace_table_attributes` or `post_general_dataspace_attribute` fails or targets wrong attribute | The config returns both; use `attribute_name` (the server-generated key) not `attribute_label` (the human label) |
| Using `AttributeType` enum values in config `attribute_type` | Config creation fails | Use plain strings: `"table_attributes"`, `"float_attributes"`, etc. |

---

## Reasoning

Reasoning (the LLM's explanation of why an attribute has its value) is **read-only** — it is set exclusively by the extraction pipeline and cannot be written manually. There is no endpoint to set or update it.
