---
name: tektome-sdk
description: Guide for writing scripts using the Tektome Python SDK. Use when creating Tektome Openflow scripts, standalone Python scripts using the Tektome API, or working with Tektome schema classes (Context, Resource, Project, etc.).
---

# Tektome Python SDK Development Guide

The `tektome` Python SDK is used in two contexts:

1. **Openflow scripts** - executed by Tektome's Openflow platform, which injects `Context` and schema inputs as dicts. Requires `@parseio` and a Pydantic `Output` model.
2. **Standalone Python scripts** - regular Python scripts that use the SDK's API client and models directly. No `@parseio` required.

---

## Openflow Scripts

Openflow is Tektome's automation platform. It calls your `main()` function with dict arguments (Context, Resource, etc.) that `@parseio` coerces into Pydantic models. The return value is serialized back to a dict for Openflow to consume.

### Required structure

```python
# requirements:
# git+https://github.com/tektomejp/tektome_python.git@<version>

from pydantic import BaseModel
from tektome import Context, Resource
from tektome.decorators import parseio

class Output(BaseModel):
    status: str

@parseio
def main(ctx: Context, resource: Resource) -> Output:
    with ctx.client() as client:
        # Use endpoint functions with client
        pass
    return Output(status="success")
```

### Key rules for Openflow

1. **Always decorate `main` with `@parseio`** - Openflow passes dicts; `@parseio` coerces them into Pydantic models via `validate_call`, and serializes the output back to a JSON-serializable dict
2. **Define a Pydantic `Output` model** for the return type - `@parseio` validates and converts it
3. **Use `ctx.client()` as a context manager** to get an authenticated HTTP client
4. **Return Pydantic models, not dicts** - `@parseio` handles the conversion
5. **Add the `# requirements:` comment** at the top so Openflow knows which packages to install

### @parseio behavior

- **Input:** dicts are coerced to Pydantic models (e.g. `{"id": "...", "kind": "resource"}` becomes `Resource`)
- **Output:** Pydantic models are converted to dicts via `.model_dump()`, then validated for JSON serializability
- Must return a `dict` or `BaseModel` - returning `str`, `list`, `int`, `None` etc. raises `TypeError`

### @parseio options

```python
@parseio                                       # default: return dict, validate JSON
@parseio(return_dict=False)                    # return Pydantic model instance
@parseio(validate_json_serializable=False)     # skip JSON validation
```

---

## Standalone Python Scripts

When using the SDK outside Openflow (CLI tools, notebooks, other services), you don't need `@parseio`. Construct `Context` or `AuthenticatedClient` directly.

```python
from uuid import UUID
from tektome import Context
from tektome.endpoints.api.dataspace import list_dataspaces

ctx = Context(
    system_user_api_key="sk-...",
    system_base_url="https://your-tektome-instance.example.com",
    system_flow_type="general",
)

with ctx.client() as client:
    response = list_dataspaces.sync_detailed(client=client)
    if response.parsed:
        for ds in response.parsed.items:
            print(ds.core_attributes.name)
```

Or use `AuthenticatedClient` directly:

```python
from tektome.endpoints.client import AuthenticatedClient

with AuthenticatedClient(
    base_url="https://your-tektome-instance.example.com",
    token="sk-...",
) as client:
    # Use endpoint functions with client
    pass
```

---

## Input Schema Classes

Import from `tektome`. These are used as `main()` parameter types in Openflow, or for constructing input manually in standalone scripts.

| Class | Fields | Kind value |
|-------|--------|------------|
| `Resource` | `id: UUID` | `"resource"` |
| `Resources` | `ids: list[UUID]` | `"resource[]"` |
| `Project` | `id: UUID` | `"project"` |
| `Projects` | `ids: list[UUID]` | `"project[]"` |
| `AttributeDefinitions` | `ids: list[UUID]` | `"attribute_definition[]"` |
| `Date` | `value: date` | `"date"` |
| `DateTime` | `value: datetime` | `"datetime"` |

All schemas use `extra="forbid"` - unexpected fields raise validation errors.

## Context Object

`Context` provides authentication and execution metadata injected by Openflow (or constructed manually for standalone use):

```python
ctx.system_user_api_key   # str - Bearer token for API auth
ctx.system_base_url       # AnyHttpUrl - deployment base URL
ctx.system_flow_type      # Literal["general", "project_attr_extraction", "resource_attr_extraction"]
```

**Guarded fields** (raise `AttributeError` if not available in current execution context):

```python
ctx.system_chatroom_id              # UUID | None - only when invoked from a chatroom
ctx.system_execution_id             # UUID | None
ctx.system_dataspace_id             # UUID | None
ctx.system_project_id               # UUID | None
ctx.system_resource_id              # UUID | None
ctx.system_attribute_definition_ids # list[UUID] | None
```

### Flow types and attribute definition IDs

| `system_flow_type` | Guaranteed context fields | Description |
|---|---|---|
| `"general"` | None beyond auth | General-purpose flow — no attribute or entity context is injected |
| `"resource_attr_extraction"` | `system_resource_id`, `system_attribute_definition_ids` | The platform pre-creates attribute instances on the resource and passes their config IDs. The flow should populate their values and submit approval tickets. |
| `"project_attr_extraction"` | `system_project_id`, `system_attribute_definition_ids` | Same as above, but attributes are scoped to a project rather than a single resource. |

