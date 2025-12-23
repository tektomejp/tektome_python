from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

if TYPE_CHECKING:
    from ..models.dataspace_resource_upload_in import DataspaceResourceUploadIn


T = TypeVar("T", bound="AppcoreRoutesDataspacesPostUploadDataspaceProjectMultiPartBodyParams")


@_attrs_define
class AppcoreRoutesDataspacesPostUploadDataspaceProjectMultiPartBodyParams:
    """
    Attributes:
        file (File):
        payload (DataspaceResourceUploadIn):
    """

    file: File
    payload: DataspaceResourceUploadIn
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "payload": payload,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(("payload", (None, json.dumps(self.payload.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataspace_resource_upload_in import DataspaceResourceUploadIn

        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        payload = DataspaceResourceUploadIn.from_dict(d.pop("payload"))

        appcore_routes_dataspaces_post_upload_dataspace_project_multi_part_body_params = cls(
            file=file,
            payload=payload,
        )

        appcore_routes_dataspaces_post_upload_dataspace_project_multi_part_body_params.additional_properties = d
        return appcore_routes_dataspaces_post_upload_dataspace_project_multi_part_body_params

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
