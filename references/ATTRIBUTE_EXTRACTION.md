# Attribute Extraction — Agent Reference

This document explains how to run LLM-based attribute extraction on a PDF resource using the Tektome Python SDK. Follow each step in order; skipping any will result in a 400/422 error.

---

## Overview

Attribute extraction runs an LLM over a PDF resource to answer a question and return a typed value plus reasoning. The full flow is:

```
list pages → create section → submit extraction (for_approval=True) → poll for result → create approval ticket
```

The attribute `name` passed to the extraction must match an existing attribute config in the dataspace. When it does, the extraction automatically persists the value and citations to the dataspace — no separate upload or citation step is needed.

---

## Step 1 — List pages for the resource

Fetch all pages belonging to the PDF resource and collect their IDs.

```python
from tektome.endpoints.api.page import list_resource_pages
from uuid import UUID

pages = list_resource_pages.sync(resource_id=resource_uuid, client=client)
page_ids = [p.id for p in pages if isinstance(p.id, UUID)]
```

**If `page_ids` is empty**, the resource has not been OCR-processed yet. Extraction cannot proceed.

---

## Step 2 — Create a Section

A Section is required as the context container for extraction. Create one with the page IDs.

```python
from tektome.endpoints.api.section import create_core_section
from tektome.endpoints.models.create_section_creation_request import CreateSectionCreationRequest

section_body = CreateSectionCreationRequest(
    project_id=project_uuid,   # project the resource belongs to — required
    page_ids=page_ids,         # all page IDs from step 1
)
section_response = create_core_section.sync_detailed(client=client, body=section_body)
# section_response.status_code should be 201
section_id = section_response.parsed.id
```

### Critical rules for Section creation

| Field | Usage |
|---|---|
| `page_ids` | ✅ Use this for PDF page content |
| `resource_ids` | ❌ Reserved for **images only** — do not pass PDF resource IDs here |
| `project_id` | ✅ Required — must be the project the resource belongs to |

---

## Step 3 — Submit attribute extraction

```python
from tektome.endpoints.api.extraction import create_attribute_extraction
from tektome.endpoints.models.create_extraction_request import CreateExtractionRequest
from tektome.endpoints.models.attribute import Attribute
from tektome.endpoints.models.attribute_type import AttributeType
from tektome.endpoints.models.recipeschoices import RECIPESCHOICES

body = CreateExtractionRequest(
    section_id=section_id,
    recipe=RECIPESCHOICES.V1,                     # see Recipes below
    attributes=[
        Attribute(
            name="contract_value",                # see Attribute name rules below
            prompt="What is the total contract value?",
            kind=AttributeType.STRING_ATTRIBUTES,
        )
    ],
    enduser_prompt="What is the total contract value?",
    include_pdf_pages_as_images=True,             # recommended for PDFs
    for_approval=True,                            # required for Step 6 — see below
)

extraction_response = create_attribute_extraction.sync_detailed(client=client, body=body)
# extraction_response.status_code should be 201
```

### Recipes

Only one recipe is valid for attribute extraction:

| Recipe | Use when |
|---|---|
| `RECIPESCHOICES.V1` (`"v1"`) | Standard extraction — use for all attributes |

All other `RECIPESCHOICES` values (`deep-research-*`, `auto-capture-*`, `tektome-os-v1`) are for other functions and **will fail** if used for attribute extraction.

### Attribute name rules

- Must be **lowercase**
- No spaces (use underscores: `"contract_value"` not `"contract value"`)
- Must not start with `"system:"`
- Must not end with `"_error_message"` or `"_sources"`

### Attribute types

