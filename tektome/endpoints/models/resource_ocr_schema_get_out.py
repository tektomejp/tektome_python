from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_ocr_schema_get_out_latest_task_result_type_0 import (
        ResourceOCRSchemaGetOutLatestTaskResultType0,
    )


T = TypeVar("T", bound="ResourceOCRSchemaGetOut")


@_attrs_define
class ResourceOCRSchemaGetOut:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        latest_submission_time (datetime.datetime):
        resource (UUID):
        id (None | Unset | UUID):
        status (str | Unset):  Default: 'PENDING'.
        latest_task_id (None | str | Unset):
        latest_task_result (None | ResourceOCRSchemaGetOutLatestTaskResultType0 | Unset):
        extraction_result_file (None | str | Unset):
        result_query_url (None | str | Unset):
    """

    created: datetime.datetime
    updated: datetime.datetime
    latest_submission_time: datetime.datetime
    resource: UUID
    id: None | Unset | UUID = UNSET
    status: str | Unset = "PENDING"
    latest_task_id: None | str | Unset = UNSET
    latest_task_result: None | ResourceOCRSchemaGetOutLatestTaskResultType0 | Unset = UNSET
    extraction_result_file: None | str | Unset = UNSET
    result_query_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_ocr_schema_get_out_latest_task_result_type_0 import (
            ResourceOCRSchemaGetOutLatestTaskResultType0,
        )

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        latest_submission_time = self.latest_submission_time.isoformat()

        resource = str(self.resource)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        status = self.status

        latest_task_id: None | str | Unset
        if isinstance(self.latest_task_id, Unset):
            latest_task_id = UNSET
        else:
            latest_task_id = self.latest_task_id

        latest_task_result: dict[str, Any] | None | Unset
        if isinstance(self.latest_task_result, Unset):
            latest_task_result = UNSET
        elif isinstance(self.latest_task_result, ResourceOCRSchemaGetOutLatestTaskResultType0):
            latest_task_result = self.latest_task_result.to_dict()
        else:
            latest_task_result = self.latest_task_result

        extraction_result_file: None | str | Unset
        if isinstance(self.extraction_result_file, Unset):
            extraction_result_file = UNSET
        else:
            extraction_result_file = self.extraction_result_file

        result_query_url: None | str | Unset
        if isinstance(self.result_query_url, Unset):
            result_query_url = UNSET
        else:
            result_query_url = self.result_query_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "latest_submission_time": latest_submission_time,
                "resource": resource,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if latest_task_id is not UNSET:
            field_dict["latest_task_id"] = latest_task_id
        if latest_task_result is not UNSET:
            field_dict["latest_task_result"] = latest_task_result
        if extraction_result_file is not UNSET:
            field_dict["extraction_result_file"] = extraction_result_file
        if result_query_url is not UNSET:
            field_dict["result_query_url"] = result_query_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_ocr_schema_get_out_latest_task_result_type_0 import (
            ResourceOCRSchemaGetOutLatestTaskResultType0,
        )

        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        latest_submission_time = isoparse(d.pop("latest_submission_time"))

        resource = UUID(d.pop("resource"))

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

        status = d.pop("status", UNSET)

        def _parse_latest_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_task_id = _parse_latest_task_id(d.pop("latest_task_id", UNSET))

        def _parse_latest_task_result(data: object) -> None | ResourceOCRSchemaGetOutLatestTaskResultType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_task_result_type_0 = ResourceOCRSchemaGetOutLatestTaskResultType0.from_dict(data)

                return latest_task_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceOCRSchemaGetOutLatestTaskResultType0 | Unset, data)

        latest_task_result = _parse_latest_task_result(d.pop("latest_task_result", UNSET))

        def _parse_extraction_result_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extraction_result_file = _parse_extraction_result_file(d.pop("extraction_result_file", UNSET))

        def _parse_result_query_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_query_url = _parse_result_query_url(d.pop("result_query_url", UNSET))

        resource_ocr_schema_get_out = cls(
            created=created,
            updated=updated,
            latest_submission_time=latest_submission_time,
            resource=resource,
            id=id,
            status=status,
            latest_task_id=latest_task_id,
            latest_task_result=latest_task_result,
            extraction_result_file=extraction_result_file,
            result_query_url=result_query_url,
        )

        resource_ocr_schema_get_out.additional_properties = d
        return resource_ocr_schema_get_out

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
