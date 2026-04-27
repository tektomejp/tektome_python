"""Test suite for create_attribute_approval_ticket shortcut."""

import uuid
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from tektome.endpoints.models import (
    ApprovalCategoryTypes,
    AttributeType,
    CandidateItemKind,
    PostGeneralDataspaceAttributeDataspaceEntityType,
)
from tektome.shortcuts.create_attribute_approval_ticket import (
    AttributeConfig,
    AttributePayload,
    create_attribute_approval_ticket,
)

POST_PATH = (
    "tektome.shortcuts.create_attribute_approval_ticket"
    ".post_general_dataspace_attribute.sync_detailed"
)
CREATE_TICKET_PATH = (
    "tektome.shortcuts.create_attribute_approval_ticket"
    ".create_execution_approval_ticket_with_candidates.sync_detailed"
)


def _make_payload(name, type_, value):
    return AttributePayload(
        attribute_config=AttributeConfig(attribute_name=name, attribute_type=type_),
        value=value,
    )


def _make_post_response(parsed):
    return SimpleNamespace(parsed=parsed)


class TestCreateAttributeApprovalTicketHappyPath:
    def test_creates_single_attribute_and_approval_ticket(
        self, client, context, dataspace_id, resource_id, execution_id
    ):
        attr_id = uuid.uuid4()
        payload = _make_payload("title", AttributeType.STRING_ATTRIBUTES, "hello")
        ticket_response = SimpleNamespace(parsed=SimpleNamespace())

        with (
            patch(POST_PATH) as mock_post,
            patch(CREATE_TICKET_PATH) as mock_ticket,
        ):
            mock_post.return_value = _make_post_response(SimpleNamespace(id=attr_id))
            mock_ticket.return_value = ticket_response

            result = create_attribute_approval_ticket(client, context, [payload])

        assert result is ticket_response
        assert mock_post.call_count == 1
        post_kwargs = mock_post.call_args.kwargs
        assert (
            post_kwargs["attribute_category"]
            == PostGeneralDataspaceAttributeDataspaceEntityType.RESOURCE
        )
        assert post_kwargs["client"] is client
        assert post_kwargs["dataspace_id"] == dataspace_id
        body = post_kwargs["body"]
        assert body.name == "title"
        assert body.type_ == AttributeType.STRING_ATTRIBUTES
        assert body.value == "hello"
        assert body.entity_id == resource_id

        assert mock_ticket.call_count == 1
        ticket_kwargs = mock_ticket.call_args.kwargs
        assert ticket_kwargs["client"] is client
        assert ticket_kwargs["dataspace_id"] == dataspace_id
        assert ticket_kwargs["execution_id"] == execution_id
        ticket_payload = ticket_kwargs["body"].payload
        assert ticket_payload.category == ApprovalCategoryTypes.ATTRIBUTE_UPDATE
        assert len(ticket_payload.candidates) == 1
        candidate = ticket_payload.candidates[0]
        assert candidate.data.attribute_id == attr_id
        assert candidate.data.resource_id == resource_id
        assert candidate.kind == CandidateItemKind.CREATE_UPDATE_STRING_ATTRIBUTES

    def test_creates_multiple_attributes_in_one_ticket(
        self, client, context, dataspace_id, resource_id, execution_id
    ):
        attr_ids = [uuid.uuid4() for _ in range(3)]
        payloads = [
            _make_payload("a1", AttributeType.STRING_ATTRIBUTES, "v1"),
            _make_payload("a2", AttributeType.STRING_ATTRIBUTES, "v2"),
            _make_payload("a3", AttributeType.STRING_ATTRIBUTES, "v3"),
        ]
        ticket_response = SimpleNamespace(parsed=SimpleNamespace())

        with (
            patch(POST_PATH) as mock_post,
            patch(CREATE_TICKET_PATH) as mock_ticket,
        ):
            mock_post.side_effect = [
                _make_post_response(SimpleNamespace(id=attr_id)) for attr_id in attr_ids
            ]
            mock_ticket.return_value = ticket_response

            result = create_attribute_approval_ticket(client, context, payloads)

        assert result is ticket_response
        assert mock_post.call_count == 3
        for call, payload in zip(mock_post.call_args_list, payloads):
            body = call.kwargs["body"]
            assert body.name == payload.attribute_config.attribute_name
            assert body.type_ == AttributeType.STRING_ATTRIBUTES
            assert body.value == payload.value
            assert body.entity_id == resource_id

        assert mock_ticket.call_count == 1
        ticket_payload = mock_ticket.call_args.kwargs["body"].payload
        assert ticket_payload.category == ApprovalCategoryTypes.ATTRIBUTE_UPDATE
        assert [c.data.attribute_id for c in ticket_payload.candidates] == attr_ids
        assert all(c.data.resource_id == resource_id for c in ticket_payload.candidates)
        assert all(
            c.kind == CandidateItemKind.CREATE_UPDATE_STRING_ATTRIBUTES
            for c in ticket_payload.candidates
        )


