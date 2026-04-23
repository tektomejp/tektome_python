# PDF Data and Tools — Agent Reference

This document explains how to upload, process, and work with PDF documents using the Tektome Python SDK. It covers file upload, OCR text extraction, page retrieval, document search, and the PDF citation system.

---

## Overview

PDF handling in Tektome follows a pipeline:

```
upload file → (auto or manual) OCR extraction → pages available → search / cite
```

Once a PDF is uploaded as a resource and OCR-processed, its text content becomes available page-by-page, searchable via document search, and citable via PDF citations on attributes.

Key concepts:
- **Resource** — the uploaded file record (PDF, DOCX, IFC, image, etc.)
- **OCR extraction** — Azure Document Intelligence processes the PDF into structured text with positional data
- **Page components** — individual page records with IDs, used for sections and citations
- **Sections** — groups of pages used as extraction context (for LLM attribute extraction)
- **PDF citations** — link an attribute value back to a specific PDF resource, optionally with polygon annotations marking the source region

---

## Step 1 — Upload a PDF file

There are three upload methods depending on context and file size.

### 1a. Direct upload to a dataspace project

For standard-size files (under ~500MB):

```python
from tektome.endpoints.api.dataspace import upload_dataspace_project_file
from tektome.endpoints.models.upload_dataspace_project_file_multi_part_body_params import (
    UploadDataspaceProjectFileMultiPartBodyParams,
)
from tektome.endpoints.models.dataspace_resource_upload_request import DataspaceResourceUploadRequest
from tektome.endpoints.types import File

resp = upload_dataspace_project_file.sync_detailed(
    project_id=project_uuid,
    client=client,
    body=UploadDataspaceProjectFileMultiPartBodyParams(
        file=File(payload=open("document.pdf", "rb")),
        payload=DataspaceResourceUploadRequest(initialize=True),
    ),
)
if resp.status_code.value != 201:
    raise RuntimeError(f"Upload failed: {resp.status_code.value} {resp.content.decode()}")

resource = resp.parsed
resource_id = resource.id
```

This endpoint automatically detects the file type and may trigger OCR extraction or BIM conversion depending on the file extension.

### 1b. Blob upload for large files (500MB+)

Large files use a two-phase flow: request a signed upload URL, upload directly to storage, then finalise.

**Phase 1 — Request upload URL:**

```python
from tektome.endpoints.api.resource import request_appresource_blob_upload
from tektome.endpoints.models.blob_upload_request import BlobUploadRequest

blob_resp = request_appresource_blob_upload.sync(
    project_id=project_uuid,
    client=client,
    body=BlobUploadRequest(file_name="large-document.pdf"),
)
upload_url = blob_resp.upload_url   # write-only signed URL, expires in 15 minutes
upload_id = blob_resp.upload_id     # needed for finalisation
```

**Phase 2 — Upload directly to storage:**

```python
import httpx

with open("large-document.pdf", "rb") as f:
    httpx.put(upload_url, content=f.read(), headers={"x-ms-blob-type": "BlockBlob"})
```

**Phase 3 — Finalise:**

```python
from tektome.endpoints.api.resource import complete_appresource_blob_upload
from tektome.endpoints.models.blob_upload_complete_request import BlobUploadCompleteRequest

complete_resp = complete_appresource_blob_upload.sync_detailed(
    project_id=project_uuid,
    client=client,
    body=BlobUploadCompleteRequest(upload_id=upload_id),
)
resource_id = complete_resp.parsed.resource_id
```

### 1c. Upload via signed URL (async)

```python
from tektome.endpoints.api.dataspace import upload_dataspace_project_signed_url
from tektome.endpoints.models.resource_create_from_signed_url_request import ResourceCreateFromSignedUrlRequest

resp = upload_dataspace_project_signed_url.sync_detailed(
    project_id=project_uuid,
    client=client,
    body=ResourceCreateFromSignedUrlRequest(
        url="https://storage.blob.core.windows.net/...",
        resource_id=resource_uuid,
    ),
)
task_id = resp.parsed.task_id  # async — poll with get_celery_task
```

