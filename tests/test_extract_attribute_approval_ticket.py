"""Test suite for extract_attribute_approval_ticket shortcut."""

import uuid
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from tektome.endpoints.models import (
    RECIPESCHOICES,
    ApprovalCategoryTypes,
    Attribute,
    AttributeType,
    CandidateItemKind,
    GetGeneralDataspaceAttributeDataspaceEntityType,
)
from tektome.shortcuts.extract_attribute_approval_ticket import (
    collect_attr_info,
    extract_attribute_approval_ticket,
)

EXTRACT_PATH = (
    "tektome.shortcuts.extract_attribute_approval_ticket"
    ".create_attribute_extraction.sync_detailed"
)
GET_ATTR_PATH = (
    "tektome.shortcuts.extract_attribute_approval_ticket"
    ".get_general_dataspace_attribute.sync_detailed"
)
CREATE_TICKET_PATH = (
    "tektome.shortcuts.extract_attribute_approval_ticket"
    ".create_execution_approval_ticket_with_candidates.sync_detailed"
)
SLEEP_PATH = "tektome.shortcuts.extract_attribute_approval_ticket.time.sleep"


def _make_attrs_container(**attrs_by_type):
    """Build an AllAttributesSchemaResponse-shaped container.

    attrs_by_type maps an AttributeType.value to a list of (id, name) tuples.
    Any AttributeType not provided defaults to an empty list.
    """
    container = SimpleNamespace()
    for attr_type in AttributeType:
        items = [
            SimpleNamespace(id=item_id, name=item_name)
            for item_id, item_name in attrs_by_type.get(attr_type.value, [])
        ]
        setattr(container, attr_type.value, items)
    return container


def _make_get_attr_response(status):
    return SimpleNamespace(parsed=SimpleNamespace(extraction_status=status))


def _make_attribute(name, kind):
    return Attribute(name=name, prompt=f"prompt for {name}", kind=kind)


class TestCollectAttrInfo:
    def test_returns_empty_for_empty_container(self):
        container = _make_attrs_container()
        assert collect_attr_info(container) == []

    def test_filters_reserved_attribute_names(self):
        kind = AttributeType.STRING_ATTRIBUTES.value
        container = _make_attrs_container(
            **{
                kind: [
                    (uuid.uuid4(), "kind"),
                    (uuid.uuid4(), "created"),
                    (uuid.uuid4(), "created_by"),
                    (uuid.uuid4(), "updated"),
                    (uuid.uuid4(), "updated_by"),
                ]
            }
        )
        assert collect_attr_info(container) == []

    def test_returns_only_non_reserved_when_mixed(self):
        kind = AttributeType.STRING_ATTRIBUTES.value
        keep_id = uuid.uuid4()
        skip_id = uuid.uuid4()
        container = _make_attrs_container(
            **{kind: [(keep_id, "title"), (skip_id, "kind")]}
        )
        result = collect_attr_info(container)
        assert result == [(keep_id, "title", kind)]

    def test_collects_across_multiple_attribute_types(self):
        string_id = uuid.uuid4()
        int_id = uuid.uuid4()
        date_id = uuid.uuid4()
        container = _make_attrs_container(
            **{
                AttributeType.STRING_ATTRIBUTES.value: [(string_id, "title")],
                AttributeType.INTEGER_ATTRIBUTES.value: [(int_id, "count")],
                AttributeType.DATE_ATTRIBUTES.value: [(date_id, "due")],
            }
        )
        result = collect_attr_info(container)
        assert (string_id, "title", AttributeType.STRING_ATTRIBUTES.value) in result
        assert (int_id, "count", AttributeType.INTEGER_ATTRIBUTES.value) in result
        assert (date_id, "due", AttributeType.DATE_ATTRIBUTES.value) in result
        assert len(result) == 3