```python
class AttributeType(str, Enum):
    BOOLEAN_ATTRIBUTES     = "boolean_attributes"
    COORDINATE_ATTRIBUTES  = "coordinate_attributes"
    DATETIME_ATTRIBUTES    = "datetime_attributes"
    DATE_ATTRIBUTES        = "date_attributes"
    FLOAT_ATTRIBUTES       = "float_attributes"
    INTEGER_ATTRIBUTES     = "integer_attributes"
    JSON_ATTRIBUTES        = "json_attributes"
    LIST_OBJECT_ATTRIBUTES = "list_object_attributes"
    MULTI_SELECT_ATTRIBUTES  = "multi_select_attributes"
    POLYGON_ATTRIBUTES     = "polygon_attributes"
    SINGLE_SELECT_ATTRIBUTES = "single_select_attributes"
    STRING_ATTRIBUTES      = "string_attributes"
    TABLE_ATTRIBUTES       = "table_attributes"
    TIME_ATTRIBUTES        = "time_attributes"
```

### Extracting multiple attributes

Pass multiple `Attribute` objects in a single call — they are extracted in one LLM shot, which is more efficient than calling the endpoint once per attribute:

```python
attributes=[
    Attribute(name="contract_value", prompt="...", kind=AttributeType.STRING_ATTRIBUTES),
    Attribute(name="start_date",     prompt="...", kind=AttributeType.DATE_ATTRIBUTES),
    Attribute(name="is_signed",      prompt="...", kind=AttributeType.BOOLEAN_ATTRIBUTES),
]
```

---

## Step 4 — Find the created attribute ID

The response organises created attributes into typed lists. Find the ID for your attribute:

```python
def find_attribute_id(all_attrs_schema, name: str, kind: AttributeType) -> UUID | None:
    type_to_field = {
        AttributeType.STRING_ATTRIBUTES:     all_attrs_schema.string_attributes,
        AttributeType.INTEGER_ATTRIBUTES:    all_attrs_schema.integer_attributes,
        AttributeType.FLOAT_ATTRIBUTES:      all_attrs_schema.float_attributes,
        AttributeType.BOOLEAN_ATTRIBUTES:    all_attrs_schema.boolean_attributes,
        AttributeType.DATE_ATTRIBUTES:       all_attrs_schema.date_attributes,
        AttributeType.DATETIME_ATTRIBUTES:   all_attrs_schema.datetime_attributes,
        AttributeType.TIME_ATTRIBUTES:       all_attrs_schema.time_attributes,
        AttributeType.COORDINATE_ATTRIBUTES: all_attrs_schema.coordinate_attributes,
        AttributeType.POLYGON_ATTRIBUTES:    all_attrs_schema.polygon_attributes,
        AttributeType.TABLE_ATTRIBUTES:      all_attrs_schema.table_attributes,
        AttributeType.JSON_ATTRIBUTES:       all_attrs_schema.json_attributes,
    }
    for attr in type_to_field.get(kind, []):
        if attr.name == name and isinstance(attr.id, UUID):
            return attr.id
    return None

out = extraction_response.parsed
attribute_id = find_attribute_id(out.created, "contract_value", AttributeType.STRING_ATTRIBUTES)
if not attribute_id:
    # If the attribute already existed it appears in `updated`, not `created`
    attribute_id = find_attribute_id(out.updated, "contract_value", AttributeType.STRING_ATTRIBUTES)
```

---

## Step 5 — Poll for the result

Extraction runs asynchronously. Poll until a terminal status is reached.

```python
from tektome.endpoints.api.extraction import get_attribute_extraction_result
from tektome.endpoints.models.attribute_extraction_status_choices import AttributeExtractionStatusChoices
import time

TERMINAL = {
    AttributeExtractionStatusChoices.COMPLETED,
    AttributeExtractionStatusChoices.COMPLETED_NOT_FOUND,
    AttributeExtractionStatusChoices.FAILED,
    AttributeExtractionStatusChoices.CANCELLED,
    AttributeExtractionStatusChoices.PENDING_APPROVAL,   # expected when for_approval=True
}

while True:
    result = get_attribute_extraction_result.sync(attribute_id=attribute_id, client=client)
    if result and result.extraction_status in TERMINAL:
        break
    time.sleep(3)

print(result.value)     # the extracted value
print(result.reasoning) # the LLM's reasoning
```

### Terminal statuses

