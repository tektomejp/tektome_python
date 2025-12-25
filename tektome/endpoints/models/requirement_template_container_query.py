from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementTemplateContainerQuery")


@_attrs_define
class RequirementTemplateContainerQuery:
    """Serializer for Requirement Template Container Query.

    Attributes:
        organization_id (None | Unset | UUID):
        view_mode (None | str | Unset):
        page (int | None | Unset):  Default: 1.
        page_size (int | None | Unset):  Default: 30.
    """

    organization_id: None | Unset | UUID = UNSET
    view_mode: None | str | Unset = UNSET
    page: int | None | Unset = 1
    page_size: int | None | Unset = 30
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        view_mode: None | str | Unset
        if isinstance(self.view_mode, Unset):
            view_mode = UNSET
        else:
            view_mode = self.view_mode

        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        page_size: int | None | Unset
        if isinstance(self.page_size, Unset):
            page_size = UNSET
        else:
            page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if view_mode is not UNSET:
            field_dict["view_mode"] = view_mode
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_view_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view_mode = _parse_view_mode(d.pop("view_mode", UNSET))

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        def _parse_page_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_size = _parse_page_size(d.pop("page_size", UNSET))

        requirement_template_container_query = cls(
            organization_id=organization_id,
            view_mode=view_mode,
            page=page,
            page_size=page_size,
        )

        requirement_template_container_query.additional_properties = d
        return requirement_template_container_query

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
