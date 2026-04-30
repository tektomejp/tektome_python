# Manual Attributes and Citations — Agent Reference

This document explains how to manually create typed attributes on a resource or project, and then attach source citations to them, using the Tektome Python SDK.

---

## Overview

```
Primitive attributes:
  Step 0: declare config → Step 1: create attribute → get attribute_id → Step 2: create citation(s) → Step 3: submit approval ticket

Table attributes:
  Step 0: declare config → Step 1b: create empty table instance → Step 1c: upsert cells → get attribute_id → Step 2: create citation(s) → Step 3: submit approval ticket
```

Attributes store typed values (float, string, boolean, etc.) on a resource or project within a dataspace. Citations link an attribute's value back to the source evidence — a PDF page region, an image bounding box, a BIM element, raw text, or another attribute.

**Attribute configs must be declared before writing attribute data.** A config registers the attribute name, type, and (for tables) column schema on the dataspace. Attempting to write an attribute that has no config will fail.

### Approval tickets, not direct completion

Agents running inside a Tektome process execution **must not** finalise attributes themselves by setting `extraction_status="completed"`. Instead, create attributes and citations in their default `pending_approval` state, then submit an **approval ticket** referencing those candidates so a human can review and approve the work. Approval is what promotes `pending_approval` → `completed` and links the attribute to its resource/project.

Consequences of this approach:

- While the ticket is `pending`, the attribute is **not** exposed via `core_attributes_metadata` on the resource response, and `get_dataspace_project_resource` will not surface it. This is expected.
- Pending candidates are still discoverable — use the approval-ticket endpoints (`get_execution_approvals`, `get_approval_ticket_details`, `get_approval_candidates`) to list and inspect them.
- Do not pass `extraction_status=AttributeExtractionStatusChoices.COMPLETED` from an agent. Leave the field at its default so the attribute is created as `pending_approval` and flows through the approval pipeline.

### Flow types and pre-created attributes

When a process execution uses `system_flow_type` of `resource_attr_extraction` or `project_attr_extraction`, the platform **pre-creates** the attribute config and instance before the flow runs, and injects the config IDs via `ctx.system_attribute_definition_ids`. In this mode the agent does not need to create configs or attribute instances — it should:

1. Look up the config by matching `system_attribute_definition_ids[0]` against `list_dataspace_resource_attribute_configs` (or the project equivalent) to get `attribute_name`, `attribute_type`, and column schema.
2. Read the existing attribute instance ID from `core_attributes_metadata` on the resource/project response.
3. Populate the value (e.g. upsert table cells) and attach citations.
4. Submit an approval ticket referencing the attribute as a candidate.

When `system_flow_type` is `general`, no attribute context is injected and the agent must create configs and instances itself (Steps 0–1 in this document).

See the `bim-kv-table-citation-template.openflow.json` reference template for a complete working example of the `resource_attr_extraction` flow.

---

### Attribute scopes — resource vs project

There are two scopes for attributes, and choosing the right one depends on what the attribute describes:

| Scope | Also called | What it describes | `attribute_category` | `entity_id` | Config endpoint |
|---|---|---|---|---|---|
| **Resource attribute** | File attribute | A value derived from or about a **single resource** (e.g. a PDF's page count, a wall thickness extracted from one document) | `RESOURCE` | The resource UUID | `create_dataspace_resource_attribute_config` |
| **Project attribute** | Project-level attribute | A value that spans or aggregates across **multiple resources** within a project (e.g. a compliance summary across all specs, a consolidated BIM element table) | `PROJECT` | The project UUID | `create_dataspace_project_attribute_config` |

**When to use which:**
- If the attribute's value comes from a single file or describes a property of that file → **resource attribute**
- If the attribute's value is derived from multiple files, aggregates data across resources, or describes a property of the project as a whole → **project attribute**

The API mechanics are identical for both scopes — same endpoints, same models. The only differences are:
1. `attribute_category` parameter: `RESOURCE` or `PROJECT`
2. `entity_id`: pass the resource UUID or project UUID respectively
3. Config endpoint: `create_dataspace_resource_attribute_config` vs `create_dataspace_project_attribute_config`

All examples in this document use resource attributes. To use project attributes instead, swap these three values.

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
        entity_id=resource_uuid,   # REQUIRED — links attribute to entity
        # extraction_status is intentionally NOT set.
        # The default is PENDING_APPROVAL, which is what we want: the attribute
        # will be finalised via an approval ticket (Step 3), not by the agent.
    ),
)

