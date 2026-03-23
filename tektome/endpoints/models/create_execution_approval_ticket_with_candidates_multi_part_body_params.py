from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.approval_ticket_post_in import ApprovalTicketPostIn


T = TypeVar("T", bound="CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams")


@_attrs_define
class CreateExecutionApprovalTicketWithCandidatesMultiPartBodyParams:
    """
    Attributes:
        payload (ApprovalTicketPostIn): Serializer for creating an ApprovalTicket
        file (File | Unset):
    """

    payload: ApprovalTicketPostIn
    file: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = self.payload.to_dict()

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payload": payload,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("payload", (None, json.dumps(self.payload.to_dict()).encode(), "application/json")))

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_ticket_post_in import ApprovalTicketPostIn

        d = dict(src_dict)
        payload = ApprovalTicketPostIn.from_dict(d.pop("payload"))

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        create_execution_approval_ticket_with_candidates_multi_part_body_params = cls(
            payload=payload,
            file=file,
        )

        create_execution_approval_ticket_with_candidates_multi_part_body_params.additional_properties = d
        return create_execution_approval_ticket_with_candidates_multi_part_body_params

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
