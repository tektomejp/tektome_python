from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityTrackerGetOut")


@_attrs_define
class EntityTrackerGetOut:
    """
    Attributes:
        observed_entity (UUID):
        scoping_entity (UUID):
        last_seen_at (datetime.datetime):
        view_mode (str | Unset):  Default: 'default'.
    """

    observed_entity: UUID
    scoping_entity: UUID
    last_seen_at: datetime.datetime
    view_mode: str | Unset = "default"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observed_entity = str(self.observed_entity)

        scoping_entity = str(self.scoping_entity)

        last_seen_at = self.last_seen_at.isoformat()

        view_mode = self.view_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observed_entity": observed_entity,
                "scoping_entity": scoping_entity,
                "last_seen_at": last_seen_at,
            }
        )
        if view_mode is not UNSET:
            field_dict["view_mode"] = view_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        observed_entity = UUID(d.pop("observed_entity"))

        scoping_entity = UUID(d.pop("scoping_entity"))

        last_seen_at = isoparse(d.pop("last_seen_at"))

        view_mode = d.pop("view_mode", UNSET)

        entity_tracker_get_out = cls(
            observed_entity=observed_entity,
            scoping_entity=scoping_entity,
            last_seen_at=last_seen_at,
            view_mode=view_mode,
        )

        entity_tracker_get_out.additional_properties = d
        return entity_tracker_get_out

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