---

## Step 2 — Trigger OCR extraction

OCR may be triggered automatically on upload (depending on platform config), or manually:

```python
from tektome.endpoints.api.resource import initialize_lawtalk_resource_ocr

ocr_resp = initialize_lawtalk_resource_ocr.sync_detailed(
    resource_id=str(resource_uuid),
    client=client,
)
if ocr_resp.status_code.value != 201:
    raise RuntimeError(f"OCR init failed: {ocr_resp.status_code.value} {ocr_resp.content.decode()}")

task_id = ocr_resp.parsed.task_id
```

This is an **async operation**. The OCR is performed by Azure Document Intelligence (Azure Form Recognizer) and may take seconds to minutes depending on document length.

### Check OCR status

```python
from tektome.endpoints.api.resource import get_lawtalk_resource_init_status

status = get_lawtalk_resource_init_status.sync(
    resource_id=str(resource_uuid),
    client=client,
)
```

### Get OCR data

Once complete, retrieve the OCR extraction result:

```python
from tektome.endpoints.api.dataspace import get_dataspace_resource_ocr

ocr_data = get_dataspace_resource_ocr.sync_detailed(
    resource_id=resource_uuid,
    client=client,
)
```

---

## Step 3 — List pages

After OCR processing, pages are available as individual components. Page IDs are required for creating sections (used in LLM attribute extraction) and for PDF citation polygon annotations.

```python
from tektome.endpoints.api.page import list_resource_pages
from uuid import UUID

pages = list_resource_pages.sync(resource_id=resource_uuid, client=client)
page_ids = [p.id for p in pages if isinstance(p.id, UUID)]
```

**If `page_ids` is empty**, the resource has not been OCR-processed yet. Either trigger OCR manually (Step 2) or wait for automatic processing to complete.

### Get a specific page

```python
from tektome.endpoints.api.page import get_resource_page

page = get_resource_page.sync(
    resource_id=resource_uuid,
    page_num=1,
    client=client,
)
```

### Get extracted text for a page

```python
from tektome.endpoints.api.resource import get_lawtalk_resource_initialized_page

page_data = get_lawtalk_resource_initialized_page.sync(
    resource_id=str(resource_uuid),
    page_num=1,
    client=client,
)
```

Returns the OCR-extracted data for that page, including positional text information.

---

## Step 4 — Create a section (for LLM extraction)

Sections group pages together as context for LLM-based attribute extraction. Required before calling `create_attribute_extraction`.

```python
from tektome.endpoints.api.section import create_core_section
from tektome.endpoints.models.create_section_creation_request import CreateSectionCreationRequest

section_resp = create_core_section.sync_detailed(
    client=client,
    body=CreateSectionCreationRequest(
        project_id=project_uuid,
        page_ids=page_ids,
    ),
)
section_id = section_resp.parsed.id
```

| Field | Usage |
|---|---|
| `page_ids` | Use for PDF page content |
| `resource_ids` | Reserved for **images only** — do not pass PDF resource IDs here |
| `project_id` | Required — must be the project the resource belongs to |

See [ATTRIBUTE_EXTRACTION.md](ATTRIBUTE_EXTRACTION.md) for the complete extraction workflow.

---

## Step 5 — Search documents

Search across all indexed documents in the system:

```python
from tektome.endpoints.api.search import search_documents
from tektome.endpoints.models.search_document_request import SearchDocumentRequest

from tektome.endpoints.models.azure_embedding_model import AzureEmbeddingModel

results = search_documents.sync_detailed(
    client=client,
    body=SearchDocumentRequest(
        embedding_model=AzureEmbeddingModel.AZURE_TEXT_EMBEDDING_3_LARGE,
        query_content="structural design criteria",
    ),
)
```

Returns ranked results based on relevance. Documents are indexed in Azure Search after OCR extraction completes.

---

