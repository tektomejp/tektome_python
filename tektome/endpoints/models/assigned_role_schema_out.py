from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.non_primitive_role_name import NonPrimitiveRoleName
from ..models.role_name import RoleName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_entity_context import RoleEntityContext
    from ..models.role_project_context import RoleProjectContext


T = TypeVar("T", bound="AssignedRoleSchemaOut")


@_attrs_define
class AssignedRoleSchemaOut:
    """A role assigned to a user

    Attributes:
        role (NonPrimitiveRoleName | RoleName):
        organizations (list[RoleEntityContext] | None | Unset):
        dataspaces (list[RoleEntityContext] | None | Unset):
        projects (list[RoleProjectContext] | None | Unset):
    """

    role: NonPrimitiveRoleName | RoleName
    organizations: list[RoleEntityContext] | None | Unset = UNSET
    dataspaces: list[RoleEntityContext] | None | Unset = UNSET
    projects: list[RoleProjectContext] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role: str
        if isinstance(self.role, RoleName):
            role = self.role.value
        else:
            role = self.role.value

        organizations: list[dict[str, Any]] | None | Unset
        if isinstance(self.organizations, Unset):
            organizations = UNSET
        elif isinstance(self.organizations, list):
            organizations = []
            for organizations_type_0_item_data in self.organizations:
                organizations_type_0_item = organizations_type_0_item_data.to_dict()
                organizations.append(organizations_type_0_item)

        else:
            organizations = self.organizations

        dataspaces: list[dict[str, Any]] | None | Unset
        if isinstance(self.dataspaces, Unset):
            dataspaces = UNSET
        elif isinstance(self.dataspaces, list):
            dataspaces = []
            for dataspaces_type_0_item_data in self.dataspaces:
                dataspaces_type_0_item = dataspaces_type_0_item_data.to_dict()
                dataspaces.append(dataspaces_type_0_item)

        else:
            dataspaces = self.dataspaces

        projects: list[dict[str, Any]] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item = projects_type_0_item_data.to_dict()
                projects.append(projects_type_0_item)

        else:
            projects = self.projects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if dataspaces is not UNSET:
            field_dict["dataspaces"] = dataspaces
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_entity_context import RoleEntityContext
        from ..models.role_project_context import RoleProjectContext

        d = dict(src_dict)

        def _parse_role(data: object) -> NonPrimitiveRoleName | RoleName:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = RoleName(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            role_type_1 = NonPrimitiveRoleName(data)

            return role_type_1

        role = _parse_role(d.pop("role"))

        def _parse_organizations(data: object) -> list[RoleEntityContext] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizations_type_0 = []
                _organizations_type_0 = data
                for organizations_type_0_item_data in _organizations_type_0:
                    organizations_type_0_item = RoleEntityContext.from_dict(organizations_type_0_item_data)

                    organizations_type_0.append(organizations_type_0_item)

                return organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RoleEntityContext] | None | Unset, data)

        organizations = _parse_organizations(d.pop("organizations", UNSET))

        def _parse_dataspaces(data: object) -> list[RoleEntityContext] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dataspaces_type_0 = []
                _dataspaces_type_0 = data
                for dataspaces_type_0_item_data in _dataspaces_type_0:
                    dataspaces_type_0_item = RoleEntityContext.from_dict(dataspaces_type_0_item_data)

                    dataspaces_type_0.append(dataspaces_type_0_item)

                return dataspaces_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RoleEntityContext] | None | Unset, data)

        dataspaces = _parse_dataspaces(d.pop("dataspaces", UNSET))

        def _parse_projects(data: object) -> list[RoleProjectContext] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_type_0 = []
                _projects_type_0 = data
                for projects_type_0_item_data in _projects_type_0:
                    projects_type_0_item = RoleProjectContext.from_dict(projects_type_0_item_data)

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RoleProjectContext] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))

        assigned_role_schema_out = cls(
            role=role,
            organizations=organizations,
            dataspaces=dataspaces,
            projects=projects,
        )

        assigned_role_schema_out.additional_properties = d
        return assigned_role_schema_out

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
