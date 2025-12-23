from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents_positional_text_item import DocumentsPositionalTextItem


T = TypeVar("T", bound="Documents")


@_attrs_define
class Documents:
    """
    Attributes:
        positional_text (list[DocumentsPositionalTextItem] | Unset):
        image_urls (list[str] | Unset):
    """

    positional_text: list[DocumentsPositionalTextItem] | Unset = UNSET
    image_urls: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        positional_text: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.positional_text, Unset):
            positional_text = []
            for positional_text_item_data in self.positional_text:
                positional_text_item = positional_text_item_data.to_dict()
                positional_text.append(positional_text_item)

        image_urls: list[str] | Unset = UNSET
        if not isinstance(self.image_urls, Unset):
            image_urls = self.image_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if positional_text is not UNSET:
            field_dict["positional_text"] = positional_text
        if image_urls is not UNSET:
            field_dict["image_urls"] = image_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documents_positional_text_item import DocumentsPositionalTextItem

        d = dict(src_dict)
        _positional_text = d.pop("positional_text", UNSET)
        positional_text: list[DocumentsPositionalTextItem] | Unset = UNSET
        if _positional_text is not UNSET:
            positional_text = []
            for positional_text_item_data in _positional_text:
                positional_text_item = DocumentsPositionalTextItem.from_dict(positional_text_item_data)

                positional_text.append(positional_text_item)

        image_urls = cast(list[str], d.pop("image_urls", UNSET))

        documents = cls(
            positional_text=positional_text,
            image_urls=image_urls,
        )

        documents.additional_properties = d
        return documents

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
