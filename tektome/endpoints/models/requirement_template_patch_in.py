from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.requirement_template_status import RequirementTemplateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.requirement_item_template import RequirementItemTemplate


T = TypeVar("T", bound="RequirementTemplatePatchIn")


@_attrs_define
class RequirementTemplatePatchIn:
    """Serializer for creating a Requirement Template.

    Attributes:
        title (None | str | Unset):
        status (None | RequirementTemplateStatus | Unset):
        requirement_item_attribute_table (list[RequirementItemTemplate] | None | Unset):
    """

    title: None | str | Unset = UNSET
    status: None | RequirementTemplateStatus | Unset = UNSET
    requirement_item_attribute_table: list[RequirementItemTemplate] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, RequirementTemplateStatus):
            status = self.status.value
        else:
            status = self.status

        requirement_item_attribute_table: list[dict[str, Any]] | None | Unset
        if isinstance(self.requirement_item_attribute_table, Unset):
            requirement_item_attribute_table = UNSET
        elif isinstance(self.requirement_item_attribute_table, list):
            requirement_item_attribute_table = []
            for requirement_item_attribute_table_type_0_item_data in self.requirement_item_attribute_table:
                requirement_item_attribute_table_type_0_item = (
                    requirement_item_attribute_table_type_0_item_data.to_dict()
                )
                requirement_item_attribute_table.append(requirement_item_attribute_table_type_0_item)

        else:
            requirement_item_attribute_table = self.requirement_item_attribute_table

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if requirement_item_attribute_table is not UNSET:
            field_dict["requirement_item_attribute_table"] = requirement_item_attribute_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requirement_item_template import RequirementItemTemplate

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_status(data: object) -> None | RequirementTemplateStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = RequirementTemplateStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RequirementTemplateStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_requirement_item_attribute_table(data: object) -> list[RequirementItemTemplate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requirement_item_attribute_table_type_0 = []
                _requirement_item_attribute_table_type_0 = data
                for requirement_item_attribute_table_type_0_item_data in _requirement_item_attribute_table_type_0:
                    requirement_item_attribute_table_type_0_item = RequirementItemTemplate.from_dict(
                        requirement_item_attribute_table_type_0_item_data
                    )

                    requirement_item_attribute_table_type_0.append(requirement_item_attribute_table_type_0_item)

                return requirement_item_attribute_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RequirementItemTemplate] | None | Unset, data)

        requirement_item_attribute_table = _parse_requirement_item_attribute_table(
            d.pop("requirement_item_attribute_table", UNSET)
        )

        requirement_template_patch_in = cls(
            title=title,
            status=status,
            requirement_item_attribute_table=requirement_item_attribute_table,
        )

        requirement_template_patch_in.additional_properties = d
        return requirement_template_patch_in

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
