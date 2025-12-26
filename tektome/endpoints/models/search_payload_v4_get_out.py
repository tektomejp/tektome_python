from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.parsed_tektome_response_entry import ParsedTektomeResponseEntry
    from ..models.tektome_response_entry import TektomeResponseEntry


T = TypeVar("T", bound="SearchPayloadV4GetOut")


@_attrs_define
class SearchPayloadV4GetOut:
    """
    Attributes:
        tektome_response (list[TektomeResponseEntry]):
        parsed_tektome_response (list[ParsedTektomeResponseEntry]):
    """

    tektome_response: list[TektomeResponseEntry]
    parsed_tektome_response: list[ParsedTektomeResponseEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tektome_response = []
        for tektome_response_item_data in self.tektome_response:
            tektome_response_item = tektome_response_item_data.to_dict()
            tektome_response.append(tektome_response_item)

        parsed_tektome_response = []
        for parsed_tektome_response_item_data in self.parsed_tektome_response:
            parsed_tektome_response_item = parsed_tektome_response_item_data.to_dict()
            parsed_tektome_response.append(parsed_tektome_response_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tektome_response": tektome_response,
                "parsed_tektome_response": parsed_tektome_response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parsed_tektome_response_entry import ParsedTektomeResponseEntry
        from ..models.tektome_response_entry import TektomeResponseEntry

        d = dict(src_dict)
        tektome_response = []
        _tektome_response = d.pop("tektome_response")
        for tektome_response_item_data in _tektome_response:
            tektome_response_item = TektomeResponseEntry.from_dict(tektome_response_item_data)

            tektome_response.append(tektome_response_item)

        parsed_tektome_response = []
        _parsed_tektome_response = d.pop("parsed_tektome_response")
        for parsed_tektome_response_item_data in _parsed_tektome_response:
            parsed_tektome_response_item = ParsedTektomeResponseEntry.from_dict(parsed_tektome_response_item_data)

            parsed_tektome_response.append(parsed_tektome_response_item)

        search_payload_v4_get_out = cls(
            tektome_response=tektome_response,
            parsed_tektome_response=parsed_tektome_response,
        )

        search_payload_v4_get_out.additional_properties = d
        return search_payload_v4_get_out

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
