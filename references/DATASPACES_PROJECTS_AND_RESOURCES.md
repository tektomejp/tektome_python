# Dataspaces, Projects, and Resources — Agent Reference

This document explains the Tektome data hierarchy and how to navigate it using the Python SDK. It covers listing dataspaces, projects, and resources, retrieving resource metadata, and understanding the relationships between entities.

---

## Overview

Tektome data is organised in a three-level hierarchy:

```
Organization
  └── Dataspace            (isolated collaborative workspace)
        └── Project        (logical grouping within a dataspace)
              └── Resource (uploaded file: PDF, IFC, image, etc.)
```

All attribute, citation, and extraction operations require knowing which **dataspace**, **project**, and/or **resource** you're working with. In Openflow scripts, the execution context provides these IDs automatically via `ctx.system_dataspace_id`, `ctx.system_project_id`, and `ctx.system_resource_id`. In standalone scripts, you navigate the hierarchy manually.

### Key entity relationships

| Entity | Contains | Identified by |
|---|---|---|
| **Organization** | Dataspaces, users, roles | `organization_id` (UUID) |
| **Dataspace** | Projects, attribute configs, processes, search configs | `dataspace_id` (UUID) |
| **Project** | Resources, project-level attributes | `project_id` (UUID) |
| **Resource** | Pages, sections, resource-level attributes, BIM projects | `resource_id` (UUID) |

---

## Listing dataspaces

```python
from tektome.endpoints.api.dataspace import list_dataspaces

resp = list_dataspaces.sync_detailed(
    client=client,
    page=1,
    page_size=50,
)

for ds in resp.parsed.items:
    print(ds.id, ds.core_attributes.name)
```

Filter by organization:

```python
resp = list_dataspaces.sync_detailed(
    client=client,
    organization_id=org_uuid,
    page=1,
)
```

---

## Listing projects in a dataspace

```python
from tektome.endpoints.api.dataspace import list_dataspace_projects

resp = list_dataspace_projects.sync_detailed(
    dataspace_id=dataspace_uuid,
    client=client,
    page=1,
    page_size=100,
    sort_by="name",
)

for project in resp.parsed.items:
    print(project.id, project.core_attributes.name)
```

---

## Listing resources in a project

```python
from tektome.endpoints.api.dataspace import list_dataspace_project_resources

resp = list_dataspace_project_resources.sync_detailed(
    project_id=project_uuid,
    client=client,
    page=1,
    page_size=100,
)

for resource in resp.parsed.items:
    print(resource.id, resource.core_attributes.name)
```

### Pagination

All list endpoints return paginated responses. The response object contains:
- `items` — list of entities for the current page
- `count` — total number of entities
- `total_page` — total number of pages

To iterate through all pages:

```python
all_resources = []
page = 1
while True:
    resp = list_dataspace_project_resources.sync_detailed(
        project_id=project_uuid, client=client, page=page, page_size=100,
    )
    if resp.status_code.value != 200 or not resp.parsed:
        break
    all_resources.extend(resp.parsed.items)
    if page >= resp.parsed.total_page:
        break
    page += 1
```

---

## Getting a single resource

Retrieve full resource details including `core_attributes_metadata` (where approved attribute values live):

```python
from tektome.endpoints.api.dataspace import get_dataspace_project_resource

resp = get_dataspace_project_resource.sync_detailed(
    resource_id=resource_uuid,
    client=client,
)
resource = resp.parsed
```

The response includes:
- `id` — resource UUID
- `core_attributes` — basic metadata (name, file type, etc.)
- `core_attributes_metadata` — approved attribute values keyed by attribute name

### Reading attribute values from a resource

```python
import json

res_data = json.loads(resp.content.decode())
attrs_meta = res_data.get("core_attributes_metadata", {})

# Read a primitive attribute value
wall_thickness = attrs_meta.get("wall_thickness", {}).get("value")

# Read a table attribute
table = attrs_meta.get("bim_objects", {})
if table:
    table_id = table["id"]
    rows = table["value"]["rows"]
    version = table["value"]["version"]
```

**Only approved attributes appear in `core_attributes_metadata`.** Attributes with `extraction_status=PENDING_APPROVAL` are not visible here — use approval-ticket endpoints to inspect pending work. See [MANUAL_ATTRIBUTES_AND_CITATIONS.md](MANUAL_ATTRIBUTES_AND_CITATIONS.md) for details.

---

## Getting resource details (Lawtalk)

For additional resource metadata like file URL and init status:

```python
from tektome.endpoints.api.resource import get_lawtalk_resource

resource = get_lawtalk_resource.sync(
    resource_id=str(resource_uuid),
    client=client,
)
```

---

## Attribute configs on a dataspace

Attribute configs define what attributes can exist on resources or projects within a dataspace. List them to discover available attribute schemas:

### Resource attribute configs

```python
from tektome.endpoints.api.dataspace import list_dataspace_resource_attribute_configs

configs_resp = list_dataspace_resource_attribute_configs.sync_detailed(
    dataspace_id=dataspace_uuid,
    client=client,
    page=1,
    page_size=100,
)

for cfg in configs_resp.parsed.items:
    print(cfg.id, cfg.attribute_name, cfg.attribute_type)
    if cfg.attribute_metadata:
        columns = cfg.attribute_metadata.additional_properties.get("columns", [])
        print("  columns:", columns)
```

### Project attribute configs

```python
from tektome.endpoints.api.dataspace import list_dataspace_project_attribute_configs

configs_resp = list_dataspace_project_attribute_configs.sync_detailed(
    dataspace_id=dataspace_uuid,
    client=client,
    page=1,
    page_size=100,
)
```

### Resolving config from `system_attribute_definition_ids`

