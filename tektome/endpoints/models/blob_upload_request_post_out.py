from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BlobUploadRequestPostOut")


@_attrs_define
class BlobUploadRequestPostOut:
    """Output schema for the streaming upload request endpoint.

    Attributes:
        upload_id (str): Unique identifier for this upload. Use this to complete the upload.
        upload_url (str): Write-only SAS URL for uploading the file directly to Azure Blob Storage.
        blob_path (str): The blob path where the file will be stored.
        expires_at (str): ISO 8601 timestamp when the upload URL expires.
    """

    upload_id: str
    upload_url: str
    blob_path: str
    expires_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        upload_url = self.upload_url

        blob_path = self.blob_path

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
                "upload_url": upload_url,
                "blob_path": blob_path,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        upload_url = d.pop("upload_url")

        blob_path = d.pop("blob_path")

        expires_at = d.pop("expires_at")

        blob_upload_request_post_out = cls(
            upload_id=upload_id,
            upload_url=upload_url,
            blob_path=blob_path,
            expires_at=expires_at,
        )

        blob_upload_request_post_out.additional_properties = d
        return blob_upload_request_post_out

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
