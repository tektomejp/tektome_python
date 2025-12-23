from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_result_failed import ImportResultFailed


T = TypeVar("T", bound="ImportResult")


@_attrs_define
class ImportResult:
    """Response schema for import operations.

    Attributes:
        success (bool): Overall success status
        imported (list[str] | Unset): IDs of successfully imported items
        updated (list[str] | Unset): IDs of updated items
        skipped (list[str] | Unset): IDs of skipped items
        failed (ImportResultFailed | Unset): Failed items with error messages
        total_processed (int | Unset): Total number of items processed Default: 0.
        duration_ms (int | Unset): Processing duration in milliseconds Default: 0.
    """

    success: bool
    imported: list[str] | Unset = UNSET
    updated: list[str] | Unset = UNSET
    skipped: list[str] | Unset = UNSET
    failed: ImportResultFailed | Unset = UNSET
    total_processed: int | Unset = 0
    duration_ms: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        imported: list[str] | Unset = UNSET
        if not isinstance(self.imported, Unset):
            imported = self.imported

        updated: list[str] | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated

        skipped: list[str] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = self.skipped

        failed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failed, Unset):
            failed = self.failed.to_dict()

        total_processed = self.total_processed

        duration_ms = self.duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if imported is not UNSET:
            field_dict["imported"] = imported
        if updated is not UNSET:
            field_dict["updated"] = updated
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if failed is not UNSET:
            field_dict["failed"] = failed
        if total_processed is not UNSET:
            field_dict["total_processed"] = total_processed
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_result_failed import ImportResultFailed

        d = dict(src_dict)
        success = d.pop("success")

        imported = cast(list[str], d.pop("imported", UNSET))

        updated = cast(list[str], d.pop("updated", UNSET))

        skipped = cast(list[str], d.pop("skipped", UNSET))

        _failed = d.pop("failed", UNSET)
        failed: ImportResultFailed | Unset
        if isinstance(_failed, Unset):
            failed = UNSET
        else:
            failed = ImportResultFailed.from_dict(_failed)

        total_processed = d.pop("total_processed", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        import_result = cls(
            success=success,
            imported=imported,
            updated=updated,
            skipped=skipped,
            failed=failed,
            total_processed=total_processed,
            duration_ms=duration_ms,
        )

        import_result.additional_properties = d
        return import_result

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
