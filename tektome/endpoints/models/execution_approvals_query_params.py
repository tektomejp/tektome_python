from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_approvals_query_params_approval_category_types import (
    ExecutionApprovalsQueryParamsApprovalCategoryTypes,
)
from ..models.execution_approvals_query_params_approval_status import ExecutionApprovalsQueryParamsApprovalStatus
from ..models.execution_approvals_query_params_process_type_choices import (
    ExecutionApprovalsQueryParamsProcessTypeChoices,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionApprovalsQueryParams")


@_attrs_define
class ExecutionApprovalsQueryParams:
    """Query parameters for retrieving execution approvals

    Attributes:
        execution_id (None | Unset | UUID):
        status (list[ExecutionApprovalsQueryParamsApprovalStatus] | Unset): Approval status to filter executions
        process_types (list[ExecutionApprovalsQueryParamsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        execution_group_ids (list[UUID] | Unset): list of Execution group IDs
        target_files_ids (list[UUID] | Unset): Target core resource file IDs
        target_entity_ids (list[UUID] | Unset): Target DS entity IDs
        category (list[ExecutionApprovalsQueryParamsApprovalCategoryTypes] | Unset): Approval category to filter
            executions
        file_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID file attributes extracted
        entity_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID entity attributes
            extracted
    """

    execution_id: None | Unset | UUID = UNSET
    status: list[ExecutionApprovalsQueryParamsApprovalStatus] | Unset = UNSET
    process_types: list[ExecutionApprovalsQueryParamsProcessTypeChoices] | Unset = UNSET
    process_ids: list[UUID] | Unset = UNSET
    execution_group_ids: list[UUID] | Unset = UNSET
    target_files_ids: list[UUID] | Unset = UNSET
    target_entity_ids: list[UUID] | Unset = UNSET
    category: list[ExecutionApprovalsQueryParamsApprovalCategoryTypes] | Unset = UNSET
    file_attributes_extracted_ids: list[UUID] | Unset = UNSET
    entity_attributes_extracted_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id: None | str | Unset
        if isinstance(self.execution_id, Unset):
            execution_id = UNSET
        elif isinstance(self.execution_id, UUID):
            execution_id = str(self.execution_id)
        else:
            execution_id = self.execution_id

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value
                status.append(status_item)

        process_types: list[str] | Unset = UNSET
        if not isinstance(self.process_types, Unset):
            process_types = []
            for process_types_item_data in self.process_types:
                process_types_item = process_types_item_data.value
                process_types.append(process_types_item)

        process_ids: list[str] | Unset = UNSET
        if not isinstance(self.process_ids, Unset):
            process_ids = []
            for process_ids_item_data in self.process_ids:
                process_ids_item = str(process_ids_item_data)
                process_ids.append(process_ids_item)

        execution_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.execution_group_ids, Unset):
            execution_group_ids = []
            for execution_group_ids_item_data in self.execution_group_ids:
                execution_group_ids_item = str(execution_group_ids_item_data)
                execution_group_ids.append(execution_group_ids_item)

        target_files_ids: list[str] | Unset = UNSET
        if not isinstance(self.target_files_ids, Unset):
            target_files_ids = []
            for target_files_ids_item_data in self.target_files_ids:
                target_files_ids_item = str(target_files_ids_item_data)
                target_files_ids.append(target_files_ids_item)

        target_entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.target_entity_ids, Unset):
            target_entity_ids = []
            for target_entity_ids_item_data in self.target_entity_ids:
                target_entity_ids_item = str(target_entity_ids_item_data)
                target_entity_ids.append(target_entity_ids_item)

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.value
                category.append(category_item)

        file_attributes_extracted_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_attributes_extracted_ids, Unset):
            file_attributes_extracted_ids = []
            for file_attributes_extracted_ids_item_data in self.file_attributes_extracted_ids:
                file_attributes_extracted_ids_item = str(file_attributes_extracted_ids_item_data)
                file_attributes_extracted_ids.append(file_attributes_extracted_ids_item)

        entity_attributes_extracted_ids: list[str] | Unset = UNSET
        if not isinstance(self.entity_attributes_extracted_ids, Unset):
            entity_attributes_extracted_ids = []
            for entity_attributes_extracted_ids_item_data in self.entity_attributes_extracted_ids:
                entity_attributes_extracted_ids_item = str(entity_attributes_extracted_ids_item_data)
                entity_attributes_extracted_ids.append(entity_attributes_extracted_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if status is not UNSET:
            field_dict["status"] = status
        if process_types is not UNSET:
            field_dict["process_types"] = process_types
        if process_ids is not UNSET:
            field_dict["process_ids"] = process_ids
        if execution_group_ids is not UNSET:
            field_dict["execution_group_ids"] = execution_group_ids
        if target_files_ids is not UNSET:
            field_dict["target_files_ids"] = target_files_ids
        if target_entity_ids is not UNSET:
            field_dict["target_entity_ids"] = target_entity_ids
        if category is not UNSET:
            field_dict["category"] = category
        if file_attributes_extracted_ids is not UNSET:
            field_dict["file_attributes_extracted_ids"] = file_attributes_extracted_ids
        if entity_attributes_extracted_ids is not UNSET:
            field_dict["entity_attributes_extracted_ids"] = entity_attributes_extracted_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_execution_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_id_type_0 = UUID(data)

                return execution_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        execution_id = _parse_execution_id(d.pop("execution_id", UNSET))

        _status = d.pop("status", UNSET)
        status: list[ExecutionApprovalsQueryParamsApprovalStatus] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = ExecutionApprovalsQueryParamsApprovalStatus(status_item_data)

                status.append(status_item)

        _process_types = d.pop("process_types", UNSET)
        process_types: list[ExecutionApprovalsQueryParamsProcessTypeChoices] | Unset = UNSET
        if _process_types is not UNSET:
            process_types = []
            for process_types_item_data in _process_types:
                process_types_item = ExecutionApprovalsQueryParamsProcessTypeChoices(process_types_item_data)

                process_types.append(process_types_item)

        _process_ids = d.pop("process_ids", UNSET)
        process_ids: list[UUID] | Unset = UNSET
        if _process_ids is not UNSET:
            process_ids = []
            for process_ids_item_data in _process_ids:
                process_ids_item = UUID(process_ids_item_data)

                process_ids.append(process_ids_item)

        _execution_group_ids = d.pop("execution_group_ids", UNSET)
        execution_group_ids: list[UUID] | Unset = UNSET
        if _execution_group_ids is not UNSET:
            execution_group_ids = []
            for execution_group_ids_item_data in _execution_group_ids:
                execution_group_ids_item = UUID(execution_group_ids_item_data)

                execution_group_ids.append(execution_group_ids_item)

        _target_files_ids = d.pop("target_files_ids", UNSET)
        target_files_ids: list[UUID] | Unset = UNSET
        if _target_files_ids is not UNSET:
            target_files_ids = []
            for target_files_ids_item_data in _target_files_ids:
                target_files_ids_item = UUID(target_files_ids_item_data)

                target_files_ids.append(target_files_ids_item)

        _target_entity_ids = d.pop("target_entity_ids", UNSET)
        target_entity_ids: list[UUID] | Unset = UNSET
        if _target_entity_ids is not UNSET:
            target_entity_ids = []
            for target_entity_ids_item_data in _target_entity_ids:
                target_entity_ids_item = UUID(target_entity_ids_item_data)

                target_entity_ids.append(target_entity_ids_item)

        _category = d.pop("category", UNSET)
        category: list[ExecutionApprovalsQueryParamsApprovalCategoryTypes] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = ExecutionApprovalsQueryParamsApprovalCategoryTypes(category_item_data)

                category.append(category_item)

        _file_attributes_extracted_ids = d.pop("file_attributes_extracted_ids", UNSET)
        file_attributes_extracted_ids: list[UUID] | Unset = UNSET
        if _file_attributes_extracted_ids is not UNSET:
            file_attributes_extracted_ids = []
            for file_attributes_extracted_ids_item_data in _file_attributes_extracted_ids:
                file_attributes_extracted_ids_item = UUID(file_attributes_extracted_ids_item_data)

                file_attributes_extracted_ids.append(file_attributes_extracted_ids_item)

        _entity_attributes_extracted_ids = d.pop("entity_attributes_extracted_ids", UNSET)
        entity_attributes_extracted_ids: list[UUID] | Unset = UNSET
        if _entity_attributes_extracted_ids is not UNSET:
            entity_attributes_extracted_ids = []
            for entity_attributes_extracted_ids_item_data in _entity_attributes_extracted_ids:
                entity_attributes_extracted_ids_item = UUID(entity_attributes_extracted_ids_item_data)

                entity_attributes_extracted_ids.append(entity_attributes_extracted_ids_item)

        execution_approvals_query_params = cls(
            execution_id=execution_id,
            status=status,
            process_types=process_types,
            process_ids=process_ids,
            execution_group_ids=execution_group_ids,
            target_files_ids=target_files_ids,
            target_entity_ids=target_entity_ids,
            category=category,
            file_attributes_extracted_ids=file_attributes_extracted_ids,
            entity_attributes_extracted_ids=entity_attributes_extracted_ids,
        )

        execution_approvals_query_params.additional_properties = d
        return execution_approvals_query_params

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
