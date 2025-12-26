from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObservabilitySchemaIn")


@_attrs_define
class ObservabilitySchemaIn:
    """
    Attributes:
        observed_entity (UUID):
        scoping_entity (UUID):
        is_viewed (bool | Unset):  Default: False.
    """

    observed_entity: UUID
    scoping_entity: UUID
    is_viewed: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observed_entity = str(self.observed_entity)

        scoping_entity = str(self.scoping_entity)

        is_viewed = self.is_viewed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observed_entity": observed_entity,
                "scoping_entity": scoping_entity,
            }
        )
        if is_viewed is not UNSET:
            field_dict["is_viewed"] = is_viewed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        observed_entity = UUID(d.pop("observed_entity"))

        scoping_entity = UUID(d.pop("scoping_entity"))

        is_viewed = d.pop("is_viewed", UNSET)

        observability_schema_in = cls(
            observed_entity=observed_entity,
            scoping_entity=scoping_entity,
            is_viewed=is_viewed,
        )

        observability_schema_in.additional_properties = d
        return observability_schema_in

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
