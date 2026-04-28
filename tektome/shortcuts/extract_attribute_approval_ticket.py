import time
from typing import Any
from uuid import UUID

from pydantic import BaseModel

from tektome import Context
from tektome.constants import RESERVED_ATTRIBUTES
from tektome.endpoints import AuthenticatedClient, Client
from tektome.endpoints.api.dataspace import get_general_dataspace_attribute
from tektome.endpoints.api.dataspace_approval_tickets import (
    create_execution_approval_ticket_with_candidates,
)
from tektome.endpoints.api.extraction import create_attribute_extraction
from tektome.endpoints.models import (
    RECIPESCHOICES,
    AllAttributesSchemaResponse,
    ApprovalCategoryTypes,
    Attribute,
    AttributeCandidatePayload,
    AttributeType,
    CandidateItem,
    CandidateItemKind,
    CreateApprovalTicketRequest,
    CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
    CreateExtractionRequest,
    GetGeneralDataspaceAttributeDataspaceEntityType,
)


class AttributeConfig(BaseModel):
    attribute_name: str
    attribute_type: AttributeType


class AttributePayload(BaseModel):
    attribute_config: AttributeConfig
    value: Any
    citations: dict


def collect_attr_info(
    attrs_container: AllAttributesSchemaResponse,
) -> list[tuple[UUID, str, str]]:
    """
    Collects attribute information from attribute extraction response

    Args:
        attrs_container: AttributeExtractionResponse from attribute extraction response

    Returns: list of attribute information
    """
    attr_info = []

    for attribute_type in AttributeType:
        if attribute_type == AttributeType.LIST_OBJECT_ATTRIBUTES:
            # Skip unsupported for now
            continue

        attributes = getattr(attrs_container, attribute_type.value)
        for item in attributes:
            if item.name in RESERVED_ATTRIBUTES:
                continue
            attr_info.append((item.id, item.name, attribute_type.value))

    return attr_info


def extract_attribute_approval_ticket(
    client: AuthenticatedClient | Client,
    context: Context,
    section_id: UUID,
    attributes: list[Attribute],
    prompt: str,
):
    """
    Helper function to perform the following operations

    1. perform POST extractions call
    2. Create approval tickets from the extracted attributes

    Returns:
    """
    extraction_response = create_attribute_extraction.sync_detailed(
        client=client,
        body=CreateExtractionRequest(
            section_id=section_id,
            recipe=RECIPESCHOICES.V1,
            attributes=attributes,
            enduser_prompt=prompt,
            for_approval=True,
        ),
    )
    parsed_response = extraction_response.parsed

    if not parsed_response:
        print("Failed:", extraction_response)
        raise ValueError("Extraction failed, no response received")

    all_attrs = collect_attr_info(parsed_response.created) + collect_attr_info(
        parsed_response.updated
    )

    # Wait for all approval tickets to be extracted
    max_attempts = 60
    poll_attrs = all_attrs.copy()
    attempts = 0
    while poll_attrs:
        if attempts >= max_attempts:
            raise TimeoutError(
                f"Extraction did not complete after {max_attempts} attempts; "
                f"pending attributes: {poll_attrs}"
            )

        attr_id = poll_attrs[-1]
        r = get_general_dataspace_attribute.sync_detailed(
            client=client,
            attribute_id=attr_id[0],
            attribute_category=GetGeneralDataspaceAttributeDataspaceEntityType.RESOURCE,
            dataspace_id=context.system_dataspace_id,
        )

        if r.parsed.extraction_status in {"pending_approval", "completed"}:
            poll_attrs.remove(attr_id)
        else:
            print("Waiting for extraction to complete...", attr_id)
            time.sleep(5)
            attempts += 1

    # Create approval tickets
    responses = []
    for attr_id, attr_name, attr_type in all_attrs:
        response = create_execution_approval_ticket_with_candidates.sync_detailed(
            client=client,
            dataspace_id=context.system_dataspace_id,
            execution_id=context.system_execution_id,
            body=CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams(
                payload=CreateApprovalTicketRequest(
                    category=ApprovalCategoryTypes.ATTRIBUTE_UPDATE,
                    candidates=[
                        CandidateItem(
                            data=AttributeCandidatePayload(
                                attribute_id=attr_id,
                                resource_id=context.system_resource_id,
                            ),
                            kind=CandidateItemKind(attr_type),
                        )
                    ],
                )
            ),
        )
        responses.append(response)

    return responses
