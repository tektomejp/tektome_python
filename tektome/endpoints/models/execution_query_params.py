from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.execution_query_params_approval_category_types import ExecutionQueryParamsApprovalCategoryTypes
from ..models.execution_query_params_execution_review_status import ExecutionQueryParamsExecutionReviewStatus
from ..models.execution_query_params_execution_status import ExecutionQueryParamsExecutionStatus
from ..models.execution_query_params_process_type_choices import ExecutionQueryParamsProcessTypeChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionQueryParams")


@_attrs_define
class ExecutionQueryParams:
    """Query parameters for filtering executions.

    Attributes:
        process_types (list[ExecutionQueryParamsProcessTypeChoices] | Unset): Process types
        process_ids (list[UUID] | Unset): Process IDs
        status (list[ExecutionQueryParamsExecutionStatus] | Unset): Execution group statuses
        review_status (list[ExecutionQueryParamsExecutionReviewStatus] | Unset): Execution's review statuses
        launched_by_ids (list[UUID] | Unset): IDs of users who launched the execution groups
        start_datetime (datetime.datetime | None | Unset): Filter execution groups started on or after this datetime
        end_datetime (datetime.datetime | None | Unset): Filter execution groups ended on or before this datetime
        memo (None | str | Unset): Filter execution groups containing this memo text
        execution_group_ids (list[UUID] | Unset): Execution group IDs
        target_files_ids (list[UUID] | Unset): Target core resource file IDs
        target_entity_ids (list[UUID] | Unset): Target DS entity IDs
        category (list[ExecutionQueryParamsApprovalCategoryTypes] | Unset): Approval category to filter executions
        file_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID file attributes extracted
        entity_attributes_extracted_ids (list[UUID] | Unset): Filter executions with these UUID entity attributes
            extracted
    """

    process_types: list[ExecutionQueryParamsProcessTypeChoices] | Unset = UNSET
    process_ids: list[UUID] | Unset = UNSET
    status: list[ExecutionQueryParamsExecutionStatus] | Unset = UNSET
    review_status: list[ExecutionQueryParamsExecutionReviewStatus] | Unset = UNSET
    launched_by_ids: list[UUID] | Unset = UNSET
    start_datetime: datetime.datetime | None | Unset = UNSET
    end_datetime: datetime.datetime | None | Unset = UNSET
    memo: None | str | Unset = UNSET
    execution_group_ids: list[UUID] | Unset = UNSET
    target_files_ids: list[UUID] | Unset = UNSET
    target_entity_ids: list[UUID] | Unset = UNSET
    category: list[ExecutionQueryParamsApprovalCategoryTypes] | Unset = UNSET
    file_attributes_extracted_ids: list[UUID] | Unset = UNSET
    entity_attributes_extracted_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value
                status.append(status_item)

        review_status: list[str] | Unset = UNSET
        if not isinstance(self.review_status, Unset):
            review_status = []
            for review_status_item_data in self.review_status:
                review_status_item = review_status_item_data.value
                review_status.append(review_status_item)

        launched_by_ids: list[str] | Unset = UNSET
        if not isinstance(self.launched_by_ids, Unset):
            launched_by_ids = []
            for launched_by_ids_item_data in self.launched_by_ids:
                launched_by_ids_item = str(launched_by_ids_item_data)
                launched_by_ids.append(launched_by_ids_item)

        start_datetime: None | str | Unset
        if isinstance(self.start_datetime, Unset):
            start_datetime = UNSET
        elif isinstance(self.start_datetime, datetime.datetime):
            start_datetime = self.start_datetime.isoformat()
        else:
            start_datetime = self.start_datetime

        end_datetime: None | str | Unset
        if isinstance(self.end_datetime, Unset):
            end_datetime = UNSET
        elif isinstance(self.end_datetime, datetime.datetime):
            end_datetime = self.end_datetime.isoformat()
        else:
            end_datetime = self.end_datetime

        memo: None | str | Unset
        if isinstance(self.memo, Unset):
            memo = UNSET
        else:
            memo = self.memo

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
        if process_types is not UNSET:
            field_dict["process_types"] = process_types
        if process_ids is not UNSET:
            field_dict["process_ids"] = process_ids
        if status is not UNSET:
            field_dict["status"] = status
        if review_status is not UNSET:
            field_dict["review_status"] = review_status
        if launched_by_ids is not UNSET:
            field_dict["launched_by_ids"] = launched_by_ids
        if start_datetime is not UNSET:
            field_dict["start_datetime"] = start_datetime
        if end_datetime is not UNSET:
            field_dict["end_datetime"] = end_datetime
        if memo is not UNSET:
            field_dict["memo"] = memo
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
        _process_types = d.pop("process_types", UNSET)
        process_types: list[ExecutionQueryParamsProcessTypeChoices] | Unset = UNSET
        if _process_types is not UNSET:
            process_types = []
            for process_types_item_data in _process_types:
                process_types_item = ExecutionQueryParamsProcessTypeChoices(process_types_item_data)

                process_types.append(process_types_item)

        _process_ids = d.pop("process_ids", UNSET)
        process_ids: list[UUID] | Unset = UNSET
        if _process_ids is not UNSET:
            process_ids = []
            for process_ids_item_data in _process_ids:
                process_ids_item = UUID(process_ids_item_data)

                process_ids.append(process_ids_item)

        _status = d.pop("status", UNSET)
        status: list[ExecutionQueryParamsExecutionStatus] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = ExecutionQueryParamsExecutionStatus(status_item_data)

                status.append(status_item)

        _review_status = d.pop("review_status", UNSET)
        review_status: list[ExecutionQueryParamsExecutionReviewStatus] | Unset = UNSET
        if _review_status is not UNSET:
            review_status = []
            for review_status_item_data in _review_status:
                review_status_item = ExecutionQueryParamsExecutionReviewStatus(review_status_item_data)

                review_status.append(review_status_item)

        _launched_by_ids = d.pop("launched_by_ids", UNSET)
        launched_by_ids: list[UUID] | Unset = UNSET
        if _launched_by_ids is not UNSET:
            launched_by_ids = []
            for launched_by_ids_item_data in _launched_by_ids:
                launched_by_ids_item = UUID(launched_by_ids_item_data)

                launched_by_ids.append(launched_by_ids_item)

        def _parse_start_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_datetime_type_0 = isoparse(data)

                return start_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_datetime = _parse_start_datetime(d.pop("start_datetime", UNSET))

        def _parse_end_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_datetime_type_0 = isoparse(data)

                return end_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_datetime = _parse_end_datetime(d.pop("end_datetime", UNSET))

        def _parse_memo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        memo = _parse_memo(d.pop("memo", UNSET))

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
        category: list[ExecutionQueryParamsApprovalCategoryTypes] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = ExecutionQueryParamsApprovalCategoryTypes(category_item_data)

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

        execution_query_params = cls(
            process_types=process_types,
            process_ids=process_ids,
            status=status,
            review_status=review_status,
            launched_by_ids=launched_by_ids,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            memo=memo,
            execution_group_ids=execution_group_ids,
            target_files_ids=target_files_ids,
            target_entity_ids=target_entity_ids,
            category=category,
            file_attributes_extracted_ids=file_attributes_extracted_ids,
            entity_attributes_extracted_ids=entity_attributes_extracted_ids,
        )

        execution_query_params.additional_properties = d
        return execution_query_params

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
