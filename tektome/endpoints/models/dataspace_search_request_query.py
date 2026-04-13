from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataspaceSearchRequestQuery")


@_attrs_define
class DataspaceSearchRequestQuery:
    """
    Attributes:
        user_ids (list[UUID] | Unset): Filter by creator user IDs.
        date_from (datetime.date | None | Unset): Filter search requests created on or after this date (inclusive).
        date_to (datetime.date | None | Unset): Filter search requests created on or before this date (inclusive, end of
            day).
        search (None | str | Unset): Keyword search across snapshot tag name, keywords, highlight keywords, and snapshot
            filter configuration names.
    """

    user_ids: list[UUID] | Unset = UNSET
    date_from: datetime.date | None | Unset = UNSET
    date_to: datetime.date | None | Unset = UNSET
    search: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = []
            for user_ids_item_data in self.user_ids:
                user_ids_item = str(user_ids_item_data)
                user_ids.append(user_ids_item)

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        elif isinstance(self.date_from, datetime.date):
            date_from = self.date_from.isoformat()
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        elif isinstance(self.date_to, datetime.date):
            date_to = self.date_to.isoformat()
        else:
            date_to = self.date_to

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if search is not UNSET:
            field_dict["search"] = search

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _user_ids = d.pop("user_ids", UNSET)
        user_ids: list[UUID] | Unset = UNSET
        if _user_ids is not UNSET:
            user_ids = []
            for user_ids_item_data in _user_ids:
                user_ids_item = UUID(user_ids_item_data)

                user_ids.append(user_ids_item)

        def _parse_date_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_from_type_0 = isoparse(data).date()

                return date_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_to_type_0 = isoparse(data).date()

                return date_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        dataspace_search_request_query = cls(
            user_ids=user_ids,
            date_from=date_from,
            date_to=date_to,
            search=search,
        )

        dataspace_search_request_query.additional_properties = d
        return dataspace_search_request_query

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