In `resource_attr_extraction` or `project_attr_extraction` flows, the platform injects attribute config IDs via `ctx.system_attribute_definition_ids`. Match them against the config list:

```python
target_config_id = ctx.system_attribute_definition_ids[0]

attr_config = None
page = 1
while True:
    configs_resp = list_dataspace_resource_attribute_configs.sync_detailed(
        dataspace_id=ctx.system_dataspace_id, client=client, page=page, page_size=100,
    )
    if configs_resp.status_code.value != 200 or not configs_resp.parsed:
        break
    for cfg in configs_resp.parsed.items:
        if cfg.id == target_config_id:
            attr_config = cfg
            break
    if attr_config or page >= configs_resp.parsed.total_page:
        break
    page += 1

attr_name = attr_config.attribute_name
attr_type = attr_config.attribute_type
```

---

## Openflow context fields

When running as an Openflow, the `Context` object provides pre-resolved IDs. Which fields are available depends on `system_flow_type`:

| Field | `general` | `resource_attr_extraction` | `project_attr_extraction` |
|---|---|---|---|
| `system_user_api_key` | always | always | always |
| `system_base_url` | always | always | always |
| `system_flow_type` | always | always | always |
| `system_dataspace_id` | if available | always | always |
| `system_execution_id` | if available | always | always |
| `system_project_id` | if available | if available | always |
| `system_resource_id` | if available | always | if available |
| `system_attribute_definition_ids` | never | always (non-empty) | always (non-empty) |
| `system_chatroom_id` | if invoked from chat | if invoked from chat | if invoked from chat |

**Guarded fields** raise `AttributeError` when accessed if the value is not available. This means you don't need explicit None checks — just use them and catch `AttributeError` if the field might not be present.

```python
try:
    ds_id = ctx.system_dataspace_id
except AttributeError:
    raise RuntimeError("This flow requires a dataspace context")
```

---

## Document search

Search across indexed documents within dataspaces:

```python
from tektome.endpoints.api.search import search_documents
from tektome.endpoints.models.search_document_request import SearchDocumentRequest
from tektome.endpoints.models.azure_embedding_model import AzureEmbeddingModel

results = search_documents.sync_detailed(
    client=client,
    body=SearchDocumentRequest(
        embedding_model=AzureEmbeddingModel.AZURE_TEXT_EMBEDDING_3_LARGE,
        query_content="structural specification",
        data_space_ids=[str(dataspace_uuid)],  # optional: scope to specific dataspaces
    ),
)
```

See [PDF_DATA_AND_TOOLS.md](PDF_DATA_AND_TOOLS.md) for the full document search and PDF handling reference.

---

## Key rules

| Rule | Detail |
|---|---|
| Hierarchy is Organization → Dataspace → Project → Resource | All operations require knowing the correct level in the hierarchy |
| `core_attributes_metadata` only shows approved attributes | Pending attributes (from in-flight extractions) are not visible — use approval-ticket endpoints |
| Guarded context fields raise `AttributeError` | Don't check for `None` — just access the field and catch `AttributeError` if it might not be present |
| `attribute_name` ≠ `attribute_label` | Configs have both: `attribute_label` is the human-readable display name, `attribute_name` is the server-generated key (lowercase, underscores). Always use `attribute_name` for API calls |
| Pagination starts at page 1 | Not page 0 |
| `system_attribute_definition_ids` contains config IDs | These are attribute config IDs, not attribute instance IDs. The instance ID comes from the resource's `core_attributes_metadata` or from `post_general_dataspace_attribute` |
| All list endpoints are paginated | Always check `total_page` and loop if you need all results |
| `resource_id` parameter types vary | Some endpoints take `UUID`, others take `str`. Check the endpoint signature |

---

## Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Confusing `attribute_name` with `attribute_label` | API calls fail or target wrong attribute | Use `attribute_name` (the config's server-generated key), not `attribute_label` (display name) |
| Confusing config ID with instance ID | 404 when upserting table cells or creating citations | Config ID comes from `system_attribute_definition_ids`; instance ID comes from `core_attributes_metadata` or `post_general_dataspace_attribute` response |
| Expecting pending attributes in `core_attributes_metadata` | Attribute appears missing after creation | Pending attributes are hidden until approved. Use approval-ticket endpoints to inspect in-flight work |
| Not paginating list results | Only seeing first page of results | Check `total_page` in the response and loop through all pages |
| Accessing guarded context fields without handling `AttributeError` | Unhandled `AttributeError` crash | Wrap access in try/except when the field might not be available for the current flow type |
| Using `organization_id` without knowing it | 403 or empty results | In Openflow scripts, the organization is implicit from the user's token. In standalone scripts, you may need to look it up via account endpoints |
| Passing `str(uuid)` where `UUID` is expected (or vice versa) | Type errors or 422 responses | Check the endpoint's parameter type — some accept `UUID`, others accept `str` |

---

## Endpoint reference

| Operation | Endpoint function | Method |
|---|---|---|
| List dataspaces | `dataspace.list_dataspaces` | GET |
| List projects in dataspace | `dataspace.list_dataspace_projects` | GET |
| List resources in project | `dataspace.list_dataspace_project_resources` | GET |
| Get single resource | `dataspace.get_dataspace_project_resource` | GET |
| Get resource (Lawtalk) | `resource.get_lawtalk_resource` | GET |
| List resource attribute configs | `dataspace.list_dataspace_resource_attribute_configs` | GET |
| List project attribute configs | `dataspace.list_dataspace_project_attribute_configs` | GET |
| Create resource attribute config | `dataspace.create_dataspace_resource_attribute_config` | POST |
| Create project attribute config | `dataspace.create_dataspace_project_attribute_config` | POST |
| Search documents | `search.search_documents` | POST |
| Get dataspace project | `dataspace.get_dataspace_project` | GET |