## Step 6 — Create PDF citations

PDF citations link an attribute's value back to a specific PDF resource, optionally highlighting the source region with polygon annotations.

### Basic PDF citation (no polygon)

```python
from tektome.endpoints.api.dataspace_attributes_citations import create_attribute_pdf_citation
from tektome.endpoints.models.create_pdf_citation_request import CreatePDFCitationRequest
from tektome.endpoints.models.attribute_type import AttributeType
from tektome.endpoints.models.create_attribute_pdf_citation_dataspace_entity_type import (
    CreateAttributePdfCitationDataspaceEntityType,
)

resp = create_attribute_pdf_citation.sync_detailed(
    dataspace_id=dataspace_uuid,
    attribute_category=CreateAttributePdfCitationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,
    client=client,
    body=CreatePDFCitationRequest(
        title="Section 4.2",
        attribute_type=AttributeType.STRING_ATTRIBUTES,
        resource_id=pdf_resource_uuid,
        keywords=["design", "criteria"],
    ),
)
if resp.status_code.value != 201:
    raise RuntimeError(f"PDF citation failed: {resp.content.decode()}")
```

### PDF citation with polygon annotations

Polygon annotations mark specific regions on PDF pages. Create the citation first, then add polygon annotations:

```python
pdf_citation_id = resp.parsed.id

from tektome.endpoints.api.dataspace_attributes_citations import post_pdf_citation_polygon_annotation
from tektome.endpoints.models.create_pdf_citation_polygon_annotation_request import (
    CreatePDFCitationPolygonAnnotationRequest,
)

from tektome.endpoints.models.post_pdf_citation_polygon_annotation_dataspace_entity_type import (
    PostPdfCitationPolygonAnnotationDataspaceEntityType,
)

annotation_resp = post_pdf_citation_polygon_annotation.sync_detailed(
    dataspace_id=dataspace_uuid,
    attribute_category=PostPdfCitationPolygonAnnotationDataspaceEntityType.RESOURCE,
    attribute_id=attribute_id,
    pdf_citation_id=pdf_citation_id,
    client=client,
    body=CreatePDFCitationPolygonAnnotationRequest(
        page_id=page_ids[0],                              # UUID of the specific page
        attribute_type=AttributeType.STRING_ATTRIBUTES,
        bounding_geometry=[[100.0, 200.0], [400.0, 200.0], [400.0, 350.0], [100.0, 350.0]],
    ),
)
```

`bounding_geometry` is a list of `[x, y]` coordinate pairs defining the polygon vertices on the page.

### Citation management

| Operation | Endpoint |
|---|---|
| Create PDF citation | `dataspace_attributes_citations.create_attribute_pdf_citation` |
| Get citation by ID | `dataspace_attributes_citations.get_attribute_pdf_citation` |
| Update citation | `dataspace_attributes_citations.update_attribute_pdf_citation` |
| Delete citation | `dataspace_attributes_citations.delete_attribute_pdf_citation` |
| Add polygon annotation | `dataspace_attributes_citations.post_pdf_citation_polygon_annotation` |
| List polygon annotations | `dataspace_attributes_citations.get_pdf_citation_polygon_annotation` |

See [MANUAL_ATTRIBUTES_AND_CITATIONS.md](MANUAL_ATTRIBUTES_AND_CITATIONS.md) for the full attribute creation and citation workflow.

---

## DOCX handling

DOCX files uploaded to the platform are automatically converted to PDF via Gotenberg (LibreOffice-based conversion). After conversion:
1. The derived PDF is stored as a `ResourceDerivedFile`
2. OCR extraction is automatically triggered on the converted PDF
3. The resource becomes searchable and citable like any other PDF

No special SDK handling is needed — upload a DOCX file the same way as a PDF.

---

## Key rules

