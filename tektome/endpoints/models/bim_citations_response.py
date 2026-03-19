from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cited_bim_element_schema_response import CitedBIMElementSchemaResponse
    from ..models.user_metadata import UserMetadata


T = TypeVar("T", bound="BIMCitationsResponse")


@_attrs_define
class BIMCitationsResponse:
    """
    Attributes:
        created_by (UserMetadata):
        updated_by (UserMetadata):
        cited_bim_elements (list[CitedBIMElementSchemaResponse]):
        created (datetime.datetime):
        updated (datetime.datetime):
        resource (UUID): This is the cited BIM Resource
        citation_type (Literal['bim_citation'] | Unset):  Default: 'bim_citation'.
        keywords (list[str] | Unset):
        id (None | Unset | UUID):
        title (str | Unset):  Default: ''.
    """

    created_by: UserMetadata
    updated_by: UserMetadata
    cited_bim_elements: list[CitedBIMElementSchemaResponse]
    created: datetime.datetime
    updated: datetime.datetime
    resource: UUID
    citation_type: Literal["bim_citation"] | Unset = "bim_citation"
    keywords: list[str] | Unset = UNSET
    id: None | Unset | UUID = UNSET
    title: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by.to_dict()

        updated_by = self.updated_by.to_dict()

        cited_bim_elements = []
        for cited_bim_elements_item_data in self.cited_bim_elements:
            cited_bim_elements_item = cited_bim_elements_item_data.to_dict()
            cited_bim_elements.append(cited_bim_elements_item)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        resource = str(self.resource)

        citation_type = self.citation_type

        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_by": created_by,
                "updated_by": updated_by,
                "cited_bim_elements": cited_bim_elements,
                "created": created,
                "updated": updated,
                "resource": resource,
            }
        )
        if citation_type is not UNSET:
            field_dict["citation_type"] = citation_type
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cited_bim_element_schema_response import CitedBIMElementSchemaResponse
        from ..models.user_metadata import UserMetadata

        d = dict(src_dict)
        created_by = UserMetadata.from_dict(d.pop("created_by"))

        updated_by = UserMetadata.from_dict(d.pop("updated_by"))

        cited_bim_elements = []
        _cited_bim_elements = d.pop("cited_bim_elements")
        for cited_bim_elements_item_data in _cited_bim_elements:
            cited_bim_elements_item = CitedBIMElementSchemaResponse.from_dict(cited_bim_elements_item_data)

            cited_bim_elements.append(cited_bim_elements_item)

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        resource = UUID(d.pop("resource"))

        citation_type = cast(Literal["bim_citation"] | Unset, d.pop("citation_type", UNSET))
        if citation_type != "bim_citation" and not isinstance(citation_type, Unset):
            raise ValueError(f"citation_type must match const 'bim_citation', got '{citation_type}'")

        keywords = cast(list[str], d.pop("keywords", UNSET))

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

        title = d.pop("title", UNSET)

        bim_citations_response = cls(
            created_by=created_by,
            updated_by=updated_by,
            cited_bim_elements=cited_bim_elements,
            created=created,
            updated=updated,
            resource=resource,
            citation_type=citation_type,
            keywords=keywords,
            id=id,
            title=title,
        )

        bim_citations_response.additional_properties = d
        return bim_citations_response

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
