from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CitedBIMElementSchemaResponse")


@_attrs_define
class CitedBIMElementSchemaResponse:
    """
    Attributes:
        bim_project (UUID): The BIM project cited as a source in the citation.
        id (None | Unset | UUID):
        bim_object (None | str | Unset): The specific BIM object within the cited BIM project that is relevant to the
            citation.
    """

    bim_project: UUID
    id: None | Unset | UUID = UNSET
    bim_object: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bim_project = str(self.bim_project)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        bim_object: None | str | Unset
        if isinstance(self.bim_object, Unset):
            bim_object = UNSET
        else:
            bim_object = self.bim_object

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bim_project": bim_project,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if bim_object is not UNSET:
            field_dict["bim_object"] = bim_object

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bim_project = UUID(d.pop("bim_project"))

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

        def _parse_bim_object(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bim_object = _parse_bim_object(d.pop("bim_object", UNSET))

        cited_bim_element_schema_response = cls(
            bim_project=bim_project,
            id=id,
            bim_object=bim_object,
        )

        cited_bim_element_schema_response.additional_properties = d
        return cited_bim_element_schema_response

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
