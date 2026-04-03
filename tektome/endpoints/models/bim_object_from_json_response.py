from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BimObjectFromJsonResponse")


@_attrs_define
class BimObjectFromJsonResponse:
    """Response returned after creating one standalone BIM object from JSON.

    The API keeps this response intentionally small: callers mainly need the
    content-derived object ID and a human-readable confirmation message.

        Attributes:
            id (str): Content-derived Speckle ID of the created BIM object (SHA-256 truncated to 32 hex characters).
            message (str): Human-readable confirmation message.
    """

    id: str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        message = d.pop("message")

        bim_object_from_json_response = cls(
            id=id,
            message=message,
        )

        bim_object_from_json_response.additional_properties = d
        return bim_object_from_json_response

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
