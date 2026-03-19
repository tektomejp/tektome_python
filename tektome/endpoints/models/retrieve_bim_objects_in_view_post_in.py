from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieveBimObjectsInViewPostIn")


@_attrs_define
class RetrieveBimObjectsInViewPostIn:
    """
    Attributes:
        bim_project_id (UUID):
        only_ids (bool | Unset):  Default: False.
        all_at_once (bool | Unset):  Default: False.
        page_size (int | Unset):  Default: 100.
        page (int | Unset):  Default: 1.
    """

    bim_project_id: UUID
    only_ids: bool | Unset = False
    all_at_once: bool | Unset = False
    page_size: int | Unset = 100
    page: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_project_id = str(self.bim_project_id)

        only_ids = self.only_ids

        all_at_once = self.all_at_once

        page_size = self.page_size

        page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_project_id": bim_project_id,
            }
        )
        if only_ids is not UNSET:
            field_dict["only_ids"] = only_ids
        if all_at_once is not UNSET:
            field_dict["all_at_once"] = all_at_once
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bim_project_id = UUID(d.pop("bim_project_id"))

        only_ids = d.pop("only_ids", UNSET)

        all_at_once = d.pop("all_at_once", UNSET)

        page_size = d.pop("page_size", UNSET)

        page = d.pop("page", UNSET)

        retrieve_bim_objects_in_view_post_in = cls(
            bim_project_id=bim_project_id,
            only_ids=only_ids,
            all_at_once=all_at_once,
            page_size=page_size,
            page=page,
        )

        retrieve_bim_objects_in_view_post_in.additional_properties = d
        return retrieve_bim_objects_in_view_post_in

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