| Rule | Detail |
|---|---|
| OCR must complete before pages are available | `list_resource_pages` returns empty until OCR finishes. Check status or poll |
| `page_ids` for PDFs, `resource_ids` for images | Do not pass PDF resource IDs in section `resource_ids` — it's for images only |
| Async operations need polling | OCR extraction and signed-URL uploads return task IDs. Poll with `get_celery_task` or `get_lawtalk_resource_init_status` |
| Blob upload URLs expire in 15 minutes | Complete the upload and call the finalise endpoint promptly |
| Blob upload URLs are write-only | They cannot be used to read or download files |
| Use `sync_detailed()` for citations | `sync()` silently returns error objects without raising — always check status codes |
| Citation `title` max 32 characters | The database column is `varchar(32)` — longer titles cause 400 errors |
| `resource_id` in PDF citations is the PDF resource | Not the BIM resource — use the UUID of the uploaded PDF file |
| Polygon coordinates are page-relative | `bounding_geometry` uses the page's coordinate system from OCR data |
| `overlay_html` is unsanitized | The `overlay_html` field on PDF citations accepts raw HTML (max 1MB) — it is not sanitized server-side |
| Document search requires indexed content | Documents are indexed after OCR completes. Searching before indexing returns no results |

---

## Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Trying to list pages before OCR completes | Empty `page_ids` list | Wait for OCR to finish — poll `get_lawtalk_resource_init_status` or check if pages exist |
| Passing PDF resource IDs in section `resource_ids` | Section creation fails or extraction returns wrong content | Use `page_ids` for PDF content, `resource_ids` is for images only |
| Not finalising blob uploads | Resource record never created despite file being in storage | Always call `complete_appresource_blob_upload` (or `complete_lawtalk_blob_upload`) after uploading to the signed URL |
| Using `sync()` for citation endpoints | Script appears to succeed but no citations created | Use `sync_detailed()` and check `resp.status_code.value == 201` |
| Searching documents immediately after upload | No search results | OCR and search indexing are async — wait for both to complete before searching |
| Using page numbers instead of page UUIDs in polygon annotations | 400 error on polygon creation | `page_id` must be the UUID from `list_resource_pages`, not the integer page number |
| Exceeding 32-char citation title | 400 error | Keep titles under 32 characters |
| Uploading DOCX and expecting immediate PDF availability | Pages not found | DOCX→PDF conversion is async — wait for conversion and OCR to complete |
| Not checking OCR task status | Proceeding with extraction on unprocessed resource | Poll `get_lawtalk_resource_init_status` until status indicates completion |

---

## Endpoint reference

| Operation | Endpoint function | Method |
|---|---|---|
| Upload file to project | `dataspace.upload_dataspace_project_file` | POST |
| Upload via signed URL | `dataspace.upload_dataspace_project_signed_url` | POST |
| Request blob upload URL | `resource.request_appresource_blob_upload` | POST |
| Complete blob upload | `resource.complete_appresource_blob_upload` | POST |
| Trigger OCR | `resource.initialize_lawtalk_resource_ocr` | POST |
| Check OCR status | `resource.get_lawtalk_resource_init_status` | GET |
| Get OCR data | `dataspace.get_dataspace_resource_ocr` | GET |
| List pages | `page.list_resource_pages` | GET |
| Get specific page | `page.get_resource_page` | GET |
| Get extracted page data | `resource.get_lawtalk_resource_initialized_page` | GET |
| Search documents | `search.search_documents` | POST |
| Create PDF citation | `dataspace_attributes_citations.create_attribute_pdf_citation` | POST |
| Get PDF citation | `dataspace_attributes_citations.get_attribute_pdf_citation` | GET |
| Update PDF citation | `dataspace_attributes_citations.update_attribute_pdf_citation` | PATCH |
| Delete PDF citation | `dataspace_attributes_citations.delete_attribute_pdf_citation` | DELETE |
| Add polygon annotation | `dataspace_attributes_citations.post_pdf_citation_polygon_annotation` | POST |
| List polygon annotations | `dataspace_attributes_citations.get_pdf_citation_polygon_annotation` | GET |
| Create section | `section.create_core_section` | POST |
