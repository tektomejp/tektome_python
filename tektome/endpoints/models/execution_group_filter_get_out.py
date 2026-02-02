from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_category_types import ApprovalCategoryTypes
from ..models.execution_review_status import ExecutionReviewStatus
from ..models.process_type_choices import ProcessTypeChoices
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_attributes_extracted_filter_options import EntityAttributesExtractedFilterOptions
    from ..models.file_attributes_extracted_filter_options import FileAttributesExtractedFilterOptions
    from ..models.process_filter_options import ProcessFilterOptions
    from ..models.target_model_entity_filter_options import TargetModelEntityFilterOptions


T = TypeVar("T", bound="ExecutionGroupFilterGetOut")


@_attrs_define
class ExecutionGroupFilterGetOut:
    """
    Attributes:
        process (list[ProcessFilterOptions]):
        process_type (list[ProcessTypeChoices]):
        target_files (list[TargetModelEntityFilterOptions]):
        target_entities (list[TargetModelEntityFilterOptions]):
        file_attributes_extracted (list[FileAttributesExtractedFilterOptions]):
        entity_attributes_extracted (list[EntityAttributesExtractedFilterOptions]):
        category (list[ApprovalCategoryTypes] | Unset):
        approval_review_status (list[ExecutionReviewStatus] | Unset):
    """

    process: list[ProcessFilterOptions]
    process_type: list[ProcessTypeChoices]
    target_files: list[TargetModelEntityFilterOptions]
    target_entities: list[TargetModelEntityFilterOptions]
    file_attributes_extracted: list[FileAttributesExtractedFilterOptions]
    entity_attributes_extracted: list[EntityAttributesExtractedFilterOptions]
    category: list[ApprovalCategoryTypes] | Unset = UNSET
    approval_review_status: list[ExecutionReviewStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process = []
        for process_item_data in self.process:
            process_item = process_item_data.to_dict()
            process.append(process_item)

        process_type = []
        for process_type_item_data in self.process_type:
            process_type_item = process_type_item_data.value
            process_type.append(process_type_item)

        target_files = []
        for target_files_item_data in self.target_files:
            target_files_item = target_files_item_data.to_dict()
            target_files.append(target_files_item)

        target_entities = []
        for target_entities_item_data in self.target_entities:
            target_entities_item = target_entities_item_data.to_dict()
            target_entities.append(target_entities_item)

        file_attributes_extracted = []
        for file_attributes_extracted_item_data in self.file_attributes_extracted:
            file_attributes_extracted_item = file_attributes_extracted_item_data.to_dict()
            file_attributes_extracted.append(file_attributes_extracted_item)

        entity_attributes_extracted = []
        for entity_attributes_extracted_item_data in self.entity_attributes_extracted:
            entity_attributes_extracted_item = entity_attributes_extracted_item_data.to_dict()
            entity_attributes_extracted.append(entity_attributes_extracted_item)

        category: list[str] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.value
                category.append(category_item)

        approval_review_status: list[str] | Unset = UNSET
        if not isinstance(self.approval_review_status, Unset):
            approval_review_status = []
            for approval_review_status_item_data in self.approval_review_status:
                approval_review_status_item = approval_review_status_item_data.value
                approval_review_status.append(approval_review_status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process": process,
                "process_type": process_type,
                "target_files": target_files,
                "target_entities": target_entities,
                "file_attributes_extracted": file_attributes_extracted,
                "entity_attributes_extracted": entity_attributes_extracted,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if approval_review_status is not UNSET:
            field_dict["approval_review_status"] = approval_review_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_attributes_extracted_filter_options import EntityAttributesExtractedFilterOptions
        from ..models.file_attributes_extracted_filter_options import FileAttributesExtractedFilterOptions
        from ..models.process_filter_options import ProcessFilterOptions
        from ..models.target_model_entity_filter_options import TargetModelEntityFilterOptions

        d = dict(src_dict)
        process = []
        _process = d.pop("process")
        for process_item_data in _process:
            process_item = ProcessFilterOptions.from_dict(process_item_data)

            process.append(process_item)

        process_type = []
        _process_type = d.pop("process_type")
        for process_type_item_data in _process_type:
            process_type_item = ProcessTypeChoices(process_type_item_data)

            process_type.append(process_type_item)

        target_files = []
        _target_files = d.pop("target_files")
        for target_files_item_data in _target_files:
            target_files_item = TargetModelEntityFilterOptions.from_dict(target_files_item_data)

            target_files.append(target_files_item)

        target_entities = []
        _target_entities = d.pop("target_entities")
        for target_entities_item_data in _target_entities:
            target_entities_item = TargetModelEntityFilterOptions.from_dict(target_entities_item_data)

            target_entities.append(target_entities_item)

        file_attributes_extracted = []
        _file_attributes_extracted = d.pop("file_attributes_extracted")
        for file_attributes_extracted_item_data in _file_attributes_extracted:
            file_attributes_extracted_item = FileAttributesExtractedFilterOptions.from_dict(
                file_attributes_extracted_item_data
            )

            file_attributes_extracted.append(file_attributes_extracted_item)

        entity_attributes_extracted = []
        _entity_attributes_extracted = d.pop("entity_attributes_extracted")
        for entity_attributes_extracted_item_data in _entity_attributes_extracted:
            entity_attributes_extracted_item = EntityAttributesExtractedFilterOptions.from_dict(
                entity_attributes_extracted_item_data
            )

            entity_attributes_extracted.append(entity_attributes_extracted_item)

        _category = d.pop("category", UNSET)
        category: list[ApprovalCategoryTypes] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = ApprovalCategoryTypes(category_item_data)

                category.append(category_item)

        _approval_review_status = d.pop("approval_review_status", UNSET)
        approval_review_status: list[ExecutionReviewStatus] | Unset = UNSET
        if _approval_review_status is not UNSET:
            approval_review_status = []
            for approval_review_status_item_data in _approval_review_status:
                approval_review_status_item = ExecutionReviewStatus(approval_review_status_item_data)

                approval_review_status.append(approval_review_status_item)

        execution_group_filter_get_out = cls(
            process=process,
            process_type=process_type,
            target_files=target_files,
            target_entities=target_entities,
            file_attributes_extracted=file_attributes_extracted,
            entity_attributes_extracted=entity_attributes_extracted,
            category=category,
            approval_review_status=approval_review_status,
        )

        execution_group_filter_get_out.additional_properties = d
        return execution_group_filter_get_out

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