class TestCreateAttributeApprovalTicketValidation:
    def test_raises_on_attribute_type_mismatch(self, client, context):
        payloads = [
            _make_payload("a1", AttributeType.STRING_ATTRIBUTES, "v1"),
            _make_payload("a2", AttributeType.INTEGER_ATTRIBUTES, 1),
        ]

        with (
            patch(POST_PATH) as mock_post,
            patch(CREATE_TICKET_PATH) as mock_ticket,
        ):
            with pytest.raises(ValueError, match="Attribute type mismatch"):
                create_attribute_approval_ticket(client, context, payloads)

            mock_post.assert_not_called()
            mock_ticket.assert_not_called()


class TestCreateAttributeApprovalTicketCandidateSkipping:
    def test_skips_candidate_when_post_response_unparsed(
        self, client, context, resource_id
    ):
        attr_ids = [uuid.uuid4(), uuid.uuid4()]
        payloads = [
            _make_payload("a1", AttributeType.STRING_ATTRIBUTES, "v1"),
            _make_payload("a2", AttributeType.STRING_ATTRIBUTES, "v2"),
            _make_payload("a3", AttributeType.STRING_ATTRIBUTES, "v3"),
        ]

        with (
            patch(POST_PATH) as mock_post,
            patch(CREATE_TICKET_PATH) as mock_ticket,
        ):
            mock_post.side_effect = [
                _make_post_response(SimpleNamespace(id=attr_ids[0])),
                _make_post_response(None),
                _make_post_response(SimpleNamespace(id=attr_ids[1])),
            ]
            mock_ticket.return_value = SimpleNamespace(parsed=SimpleNamespace())

            create_attribute_approval_ticket(client, context, payloads)

        assert mock_post.call_count == 3
        assert mock_ticket.call_count == 1
        ticket_payload = mock_ticket.call_args.kwargs["body"].payload
        assert [c.data.attribute_id for c in ticket_payload.candidates] == attr_ids
        assert all(c.data.resource_id == resource_id for c in ticket_payload.candidates)

    def test_creates_empty_ticket_when_all_post_responses_unparsed(
        self, client, context
    ):
        payloads = [
            _make_payload("a1", AttributeType.STRING_ATTRIBUTES, "v1"),
            _make_payload("a2", AttributeType.STRING_ATTRIBUTES, "v2"),
        ]

        with (
            patch(POST_PATH) as mock_post,
            patch(CREATE_TICKET_PATH) as mock_ticket,
        ):
            mock_post.side_effect = [
                _make_post_response(None),
                _make_post_response(None),
            ]
            mock_ticket.return_value = SimpleNamespace(parsed=SimpleNamespace())

            create_attribute_approval_ticket(client, context, payloads)

        assert mock_post.call_count == 2
        assert mock_ticket.call_count == 1
        ticket_payload = mock_ticket.call_args.kwargs["body"].payload
        assert ticket_payload.candidates == []