| Status | Meaning |
|---|---|
| `completed` | Value successfully extracted — check `result.value` |
| `completed_not_found` | Extraction ran fine but the answer is not in the document — `result.value` will be null. This is **not an error**. |
| `failed` | Extraction failed — check `result.error_message` |
| `cancelled` | Job was cancelled |
| `pending_approval` | Only occurs when `for_approval=True` — result awaits human approval before finalising |

`completed_not_found` is easy to conflate with failure. It means the LLM ran successfully but determined the document does not contain the requested information.

---

## Step 6 — Create an approval ticket

Submit the extracted attribute for approval. Use the `attribute_id` from Step 4 directly — when the attribute name matches an existing dataspace attribute config, the extraction already persisted the value and citations to the dataspace, so no separate upload or citation step is needed.

Fetch the attribute first to resolve its server-side type for `CandidateItemKind`.

```python
from tektome.endpoints.api.dataspace import get_general_dataspace_attribute
from tektome.endpoints.api.dataspace_approval_tickets import (
    create_execution_approval_ticket_with_candidates,
)
from tektome.endpoints.models import (
    ApprovalCategoryTypes,
    AttributeCandidatePayload,
    CandidateItem,
    CandidateItemKind,
    CreateApprovalTicketRequest,
    CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
    GetGeneralDataspaceAttributeDataspaceEntityType,
)

attr_response = get_general_dataspace_attribute.sync_detailed(
    dataspace_id=context.system_dataspace_id,
    attribute_category=GetGeneralDataspaceAttributeDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,     # from Step 4
    client=client,
)
kind = CandidateItemKind(attr_response.parsed.type_)

ticket_response = create_execution_approval_ticket_with_candidates.sync_detailed(
    client=client,
    dataspace_id=context.system_dataspace_id,
    execution_id=context.system_execution_id,
    body=CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams(
        payload=CreateApprovalTicketRequest(
            category=ApprovalCategoryTypes.ATTRIBUTE_UPDATE,
            candidates=[
                CandidateItem(
                    data=AttributeCandidatePayload(
                        attribute_id=attribute_id,
                        resource_id=context.system_resource_id,
                    ),
                    kind=kind,
                )
            ],
        )
    ),
)
# ticket_response.status_code should be 201
```

The attribute must have `extraction_status=PENDING_APPROVAL`, which requires `for_approval=True` in Step 3.

For project flows, use `GetGeneralDataspaceAttributeDataspaceEntityType.PROJECT` and pass `project_id=context.system_project_id` instead of `resource_id` in `AttributeCandidatePayload`.

---

## Common errors

| Error | Cause |
|---|---|
| `400` on `POST /api/core/sections/` | `project_id` is wrong or inaccessible, or `page_ids` is empty |
| `422` on `POST /api/core/extractions/attributes/` | Invalid recipe (only `v1` / `table_v1` allowed), attribute name violates naming rules, or `section_id` doesn't exist |
| Pages list is empty | Resource has not been OCR-processed — run OCR first |
| Attribute ID not found in response | Wrong `kind` passed — check `created` and `updated` in the response |

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

#### `extract_attribute_approval_ticket`

Runs an attribute extraction against a section, polls until each extracted attribute is ready, then creates one approval ticket per non-reserved attribute.

```python
from uuid import UUID

from tektome import Context
from tektome.endpoints.models import Attribute, AttributeType
from tektome.shortcuts.extract_attribute_approval_ticket import (
    extract_attribute_approval_ticket,
)

def main(ctx: Context, section_id: UUID):
    attributes = [
        Attribute(
            name="title",
            prompt="Extract the document title",
            kind=AttributeType.STRING_ATTRIBUTES,
        )
    ]

    with ctx.client() as client:
        responses = extract_attribute_approval_ticket(
            client,
            ctx,
            section_id,
            attributes,
            prompt="Extract the requested attributes from this section.",
        )
        print(f"Created {len(responses)} approval tickets")
```


## Full working example

See `script_tests/extract_resource_attribute.py` for a complete runnable script.
Prioritize shortcuts, but refer to the full flow in this document if you need more control or want to understand the underlying calls.
