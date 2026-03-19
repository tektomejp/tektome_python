from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bim_element_request import BIMElementRequest


T = TypeVar("T", bound="UpdateBIMCitationRequest")


@_attrs_define
class UpdateBIMCitationRequest:
    """
    Attributes:
        title (None | str | Unset):
        keywords (list[str] | None | Unset):
        bim_elements (list[BIMElementRequest] | None | Unset):
    """

    title: None | str | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    bim_elements: list[BIMElementRequest] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        bim_elements: list[dict[str, Any]] | None | Unset
        if isinstance(self.bim_elements, Unset):
            bim_elements = UNSET
        elif isinstance(self.bim_elements, list):
            bim_elements = []
            for bim_elements_type_0_item_data in self.bim_elements:
                bim_elements_type_0_item = bim_elements_type_0_item_data.to_dict()
                bim_elements.append(bim_elements_type_0_item)

        else:
            bim_elements = self.bim_elements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if bim_elements is not UNSET:
            field_dict["bim_elements"] = bim_elements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_element_request import BIMElementRequest

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_bim_elements(data: object) -> list[BIMElementRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bim_elements_type_0 = []
                _bim_elements_type_0 = data
                for bim_elements_type_0_item_data in _bim_elements_type_0:
                    bim_elements_type_0_item = BIMElementRequest.from_dict(bim_elements_type_0_item_data)

                    bim_elements_type_0.append(bim_elements_type_0_item)

                return bim_elements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BIMElementRequest] | None | Unset, data)

        bim_elements = _parse_bim_elements(d.pop("bim_elements", UNSET))

        update_bim_citation_request = cls(
            title=title,
            keywords=keywords,
            bim_elements=bim_elements,
        )

        update_bim_citation_request.additional_properties = d
        return update_bim_citation_request

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