class TestExtractAttributeApprovalTicketHappyPath:
    def test_creates_tickets_for_all_extracted_attributes(
        self, client, context, dataspace_id, resource_id, execution_id
    ):
        section_id = uuid.uuid4()
        prompt = "Extract attributes"
        input_attrs = [_make_attribute("title", AttributeType.STRING_ATTRIBUTES)]

        created_string_id = uuid.uuid4()
        updated_int_id = uuid.uuid4()
        parsed_response = SimpleNamespace(
            created=_make_attrs_container(
                **{
                    AttributeType.STRING_ATTRIBUTES.value: [
                        (created_string_id, "title")
                    ]
                }
            ),
            updated=_make_attrs_container(
                **{
                    AttributeType.INTEGER_ATTRIBUTES.value: [(updated_int_id, "count")]
                }
            ),
        )

        with (
            patch(EXTRACT_PATH) as mock_extract,
            patch(GET_ATTR_PATH) as mock_get,
            patch(CREATE_TICKET_PATH) as mock_ticket,
            patch(SLEEP_PATH) as mock_sleep,
        ):
            mock_extract.return_value = SimpleNamespace(parsed=parsed_response)
            mock_get.return_value = _make_get_attr_response("completed")
            mock_ticket.side_effect = [
                SimpleNamespace(parsed="ticket1"),
                SimpleNamespace(parsed="ticket2"),
            ]

            results = extract_attribute_approval_ticket(
                client, context, section_id, input_attrs, prompt
            )

        assert mock_extract.call_count == 1
        extract_kwargs = mock_extract.call_args.kwargs
        assert extract_kwargs["client"] is client
        extract_body = extract_kwargs["body"]
        assert extract_body.section_id == section_id
        assert extract_body.recipe == RECIPESCHOICES.V1
        assert extract_body.attributes == input_attrs
        assert extract_body.enduser_prompt == prompt
        assert extract_body.for_approval is True

        assert mock_get.call_count == 2
        for call in mock_get.call_args_list:
            assert call.kwargs["client"] is client
            assert (
                call.kwargs["attribute_category"]
                == GetGeneralDataspaceAttributeDataspaceEntityType.RESOURCE
            )
            assert call.kwargs["dataspace_id"] == dataspace_id
        polled_ids = {call.kwargs["attribute_id"] for call in mock_get.call_args_list}
        assert polled_ids == {created_string_id, updated_int_id}

        mock_sleep.assert_not_called()

        assert mock_ticket.call_count == 2
        ticketed_pairs = []
        for call in mock_ticket.call_args_list:
            assert call.kwargs["client"] is client
            assert call.kwargs["dataspace_id"] == dataspace_id
            assert call.kwargs["execution_id"] == execution_id
            payload = call.kwargs["body"].payload
            assert payload.category == ApprovalCategoryTypes.ATTRIBUTE_UPDATE
            assert len(payload.candidates) == 1
            candidate = payload.candidates[0]
            assert candidate.data.resource_id == resource_id
            ticketed_pairs.append((candidate.data.attribute_id, candidate.kind))

        assert (
            created_string_id,
            CandidateItemKind.CREATE_UPDATE_STRING_ATTRIBUTES,
        ) in ticketed_pairs
        assert (
            updated_int_id,
            CandidateItemKind.CREATE_UPDATE_INTEGER_ATTRIBUTES,
        ) in ticketed_pairs

        assert results == [
            SimpleNamespace(parsed="ticket1"),
            SimpleNamespace(parsed="ticket2"),
        ]


class TestExtractAttributeApprovalTicketExtractionFailure:
    def test_raises_when_extraction_response_unparsed(self, client, context):
        section_id = uuid.uuid4()

        with (
            patch(EXTRACT_PATH) as mock_extract,
            patch(GET_ATTR_PATH) as mock_get,
            patch(CREATE_TICKET_PATH) as mock_ticket,
            patch(SLEEP_PATH) as mock_sleep,
        ):
            mock_extract.return_value = SimpleNamespace(parsed=None)

            with pytest.raises(
                ValueError, match="Extraction failed, no response received"
            ):
                extract_attribute_approval_ticket(
                    client, context, section_id, [], "prompt"
                )

            mock_get.assert_not_called()
            mock_ticket.assert_not_called()
            mock_sleep.assert_not_called()