When `system_flow_type` is `resource_attr_extraction` or `project_attr_extraction`, the flow can expect `system_attribute_definition_ids` to be a non-empty list of attribute config UUIDs. These identify which attribute configs to look up on the dataspace (via `list_dataspace_resource_attribute_configs` or `list_dataspace_project_attribute_configs`) to obtain the `attribute_name`, `attribute_type`, and column schema. The corresponding attribute instances are already created on the target entity and can be found via `core_attributes_metadata` on the resource/project response.

Use `ctx.client()` to get an `AuthenticatedClient` pre-configured with credentials.

## Making API Calls

Endpoints are in `tektome.endpoints.api.<domain>`. Request/response models are in `tektome.endpoints.models`.

```python
from tektome.endpoints.api.resource import get_lawtalk_resource

response = get_lawtalk_resource.sync_detailed(
    resource_id=str(resource.id),
    client=client,
)

if response.parsed is None:
    raise ValueError(
        f"API error: {response.status_code} - {response.content.decode()}"
    )

result = response.parsed
```

### API domains

Endpoints are organized under: `access`, `account`, `attribute`, `dataspace`, `extraction`, `project`, `resource`, `search`, `user`, and 30+ more domains in `tektome/endpoints/api/`.

### Error handling pattern

Use `raise_on_unexpected_status=False` in `ctx.client()` and check `response.parsed`:

```python
with ctx.client(raise_on_unexpected_status=False) as client:
    response = some_endpoint.sync_detailed(client=client, body=payload)
    if response.parsed is None:
        raise ValueError(f"Failed: {response.status_code} - {response.content.decode()}")
```

### List response shape

All paginated list endpoints (e.g. `get_attribute_citations`,
`list_dataspace_resource_attribute_configs`, `get_execution_approvals`,
`get_approval_candidates`, `list_bim_projects_by_resource`) return the same
envelope: `{"items": [...], "count": N, "page": ..., "total_page": ...}`.

**Records always live under the `"items"` key. There are no type-specific
sub-keys** like `"bim_citations"`, `"pdf_citations"`, `"candidates"`, or
`"configs"` — even when the list is mixed-type. Filter the flat `items` list by
a discriminator field on each record (e.g. `citation_type`, `kind`).

Prefer `response.parsed.items` when the SDK has a typed model:

```python
resp = list_dataspace_resource_attribute_configs.sync_detailed(
    dataspace_id=ds_uuid, client=client, page=1, page_size=100,
)
for cfg in resp.parsed.items:                       # ✅ typed access
    ...
```

Only fall back to `json.loads(...)` when you need a field the typed model
doesn't expose, and read from `"items"`:

```python
body = json.loads(resp.content.decode())
records = body.get("items", [])                     # ✅ always "items"
# body.get("bim_citations")                         # ❌ this key does not exist
```

Mixed-type example — `get_attribute_citations` returns BIM, PDF, image,
raw-text, and attribute-to-attribute citations interleaved in one `items`
list, each tagged with `citation_type`:

```python
body = json.loads(resp.content.decode())
bim_citation_id = next(
    UUID(c["id"]) for c in body.get("items", []) if c.get("citation_type") == "bim"
)
```

## Important Notes

- The `tektome/endpoints/` directory is **auto-generated** from OpenAPI spec - never edit it directly
- Python 3.13+ required
- Schema validation uses Pydantic v2
- Both sync and async clients are supported (`ctx.client()` for sync, async context manager for async)

## References

The `references` directory contains markdown files detailing specific Tektome concepts, like "attribute extraction", "citation creation", etc. Use these to help understand how to use the SDK for common tasks.
The following references are available:
- [Attribute Extraction](references/ATTRIBUTE_EXTRACTION.md) -- how to use the SDK to run agentic attribute extraction flows, and how to interpret the results
- [Manual Attributes and Citation Creation](references/MANUAL_ATTRIBUTES_AND_CITATIONS.md) -- how to use the SDK to create manually create attributes and citations to resources, and best practices for doing so
- [BIM Data and Tools](references/BIM_DATA_AND_TOOLS.md) -- how to search, fetch, and analyse BIM elements (KV search, batch streaming, spatial queries, clash detection, element data structure)
- [BIM Spatial Analysis Playbook](references/BIM_SPATIAL_ANALYSIS_PLAYBOOK.md) -- task-level workflow for BIM spatial OpenFlows: rooms/spaces, doors, object locations, bboxes, topology search, distances, and geometry fallback
- [PDF Data and Tools](references/PDF_DATA_AND_TOOLS.md) -- how to upload PDFs, trigger OCR extraction, list pages, search documents, and create PDF citations with polygon annotations
- [Dataspaces, Projects, and Resources](references/DATASPACES_PROJECTS_AND_RESOURCES.md) -- navigating the data hierarchy (dataspaces → projects → resources), reading attribute metadata, resolving configs, and understanding Openflow context fields
- [Custom BIM Visual Aids](references/CUSTOM_BIM_VISUAL_AIDS.md) -- how to create custom BIM geometry (lines, meshes, text) as visual aids in citations, e.g. escape routes, highlight zones, measurement labels
