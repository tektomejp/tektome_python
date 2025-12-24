from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.available_language import AvailableLanguage

T = TypeVar("T", bound="Chunk")


@_attrs_define
class Chunk:
    """Class to store text in page after OCR process

    and its metadata like position, language and page_number

        Attributes:
            id (str):
            text (str):
            language (AvailableLanguage):
            page_number (int):
            x (float | int):
            y (float | int):
            w (float | int):
            h (float | int):
    """

    id: str
    text: str
    language: AvailableLanguage
    page_number: int
    x: float | int
    y: float | int
    w: float | int
    h: float | int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        language = self.language.value

        page_number = self.page_number

        x: float | int
        x = self.x

        y: float | int
        y = self.y

        w: float | int
        w = self.w

        h: float | int
        h = self.h

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
                "language": language,
                "page_number": page_number,
                "x": x,
                "y": y,
                "w": w,
                "h": h,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        language = AvailableLanguage(d.pop("language"))

        page_number = d.pop("page_number")

        def _parse_x(data: object) -> float | int:
            return cast(float | int, data)

        x = _parse_x(d.pop("x"))

        def _parse_y(data: object) -> float | int:
            return cast(float | int, data)

        y = _parse_y(d.pop("y"))

        def _parse_w(data: object) -> float | int:
            return cast(float | int, data)

        w = _parse_w(d.pop("w"))

        def _parse_h(data: object) -> float | int:
            return cast(float | int, data)

        h = _parse_h(d.pop("h"))

        chunk = cls(
            id=id,
            text=text,
            language=language,
            page_number=page_number,
            x=x,
            y=y,
            w=w,
            h=h,
        )

        chunk.additional_properties = d
        return chunk

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
