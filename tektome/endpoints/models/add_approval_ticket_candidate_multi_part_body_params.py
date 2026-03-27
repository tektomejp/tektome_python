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
    from ..models.add_candidate_post_in import AddCandidatePostIn


T = TypeVar("T", bound="AddApprovalTicketCandidateMultiPartBodyParams")


@_attrs_define
class AddApprovalTicketCandidateMultiPartBodyParams:
    """
    Attributes:
        payload (AddCandidatePostIn): Serializer for adding a new candidate variation to an existing approval ticket
        file (File | Unset):
    """

    payload: AddCandidatePostIn
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
        from ..models.add_candidate_post_in import AddCandidatePostIn

        d = dict(src_dict)
        payload = AddCandidatePostIn.from_dict(d.pop("payload"))

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        add_approval_ticket_candidate_multi_part_body_params = cls(
            payload=payload,
            file=file,
        )

        add_approval_ticket_candidate_multi_part_body_params.additional_properties = d
        return add_approval_ticket_candidate_multi_part_body_params

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
