from typing import Any

from pydantic import BaseModel

from tektome import Context
from tektome.endpoints import AuthenticatedClient, Client
from tektome.endpoints.api.dataspace import post_general_dataspace_attribute
from tektome.endpoints.api.dataspace_approval_tickets import (
    create_execution_approval_ticket_with_candidates,
)
from tektome.endpoints.models import (
    ApprovalCategoryTypes,
    AttributeCandidatePayload,
    AttributeType,
    CandidateItem,
    CandidateItemKind,
    CreateApprovalTicketRequest,
    CreateAttributeRequest,
    CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams,
    PostGeneralDataspaceAttributeDataspaceEntityType,
)


class AttributeConfig(BaseModel):
    attribute_name: str
    attribute_type: AttributeType


class AttributePayload(BaseModel):
    attribute_config: AttributeConfig
    value: Any


def create_attribute_approval_ticket(
    client: AuthenticatedClient | Client,
    context: Context,
    attributes_payload: list[AttributePayload],
):
    """
    Helper function to create an attribute with approval tickets

    Args:
        client: Authenticated client
        context: Context object
        attributes_payload: list of AttributePayloads for a single approval ticket

    Returns: POST attribute response
    """
    # Validate each
    attr_type = attributes_payload[0].attribute_config.attribute_type
    for attr_payload in attributes_payload[1:]:
        if attr_payload.attribute_config.attribute_type != attr_type:
            raise ValueError("Attribute type mismatch")

    entity_id = (
        context.system_resource_id
        if context.system_resource_id
        else context.system_project_id
    )

    if not entity_id:
        raise ValueError(
            "Either system_resource_id or system_project_id must be provided in context for extraction"
        )

    # Build attribute candidate payload
    payload_candidates = []
    for attr_payload in attributes_payload:
        post_attr_data = post_general_dataspace_attribute.sync_detailed(
            attribute_category=PostGeneralDataspaceAttributeDataspaceEntityType.RESOURCE,
            client=client,
            dataspace_id=context.system_dataspace_id,
            body=CreateAttributeRequest(
                name=attr_payload.attribute_config.attribute_name,
                type_=attr_payload.attribute_config.attribute_type,
                value=attr_payload.value,
                entity_id=entity_id,
            ),
        )

        if attr_data := post_attr_data.parsed:
            payload_candidates.append(
                CandidateItem(
                    data=AttributeCandidatePayload(
                        attribute_id=attr_data.id,
                        resource_id=entity_id,
                    ),
                    kind=CandidateItemKind(
                        attr_payload.attribute_config.attribute_type
                    ),
                )
            )

    # Create approval ticket with candidates
    response = create_execution_approval_ticket_with_candidates.sync_detailed(
        client=client,
        dataspace_id=context.system_dataspace_id,
        execution_id=context.system_execution_id,
        body=CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams(
            payload=CreateApprovalTicketRequest(
                category=ApprovalCategoryTypes.ATTRIBUTE_UPDATE,
                candidates=payload_candidates,
            )
        ),
    )

    return response