class TestExtractAttributeApprovalTicketPolling:
    @pytest.mark.parametrize("terminal_status", ["pending_approval", "completed"])
    def test_terminal_status_short_circuits_loop(
        self, client, context, terminal_status
    ):
        section_id = uuid.uuid4()
        attr_id = uuid.uuid4()
        parsed_response = SimpleNamespace(
            created=_make_attrs_container(
                **{AttributeType.STRING_ATTRIBUTES.value: [(attr_id, "title")]}
            ),
            updated=_make_attrs_container(),
        )

        with (
            patch(EXTRACT_PATH) as mock_extract,
            patch(GET_ATTR_PATH) as mock_get,
            patch(CREATE_TICKET_PATH) as mock_ticket,
            patch(SLEEP_PATH) as mock_sleep,
        ):
            mock_extract.return_value = SimpleNamespace(parsed=parsed_response)
            mock_get.return_value = _make_get_attr_response(terminal_status)
            mock_ticket.return_value = SimpleNamespace(parsed=SimpleNamespace())

            extract_attribute_approval_ticket(
                client, context, section_id, [], "prompt"
            )

        assert mock_get.call_count == 1
        mock_sleep.assert_not_called()
        assert mock_ticket.call_count == 1

    def test_polling_retries_when_status_non_terminal(self, client, context):
        section_id = uuid.uuid4()
        attr_id = uuid.uuid4()
        parsed_response = SimpleNamespace(
            created=_make_attrs_container(
                **{AttributeType.STRING_ATTRIBUTES.value: [(attr_id, "title")]}
            ),
            updated=_make_attrs_container(),
        )

        with (
            patch(EXTRACT_PATH) as mock_extract,
            patch(GET_ATTR_PATH) as mock_get,
            patch(CREATE_TICKET_PATH) as mock_ticket,
            patch(SLEEP_PATH) as mock_sleep,
        ):
            mock_extract.return_value = SimpleNamespace(parsed=parsed_response)
            mock_get.side_effect = [
                _make_get_attr_response("pending"),
                _make_get_attr_response("completed"),
            ]
            mock_ticket.return_value = SimpleNamespace(parsed=SimpleNamespace())

            extract_attribute_approval_ticket(
                client, context, section_id, [], "prompt"
            )

        assert mock_get.call_count == 2
        assert mock_sleep.call_count == 1
        mock_sleep.assert_called_once_with(5)
        assert mock_ticket.call_count == 1


class TestExtractAttributeApprovalTicketReservedFiltering:
    def test_all_reserved_attributes_skip_polling_and_tickets(self, client, context):
        section_id = uuid.uuid4()
        parsed_response = SimpleNamespace(
            created=_make_attrs_container(
                **{
                    AttributeType.STRING_ATTRIBUTES.value: [
                        (uuid.uuid4(), "kind"),
                        (uuid.uuid4(), "created"),
                    ]
                }
            ),
            updated=_make_attrs_container(
                **{
                    AttributeType.STRING_ATTRIBUTES.value: [
                        (uuid.uuid4(), "updated"),
                    ]
                }
            ),
        )

        with (
            patch(EXTRACT_PATH) as mock_extract,
            patch(GET_ATTR_PATH) as mock_get,
            patch(CREATE_TICKET_PATH) as mock_ticket,
            patch(SLEEP_PATH) as mock_sleep,
        ):
            mock_extract.return_value = SimpleNamespace(parsed=parsed_response)

            results = extract_attribute_approval_ticket(
                client, context, section_id, [], "prompt"
            )

        mock_get.assert_not_called()
        mock_ticket.assert_not_called()
        mock_sleep.assert_not_called()
        assert results == []