attribute_id = attr.id   # UUID — needed for citation calls and for the approval ticket candidate
```

For a project-level attribute, use the same endpoint with `PostGeneralDataspaceAttributeDataspaceEntityType.PROJECT` as `attribute_category`.

> **Do not pass `extraction_status=AttributeExtractionStatusChoices.COMPLETED`.** Agents running inside a process execution submit an approval ticket (Step 3) instead. While the ticket is pending, the attribute will **not** appear in `core_attributes_metadata` on the resource response — that is expected. It becomes visible once approved.

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

Table attributes require a **three-step process**: declare the config (Step 0), create the attribute instance on the resource (Step 1b), then populate the table cells (Step 1c).

> **Why three steps?** The upsert endpoint (`upsert_dataspace_table_attributes`) requires an existing `TableAttribute` ID in the URL path. It **cannot** create a new attribute — it returns 404 if the attribute doesn't exist. You must create the empty attribute instance first.

### Step 1b — Create the empty table attribute instance

Use `post_general_dataspace_attribute` to create the `TableAttribute` record and link it to the resource. The `value` must be a dict matching the `Table` schema — **not** a list.

> **Do not pass `extraction_status`.** Leave it at its default (`PENDING_APPROVAL`). The attribute will not be linked to the resource via the M2M relation and will not appear in `core_attributes_metadata` until the approval ticket created in Step 3 is approved. This is intentional. You still receive the `attribute_id` in the 201 response, so Step 1c (cell upsert) and Step 2 (citations) can proceed normally.

```python
from tektome.endpoints.api.dataspace import post_general_dataspace_attribute
from tektome.endpoints.models.create_attribute_request import CreateAttributeRequest
from tektome.endpoints.models.create_attribute_request_value_type_7 import CreateAttributeRequestValueType7
from tektome.endpoints.models.attribute_type import AttributeType
from tektome.endpoints.models.post_general_dataspace_attribute_dataspace_entity_type import (
    PostGeneralDataspaceAttributeDataspaceEntityType,
)

# Build the initial empty table value — must be a dict with "rows" and "columns"
# Columns must match those declared in attribute_metadata during config creation (Step 0)
columns = [
    {"name": "element_id", "type": "string"},
    {"name": "type",       "type": "string"},
    {"name": "thickness",  "type": "float"},
]
table_value = CreateAttributeRequestValueType7()
table_value.additional_properties = {
    "rows": [],
    "columns": columns,
}

attr_resp = post_general_dataspace_attribute.sync_detailed(
    dataspace_id=dataspace_uuid,
    attribute_category=PostGeneralDataspaceAttributeDataspaceEntityType.RESOURCE,
    client=client,
    body=CreateAttributeRequest(
        name=attr_name,                # attribute_name from config (Step 0) — NOT the label
        value=table_value,
        type_=AttributeType.TABLE_ATTRIBUTES,
        entity_id=resource_uuid,
        # extraction_status is intentionally omitted — defaults to PENDING_APPROVAL.
    ),
)
if attr_resp.status_code.value == 201:
    attr_data = json.loads(attr_resp.content.decode())
    attribute_id = UUID(attr_data["id"])
else:
    raise RuntimeError(
        f"post_general_dataspace_attribute failed: {attr_resp.status_code.value} "
        f"{attr_resp.content.decode()}"
    )
```

**Value shape rules:**
- `value` must be a dict with `"rows"` and `"columns"` keys — **not** a list like `[]`
- `"columns"` must have at least one entry and match the config's `attribute_metadata.columns`
- `"rows"` can be `[]` for an empty table
- Passing `value=[]` or `value="placeholder"` causes a **500 ValidationError** on the server

**Re-runs / idempotency:** Because pending attributes are not exposed via `core_attributes_metadata`, a re-run cannot rediscover an existing pending table from the resource response. If you need to resume a prior run, list the approval candidates on the active execution (see Step 3) and reuse the `attribute_id` from the existing candidate instead of creating a new one.

### Step 1c — Populate the table cells

Now that the attribute instance exists, use `upsert_dataspace_table_attributes` to write cell data. This replaces the **entire table** in one call. Send a flat list of `TableCellUpdate` objects — one per cell — using `row_index` and `column` to address each cell.

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
    attribute_id=attribute_id,    # attribute INSTANCE ID from Step 1b — NOT the config ID
    client=client,
    body=body,
)
if upsert_resp.status_code.value != 204:
    raise RuntimeError(f"upsert_dataspace_table_attributes failed: {upsert_resp.content.decode()}")
```

### Version handling for `upsert_dataspace_table_attributes`

> **Do NOT pass `version=None`.** `None` serializes as `"version": null` in the JSON body, which the server interprets as a version mismatch and returns **409 Table has been modified**.

