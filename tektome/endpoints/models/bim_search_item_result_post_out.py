from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bim_search_item_result_post_out_file_content_type_0 import BimSearchItemResultPostOutFileContentType0


T = TypeVar("T", bound="BimSearchItemResultPostOut")


@_attrs_define
class BimSearchItemResultPostOut:
    """Schema for individual BIM search result item.

    Attributes:
        id (str):
        created (str):
        updated (str):
        project_ids (list[str]):
        score (float):
        file_content (BimSearchItemResultPostOutFileContentType0 | None | Unset):
    """

    id: str
    created: str
    updated: str
    project_ids: list[str]
    score: float
    file_content: BimSearchItemResultPostOutFileContentType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bim_search_item_result_post_out_file_content_type_0 import (
            BimSearchItemResultPostOutFileContentType0,
        )

        id = self.id

        created = self.created

        updated = self.updated

        project_ids = self.project_ids

        score = self.score

        file_content: dict[str, Any] | None | Unset
        if isinstance(self.file_content, Unset):
            file_content = UNSET
        elif isinstance(self.file_content, BimSearchItemResultPostOutFileContentType0):
            file_content = self.file_content.to_dict()
        else:
            file_content = self.file_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "updated": updated,
                "project_ids": project_ids,
                "score": score,
            }
        )
        if file_content is not UNSET:
            field_dict["file_content"] = file_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_search_item_result_post_out_file_content_type_0 import (
            BimSearchItemResultPostOutFileContentType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        created = d.pop("created")

        updated = d.pop("updated")

        project_ids = cast(list[str], d.pop("project_ids"))

        score = d.pop("score")

        def _parse_file_content(data: object) -> BimSearchItemResultPostOutFileContentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                file_content_type_0 = BimSearchItemResultPostOutFileContentType0.from_dict(data)

                return file_content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BimSearchItemResultPostOutFileContentType0 | None | Unset, data)

        file_content = _parse_file_content(d.pop("file_content", UNSET))

        bim_search_item_result_post_out = cls(
            id=id,
            created=created,
            updated=updated,
            project_ids=project_ids,
            score=score,
            file_content=file_content,
        )

        bim_search_item_result_post_out.additional_properties = d
        return bim_search_item_result_post_out

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
