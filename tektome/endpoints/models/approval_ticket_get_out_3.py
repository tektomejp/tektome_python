from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_ticket_get_out_3_data_container import ApprovalTicketGetOut3DataContainer


T = TypeVar("T", bound="ApprovalTicketGetOut3")


@_attrs_define
class ApprovalTicketGetOut3:
    """Serializer for ApprovalTicketCandidate details

    Attributes:
        id (None | Unset | UUID):
        data_container (ApprovalTicketGetOut3DataContainer | Unset): The data related to this approval ticket candidate.
            These are the payload changes proposed for approval
        status (str | Unset): The status of the approval ticket Default: 'Unselected'.
    """

    id: None | Unset | UUID = UNSET
    data_container: ApprovalTicketGetOut3DataContainer | Unset = UNSET
    status: str | Unset = "Unselected"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        data_container: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_container, Unset):
            data_container = self.data_container.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if data_container is not UNSET:
            field_dict["data_container"] = data_container
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_ticket_get_out_3_data_container import ApprovalTicketGetOut3DataContainer

        d = dict(src_dict)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        _data_container = d.pop("data_container", UNSET)
        data_container: ApprovalTicketGetOut3DataContainer | Unset
        if isinstance(_data_container, Unset):
            data_container = UNSET
        else:
            data_container = ApprovalTicketGetOut3DataContainer.from_dict(_data_container)

        status = d.pop("status", UNSET)

        approval_ticket_get_out_3 = cls(
            id=id,
            data_container=data_container,
            status=status,
        )

        approval_ticket_get_out_3.additional_properties = d
        return approval_ticket_get_out_3

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
