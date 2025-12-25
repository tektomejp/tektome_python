from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueueLengthStatusGetOut")


@_attrs_define
class QueueLengthStatusGetOut:
    """
    Attributes:
        celery (int):
        faststream (int):
    """

    celery: int
    faststream: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        celery = self.celery

        faststream = self.faststream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "celery": celery,
                "faststream": faststream,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        celery = d.pop("celery")

        faststream = d.pop("faststream")

        queue_length_status_get_out = cls(
            celery=celery,
            faststream=faststream,
        )

        queue_length_status_get_out.additional_properties = d
        return queue_length_status_get_out

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
