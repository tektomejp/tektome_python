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
    from ..models.bim_task_response_result import BimTaskResponseResult


T = TypeVar("T", bound="BimTaskResponse")


@_attrs_define
class BimTaskResponse:
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        id (None | Unset | UUID):
        resource (None | Unset | UUID):
        bim_project (None | Unset | UUID):
        task_type (str | Unset):  Default: 'UNSET'.
        celery_task_id (None | str | Unset):
        status (str | Unset):  Default: 'PENDING'.
        result (BimTaskResponseResult | Unset):
    """

    created: datetime.datetime
    updated: datetime.datetime
    id: None | Unset | UUID = UNSET
    resource: None | Unset | UUID = UNSET
    bim_project: None | Unset | UUID = UNSET
    task_type: str | Unset = "UNSET"
    celery_task_id: None | str | Unset = UNSET
    status: str | Unset = "PENDING"
    result: BimTaskResponseResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        updated = self.updated.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        resource: None | str | Unset
        if isinstance(self.resource, Unset):
            resource = UNSET
        elif isinstance(self.resource, UUID):
            resource = str(self.resource)
        else:
            resource = self.resource

        bim_project: None | str | Unset
        if isinstance(self.bim_project, Unset):
            bim_project = UNSET
        elif isinstance(self.bim_project, UUID):
            bim_project = str(self.bim_project)
        else:
            bim_project = self.bim_project

        task_type = self.task_type

        celery_task_id: None | str | Unset
        if isinstance(self.celery_task_id, Unset):
            celery_task_id = UNSET
        else:
            celery_task_id = self.celery_task_id

        status = self.status

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if resource is not UNSET:
            field_dict["resource"] = resource
        if bim_project is not UNSET:
            field_dict["bim_project"] = bim_project
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if celery_task_id is not UNSET:
            field_dict["celery_task_id"] = celery_task_id
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_task_response_result import BimTaskResponseResult

        d = dict(src_dict)
        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

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

        def _parse_resource(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_type_0 = UUID(data)

                return resource_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource = _parse_resource(d.pop("resource", UNSET))

        def _parse_bim_project(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bim_project_type_0 = UUID(data)

                return bim_project_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bim_project = _parse_bim_project(d.pop("bim_project", UNSET))

        task_type = d.pop("task_type", UNSET)

        def _parse_celery_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        celery_task_id = _parse_celery_task_id(d.pop("celery_task_id", UNSET))

        status = d.pop("status", UNSET)

        _result = d.pop("result", UNSET)
        result: BimTaskResponseResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = BimTaskResponseResult.from_dict(_result)

        bim_task_response = cls(
            created=created,
            updated=updated,
            id=id,
            resource=resource,
            bim_project=bim_project,
            task_type=task_type,
            celery_task_id=celery_task_id,
            status=status,
            result=result,
        )

        bim_task_response.additional_properties = d
        return bim_task_response

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
