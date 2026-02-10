from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_column import TableColumn
    from ..models.table_metadata_update_request_rename_columns_type_0 import (
        TableMetadataUpdateRequestRenameColumnsType0,
    )


T = TypeVar("T", bound="TableMetadataUpdateRequest")


@_attrs_define
class TableMetadataUpdateRequest:
    """Schema for updating table metadata (columns).

    Operations are applied in order: delete -> rename -> insert -> reorder.

        Attributes:
            delete_columns (list[str] | None | Unset):
            rename_columns (None | TableMetadataUpdateRequestRenameColumnsType0 | Unset):
            insert_columns (list[TableColumn] | None | Unset):
            reorder_columns (list[str] | None | Unset):
    """

    delete_columns: list[str] | None | Unset = UNSET
    rename_columns: None | TableMetadataUpdateRequestRenameColumnsType0 | Unset = UNSET
    insert_columns: list[TableColumn] | None | Unset = UNSET
    reorder_columns: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.table_metadata_update_request_rename_columns_type_0 import (
            TableMetadataUpdateRequestRenameColumnsType0,
        )

        delete_columns: list[str] | None | Unset
        if isinstance(self.delete_columns, Unset):
            delete_columns = UNSET
        elif isinstance(self.delete_columns, list):
            delete_columns = self.delete_columns

        else:
            delete_columns = self.delete_columns

        rename_columns: dict[str, Any] | None | Unset
        if isinstance(self.rename_columns, Unset):
            rename_columns = UNSET
        elif isinstance(self.rename_columns, TableMetadataUpdateRequestRenameColumnsType0):
            rename_columns = self.rename_columns.to_dict()
        else:
            rename_columns = self.rename_columns

        insert_columns: list[dict[str, Any]] | None | Unset
        if isinstance(self.insert_columns, Unset):
            insert_columns = UNSET
        elif isinstance(self.insert_columns, list):
            insert_columns = []
            for insert_columns_type_0_item_data in self.insert_columns:
                insert_columns_type_0_item = insert_columns_type_0_item_data.to_dict()
                insert_columns.append(insert_columns_type_0_item)

        else:
            insert_columns = self.insert_columns

        reorder_columns: list[str] | None | Unset
        if isinstance(self.reorder_columns, Unset):
            reorder_columns = UNSET
        elif isinstance(self.reorder_columns, list):
            reorder_columns = self.reorder_columns

        else:
            reorder_columns = self.reorder_columns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_columns is not UNSET:
            field_dict["delete_columns"] = delete_columns
        if rename_columns is not UNSET:
            field_dict["rename_columns"] = rename_columns
        if insert_columns is not UNSET:
            field_dict["insert_columns"] = insert_columns
        if reorder_columns is not UNSET:
            field_dict["reorder_columns"] = reorder_columns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_column import TableColumn
        from ..models.table_metadata_update_request_rename_columns_type_0 import (
            TableMetadataUpdateRequestRenameColumnsType0,
        )

        d = dict(src_dict)

        def _parse_delete_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                delete_columns_type_0 = cast(list[str], data)

                return delete_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        delete_columns = _parse_delete_columns(d.pop("delete_columns", UNSET))

        def _parse_rename_columns(data: object) -> None | TableMetadataUpdateRequestRenameColumnsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rename_columns_type_0 = TableMetadataUpdateRequestRenameColumnsType0.from_dict(data)

                return rename_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TableMetadataUpdateRequestRenameColumnsType0 | Unset, data)

        rename_columns = _parse_rename_columns(d.pop("rename_columns", UNSET))

        def _parse_insert_columns(data: object) -> list[TableColumn] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                insert_columns_type_0 = []
                _insert_columns_type_0 = data
                for insert_columns_type_0_item_data in _insert_columns_type_0:
                    insert_columns_type_0_item = TableColumn.from_dict(insert_columns_type_0_item_data)

                    insert_columns_type_0.append(insert_columns_type_0_item)

                return insert_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TableColumn] | None | Unset, data)

        insert_columns = _parse_insert_columns(d.pop("insert_columns", UNSET))

        def _parse_reorder_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reorder_columns_type_0 = cast(list[str], data)

                return reorder_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        reorder_columns = _parse_reorder_columns(d.pop("reorder_columns", UNSET))

        table_metadata_update_request = cls(
            delete_columns=delete_columns,
            rename_columns=rename_columns,
            insert_columns=insert_columns,
            reorder_columns=reorder_columns,
        )

        table_metadata_update_request.additional_properties = d
        return table_metadata_update_request

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
