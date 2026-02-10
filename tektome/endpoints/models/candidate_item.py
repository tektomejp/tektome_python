from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.candidate_item_kind import CandidateItemKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_attribute_candidate_payload import BooleanAttributeCandidatePayload
    from ..models.candidate_citation import CandidateCitation
    from ..models.candidate_item_data_type_1 import CandidateItemDataType1
    from ..models.float_attribute_candidate_payload import FloatAttributeCandidatePayload
    from ..models.integer_attribute_candidate_payload import IntegerAttributeCandidatePayload
    from ..models.string_attribute_candidate_payload import StringAttributeCandidatePayload


T = TypeVar("T", bound="CandidateItem")


@_attrs_define
class CandidateItem:
    """
    Attributes:
        data (BooleanAttributeCandidatePayload | CandidateItemDataType1 | FloatAttributeCandidatePayload |
            IntegerAttributeCandidatePayload | StringAttributeCandidatePayload):
        citations (list[CandidateCitation]):
        kind (CandidateItemKind):
        section_id (None | Unset | UUID):
    """

    data: (
        BooleanAttributeCandidatePayload
        | CandidateItemDataType1
        | FloatAttributeCandidatePayload
        | IntegerAttributeCandidatePayload
        | StringAttributeCandidatePayload
    )
    citations: list[CandidateCitation]
    kind: CandidateItemKind
    section_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_attribute_candidate_payload import BooleanAttributeCandidatePayload
        from ..models.float_attribute_candidate_payload import FloatAttributeCandidatePayload
        from ..models.integer_attribute_candidate_payload import IntegerAttributeCandidatePayload
        from ..models.string_attribute_candidate_payload import StringAttributeCandidatePayload

        data: dict[str, Any]
        if isinstance(self.data, StringAttributeCandidatePayload):
            data = self.data.to_dict()
        elif isinstance(self.data, IntegerAttributeCandidatePayload):
            data = self.data.to_dict()
        elif isinstance(self.data, FloatAttributeCandidatePayload):
            data = self.data.to_dict()
        elif isinstance(self.data, BooleanAttributeCandidatePayload):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        citations = []
        for citations_item_data in self.citations:
            citations_item = citations_item_data.to_dict()
            citations.append(citations_item)

        kind = self.kind.value

        section_id: None | str | Unset
        if isinstance(self.section_id, Unset):
            section_id = UNSET
        elif isinstance(self.section_id, UUID):
            section_id = str(self.section_id)
        else:
            section_id = self.section_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "citations": citations,
                "kind": kind,
            }
        )
        if section_id is not UNSET:
            field_dict["section_id"] = section_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_attribute_candidate_payload import BooleanAttributeCandidatePayload
        from ..models.candidate_citation import CandidateCitation
        from ..models.candidate_item_data_type_1 import CandidateItemDataType1
        from ..models.float_attribute_candidate_payload import FloatAttributeCandidatePayload
        from ..models.integer_attribute_candidate_payload import IntegerAttributeCandidatePayload
        from ..models.string_attribute_candidate_payload import StringAttributeCandidatePayload

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> (
            BooleanAttributeCandidatePayload
            | CandidateItemDataType1
            | FloatAttributeCandidatePayload
            | IntegerAttributeCandidatePayload
            | StringAttributeCandidatePayload
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_candidate_payload_type_0 = StringAttributeCandidatePayload.from_dict(data)

                return componentsschemas_attribute_candidate_payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_candidate_payload_type_1 = IntegerAttributeCandidatePayload.from_dict(data)

                return componentsschemas_attribute_candidate_payload_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_candidate_payload_type_2 = FloatAttributeCandidatePayload.from_dict(data)

                return componentsschemas_attribute_candidate_payload_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribute_candidate_payload_type_3 = BooleanAttributeCandidatePayload.from_dict(data)

                return componentsschemas_attribute_candidate_payload_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = CandidateItemDataType1.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data"))

        citations = []
        _citations = d.pop("citations")
        for citations_item_data in _citations:
            citations_item = CandidateCitation.from_dict(citations_item_data)

            citations.append(citations_item)

        kind = CandidateItemKind(d.pop("kind"))

        def _parse_section_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                section_id_type_0 = UUID(data)

                return section_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        section_id = _parse_section_id(d.pop("section_id", UNSET))

        candidate_item = cls(
            data=data,
            citations=citations,
            kind=kind,
            section_id=section_id,
        )

        candidate_item.additional_properties = d
        return candidate_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
