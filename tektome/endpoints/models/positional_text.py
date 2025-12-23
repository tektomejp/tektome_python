from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PositionalText")


@_attrs_define
class PositionalText:
    """Dataclass to store text and its position in a given page.

    Attributes:
        id (str):
        text (str):
        rectangle (list[float | int]):
    """

    id: str
    text: str
    rectangle: list[float | int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        rectangle = []
        for rectangle_item_data in self.rectangle:
            rectangle_item: float | int
            rectangle_item = rectangle_item_data
            rectangle.append(rectangle_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
                "rectangle": rectangle,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        rectangle = []
        _rectangle = d.pop("rectangle")
        for rectangle_item_data in _rectangle:

            def _parse_rectangle_item(data: object) -> float | int:
                return cast(float | int, data)

            rectangle_item = _parse_rectangle_item(rectangle_item_data)

            rectangle.append(rectangle_item)

        positional_text = cls(
            id=id,
            text=text,
            rectangle=rectangle,
        )

        positional_text.additional_properties = d
        return positional_text

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
