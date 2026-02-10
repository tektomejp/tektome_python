from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleProjectContext")


@_attrs_define
class RoleProjectContext:
    """Model representing a Project context object for an assigned role.

    Inherits from RoleEntityContext and adds:
    lawtalk_id: Optional UUID of the associated Lawtalk project.

        Attributes:
            id (UUID):
            name (str):
            lawtalk_id (None | Unset | UUID):
    """

    id: UUID
    name: str
    lawtalk_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        lawtalk_id: None | str | Unset
        if isinstance(self.lawtalk_id, Unset):
            lawtalk_id = UNSET
        elif isinstance(self.lawtalk_id, UUID):
            lawtalk_id = str(self.lawtalk_id)
        else:
            lawtalk_id = self.lawtalk_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if lawtalk_id is not UNSET:
            field_dict["lawtalk_id"] = lawtalk_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_lawtalk_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lawtalk_id_type_0 = UUID(data)

                return lawtalk_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        lawtalk_id = _parse_lawtalk_id(d.pop("lawtalk_id", UNSET))

        role_project_context = cls(
            id=id,
            name=name,
            lawtalk_id=lawtalk_id,
        )

        role_project_context.additional_properties = d
        return role_project_context

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