The `version` field uses `UNSET` semantics (see "UNSET vs None" below):
- **New table (first write after Step 1b):** leave `version` as the default `UNSET` — it is omitted from the request body entirely. This is the common case when the agent creates the attribute and immediately populates its cells in the same run.
- **Updating an already-approved table:** read the current version from the resource metadata (`core_attributes_metadata.<name>.value.version`) and pass it explicitly.

```python
body = UpdateDataspaceTableAttributeRequest(cells=cells)  # UNSET — version omitted
```

### Getting the `attribute_id` for citations

Parse `id` from the Step 1b 201 response body and keep it in memory for the rest of the run — you'll need it for Step 1c (cell upsert), Step 2 (citations), and Step 3 (approval-ticket candidate payload).

Because the attribute is `pending_approval`, it is **not** in `core_attributes_metadata` yet, so you cannot recover its ID by reading the resource. After the approval ticket is approved, the attribute promotes to `completed` and the resource response structure becomes:

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

### Table behaviour

- **Full replace**: every call to `upsert_dataspace_table_attributes` replaces the entire table. To add a row to an existing table, read the current data first, append to it, and send the complete set.
- **Columns must match the config**: column names in `TableCellUpdate` must match the names declared in `attribute_metadata.columns` when the config was created.
- **Sparse cells**: rows that are missing a column get `None` for that column.
- **`version`**: used for optimistic concurrency control. Pass the version number from `core_attributes_metadata.<name>.value.version` when updating an existing table. Leave as `UNSET` (the default) for a first write — do **not** pass `None`, which serializes as `null` and causes a 409.
- **`insert_dataspace_table_attribute_row`**: inserts a blank row at a given `row_index`, shifting existing rows down. Use this when you need to splice a row into the middle of an existing table rather than replacing everything.
- **Do NOT call `post_general_dataspace_attribute` again after Step 1b.** Each call creates a new attribute record; a second call for the same logical attribute produces a disconnected duplicate that will never be linked to the resource. Create the attribute once, keep the `attribute_id` in memory, and submit a single approval ticket for it.

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
    # Find the existing citation ID then PATCH it.
    # get_attribute_citations returns the standard paginated envelope (see SKILL.md
    # "List response shape"): records live under "items" — there is NO "bim_citations"
    # sub-key. The list is mixed-type (BIM, PDF, image, raw-text, attribute-to-attribute
    # interleaved); filter by citation_type == "bim". Note: the POST response uses
    # citation_type="bim_citation" (schema field), but the list response uses "bim".
    list_resp = get_attribute_citations.sync_detailed(
        dataspace_id=dataspace_uuid,
        attribute_category=GetAttributeCitationsDataspaceEntityType.RESOURCE,
        attribute_id=attribute_id,
        client=client,
        page_size=100,
    )
    citations_data = list_resp.parsed.items
    bim_citation_id = next(
        c.id for c in citations_data if c.citation_type == "bim_citation"
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

## Step 3 — Submit an approval ticket

After creating the attribute (Step 1 / Step 1b–c) and attaching its citations (Step 2), submit an approval ticket so a human can review and approve the work. The attribute stays `pending_approval` — and therefore hidden from `core_attributes_metadata` — until the ticket is approved.

This step is **required** for agents running inside a Tektome process execution. It is how values reach the resource.

### When to submit the ticket

One ticket per execution, submitted **after** all candidate attributes and their citations have been created. Batch every candidate produced by the run into a single ticket via the `candidates` list — do not POST a ticket per attribute.

### Required context

- `dataspace_id` — the dataspace the attributes live in.
- `execution_id` — the current process execution. When the script is running as an Openflow process, read it from `Context.system_execution_id`. It must be non-null.

```python
from tektome.endpoints.api.dataspace_approval_tickets import (
    create_execution_approval_ticket_with_candidates,
)
from tektome.endpoints.models.approval_category_types import ApprovalCategoryTypes
from tektome.endpoints.models.attribute_candidate_payload import AttributeCandidatePayload
from tektome.endpoints.models.candidate_item import CandidateItem
from tektome.endpoints.models.candidate_item_kind import CandidateItemKind
from tektome.endpoints.models.create_approval_ticket_request import CreateApprovalTicketRequest
from tektome.endpoints.models.create_execution_approval_ticket_with_candidates_multi_part_body_params import (
    CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
)

# One CandidateItem per attribute the agent produced in this run.
# `kind` must match the attribute's type.
candidates = [
    CandidateItem(
        kind=CandidateItemKind.CREATE_UPDATE_FLOAT_ATTRIBUTES,
        data=AttributeCandidatePayload(
            attribute_id=attribute_id,      # UUID from Step 1 / Step 1b
            resource_id=resource_uuid,      # for resource-scoped attributes
            # or: project_id=project_uuid   # for project-scoped attributes
        ),
    ),
    # ... additional CandidateItem entries for each attribute produced in this run
]

payload = CreateApprovalTicketRequest(
    category=ApprovalCategoryTypes.ATTRIBUTE_UPDATE,
    candidates=candidates,
)

ticket_resp = create_execution_approval_ticket_with_candidates.sync_detailed(
    dataspace_id=dataspace_uuid,
    execution_id=ctx.system_execution_id,   # from the Openflow Context
    client=client,
    body=CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams(payload=payload),
)
if ticket_resp.status_code.value != 201:
    raise RuntimeError(
        f"create_execution_approval_ticket_with_candidates failed: "
        f"{ticket_resp.status_code.value} {ticket_resp.content.decode()}"
    )

ticket_id = ticket_resp.parsed.id
```

### Candidate kinds

`CandidateItemKind` maps 1:1 onto `AttributeType`, plus `FILE_UPLOAD` for file-extraction tickets:

| `CandidateItemKind` | Use for |
|---|---|
| `CREATE_UPDATE_<TYPE>_ATTRIBUTES` | The corresponding primitive/table/JSON attribute kind |
| `FILE_UPLOAD` | File-extraction tickets (`ApprovalCategoryTypes.FILE_EXTRACTION`) with `FileUploadCandidatePayload` |

For attribute extraction, use `ApprovalCategoryTypes.ATTRIBUTE_UPDATE` and the matching `CREATE_UPDATE_*` kind per candidate.

### Inspecting pending candidates

Because pending attributes are not in `core_attributes_metadata`, use the approval-ticket endpoints to enumerate in-flight work:

- `get_execution_approvals` — list approval tickets for an execution.
- `get_approval_ticket_details` — inspect a ticket by ID.
- `get_approval_candidates` — list the candidates attached to a ticket, including their `attribute_id` and `serialized_review_data`.

These replace `get_dataspace_project_resource` → `core_attributes_metadata` for discovering work the agent has produced but that has not yet been approved.

---

## Key rules

| Rule | Detail |
|---|---|
| Declare config before writing | Both primitive and table attributes require a config registered on the dataspace first |
| Table config needs column schema | Pass `attribute_metadata` with a `columns` list when declaring a table config |
| `attribute_type` in config is a plain string | Use `"float_attributes"`, `"table_attributes"` etc. — not the `AttributeType` enum |
| Table attributes need Step 1b before upsert | `upsert_dataspace_table_attributes` returns 404 if the attribute instance doesn't exist — you must create it first with `post_general_dataspace_attribute` |
| Table `value` must be a dict, not a list | Pass `{"rows": [], "columns": [...]}` — not `[]` or `"placeholder"` |
| Do NOT set `extraction_status=COMPLETED` | Agents must leave `extraction_status` at its default (`PENDING_APPROVAL`) and submit an approval ticket (Step 3). Setting `COMPLETED` bypasses human review |
| Use `post_general_dataspace_attribute` to get `attribute_id` | Returns `AttributeResponse` with `id` — needed for citations and as the approval candidate's `attribute_id`. For table attributes, the ID is returned in the Step 1b response |
| `attribute_type` in citation body | Must match the type of the attribute you're citing |
| `attribute_category` | `RESOURCE` or `PROJECT` — matches where the attribute lives |
| `dataspace_id` required | All citation and approval-ticket endpoints operate within a dataspace context |
| BIM `bim_elements` is required | Must include at least one `BIMElementRequest`; `bim_element_id` is optional (omit to cite the whole project) |
| `bim_element_id` is the 32-char Speckle hash | Not the UUID, not the Revit Tag — use the `id` returned by the KV search endpoint |
| Citation `title` max 32 characters | The database column is `varchar(32)` — longer titles cause a 400 error |
| One BIM citation per resource-attribute pair | POSTing a second citation returns 400 "already cited" — use PATCH to update the existing one |
| Image `bounding_geometry` is required | Must always be provided for image citations |
| PDF `polygons` is optional | Can be omitted if you only need to cite the resource without a specific region |
| Citations attach to the attribute, not individual rows | For table attributes, all citations link to the table attribute UUID as a whole |
| Keep table `attribute_id` from Step 1b in memory | Pending attributes are not in `core_attributes_metadata`, so there is no way to recover the ID from the resource until the approval ticket is approved |
| `version` for tables: `UNSET` for new, integer for updating approved tables | `version=None` serializes as `null` → 409. Only approved tables expose a `version` via `core_attributes_metadata.<name>.value.version` |
| One approval ticket per execution | Batch all candidates produced by a run into a single `create_execution_approval_ticket_with_candidates` call; do not POST one ticket per attribute |
| `execution_id` is required for the approval ticket | Read from `Context.system_execution_id` in Openflow scripts — it must be non-null |

---

## Shortcut helpers

The `tektome.shortcuts` module bundles common multi-call workflows into a single function.

#### `create_attribute_approval_ticket`

Creates attribute on the system resource or system project into a single approval ticket. All payloads in a single call must share the same `attribute_type`.

```python
from tektome import Context
from tektome.endpoints.models import AttributeType
from tektome.shortcuts.create_attribute_approval_ticket import (
    AttributeConfig,
    AttributePayload,
    create_attribute_approval_ticket,
)

def main(ctx: Context):
    payloads = [
        AttributePayload(
            attribute_config=AttributeConfig(
                attribute_name="title",
                attribute_type=AttributeType.STRING_ATTRIBUTES,
            ),
            value="Project Alpha",
        )
    ]

    with ctx.client() as client:
        response = create_attribute_approval_ticket(client, ctx, payloads)
        print(f"Approval ticket created: {response.parsed}")
```

## Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Passing `value=[]` or `value="placeholder"` in Step 1b | **500 ValidationError** — server calls `Table.model_validate()` which expects a dict | Pass `value={"rows": [], "columns": [...]}` with columns matching the config |
| Setting `extraction_status=COMPLETED` from an agent | Bypasses human approval, skips the ticket pipeline, and attaches unreviewed values to the resource | Leave `extraction_status` at its default (`PENDING_APPROVAL`) and submit an approval ticket (Step 3) |
| Skipping Step 3 (no approval ticket) | Attribute stays `pending_approval` forever, never promotes to `completed`, and never appears in `core_attributes_metadata` | Always finish the run by calling `create_execution_approval_ticket_with_candidates` with one candidate per attribute produced |
| POSTing a separate ticket per attribute | Clutters the approvals inbox and may exceed per-execution limits | Bundle all candidates for the run into a single ticket's `candidates` list |
| Relying on `core_attributes_metadata` to rediscover an attribute after Step 1b | Pending attributes are filtered out of the resource response — lookup returns nothing | Keep the `attribute_id` from the Step 1b 201 response in memory, or enumerate via `get_approval_candidates` |
| Omitting `entity_id` in Step 1 / Step 1b | Attribute is created but not linked to any resource/project | Always pass `entity_id=resource_uuid` (or project UUID) |
| Calling `post_general_dataspace_attribute` a second time for the same logical attribute | Creates a disconnected duplicate record; only one can be referenced from the approval ticket | Call it once per attribute per run and reuse the `attribute_id` |
| Skipping Step 1b and calling `upsert_dataspace_table_attributes` directly | **404 Attribute not found** — the upsert endpoint cannot create attributes | Always create the attribute instance first (Step 1b) before upserting cells |
| Using the config ID as `attribute_id` in the upsert | **404 Attribute not found** — config IDs and attribute instance IDs are different models | Use the attribute instance ID from the Step 1b response |
| Passing `version=None` to `upsert_dataspace_table_attributes` | Server returns **409 Table has been modified** | Leave `version` as `UNSET` (default) for the first write; pass the integer version only when updating an already-approved table |
| Passing the document `resource_id` as `bim_resource_id` in a BIM citation | Server returns 400/404; no citations created | `bim_resource_id` must be the BIM resource (IFC file) UUID — always a separate parameter |
| Using `sync()` instead of `sync_detailed()` for citations or approval tickets | Script reports success but no citations/tickets exist | Use `sync_detailed()` and check `resp.status_code.value == 201` |
| Using `attribute_label` instead of `attribute_name` as the attribute `name` | `upsert_dataspace_table_attributes` or `post_general_dataspace_attribute` fails or targets wrong attribute | The config returns both; use `attribute_name` (the server-generated key) not `attribute_label` (the human label) |
| Using `AttributeType` enum values in config `attribute_type` | Config creation fails | Use plain strings: `"table_attributes"`, `"float_attributes"`, etc. |
| Submitting the approval ticket without `execution_id` (or with a stale one) | **400/404** from `create_execution_approval_ticket_with_candidates` | Read `ctx.system_execution_id` inside the Openflow-scope `main` and pass it as `execution_id` |

---

## Reasoning

Reasoning (the LLM's explanation of why an attribute has its value) is **read-only** — it is set exclusively by the extraction pipeline and cannot be written manually. There is no endpoint to set or update it.
