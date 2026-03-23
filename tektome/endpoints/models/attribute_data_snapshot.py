from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribute_data_snapshot_state import AttributeDataSnapshotState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_input_payload import AttributeInputPayload
    from ..models.attribute_reviewed_data import AttributeReviewedData


T = TypeVar("T", bound="AttributeDataSnapshot")


@_attrs_define
class AttributeDataSnapshot:
    """Data snapshot for attribute candidates.

    state="initial": populated at creation with lightweight filter IDs.
    state="reviewed": enriched on approval with full AttributeGetOut keys + citations.

        Attributes:
            state (AttributeDataSnapshotState):
            input_payload (AttributeInputPayload): Filter fields for attribute candidates — always present.
            snapshot_data_type (Literal['attribute'] | Unset):  Default: 'attribute'.
            data (AttributeReviewedData | None | Unset):
    """

    state: AttributeDataSnapshotState
    input_payload: AttributeInputPayload
    snapshot_data_type: Literal["attribute"] | Unset = "attribute"
    data: AttributeReviewedData | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_reviewed_data import AttributeReviewedData

        state = self.state.value

        input_payload = self.input_payload.to_dict()

        snapshot_data_type = self.snapshot_data_type

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, AttributeReviewedData):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "input_payload": input_payload,
            }
        )
        if snapshot_data_type is not UNSET:
            field_dict["snapshot_data_type"] = snapshot_data_type
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_input_payload import AttributeInputPayload
        from ..models.attribute_reviewed_data import AttributeReviewedData

        d = dict(src_dict)
        state = AttributeDataSnapshotState(d.pop("state"))

        input_payload = AttributeInputPayload.from_dict(d.pop("input_payload"))

        snapshot_data_type = cast(Literal["attribute"] | Unset, d.pop("snapshot_data_type", UNSET))
        if snapshot_data_type != "attribute" and not isinstance(snapshot_data_type, Unset):
            raise ValueError(f"snapshot_data_type must match const 'attribute', got '{snapshot_data_type}'")

        def _parse_data(data: object) -> AttributeReviewedData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = AttributeReviewedData.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttributeReviewedData | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        attribute_data_snapshot = cls(
            state=state,
            input_payload=input_payload,
            snapshot_data_type=snapshot_data_type,
            data=data,
        )

        attribute_data_snapshot.additional_properties = d
        return attribute_data_snapshot

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
