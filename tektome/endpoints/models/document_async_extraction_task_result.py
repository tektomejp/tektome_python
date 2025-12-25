from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document import Document


T = TypeVar("T", bound="DocumentAsyncExtractionTaskResult")


@_attrs_define
class DocumentAsyncExtractionTaskResult:
    """
    Attributes:
        task_id (str):
        task_status (str):
        task_result (Document | None | Unset):
    """

    task_id: str
    task_status: str
    task_result: Document | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.document import Document

        task_id = self.task_id

        task_status = self.task_status

        task_result: dict[str, Any] | None | Unset
        if isinstance(self.task_result, Unset):
            task_result = UNSET
        elif isinstance(self.task_result, Document):
            task_result = self.task_result.to_dict()
        else:
            task_result = self.task_result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "task_status": task_status,
            }
        )
        if task_result is not UNSET:
            field_dict["task_result"] = task_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document import Document

        d = dict(src_dict)
        task_id = d.pop("task_id")

        task_status = d.pop("task_status")

        def _parse_task_result(data: object) -> Document | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_result_type_0 = Document.from_dict(data)

                return task_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Document | None | Unset, data)

        task_result = _parse_task_result(d.pop("task_result", UNSET))

        document_async_extraction_task_result = cls(
            task_id=task_id,
            task_status=task_status,
            task_result=task_result,
        )

        document_async_extraction_task_result.additional_properties = d
        return document_async_extraction_task_result

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
