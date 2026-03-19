from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.citations_schema_out import CitationsSchemaOut


T = TypeVar("T", bound="AttributeReviewedData")


@_attrs_define
class AttributeReviewedData:
    """Reviewed data for attribute candidates — matches AttributeGetOut keys + citations.

    Attributes:
        id (None | Unset | UUID):
        name (None | str | Unset):
        value (Any | Unset): The value of the attribute.
        is_locked (bool | None | Unset):
        extraction_status (None | str | Unset):
        creation_method (None | str | Unset):
        error_message (None | str | Unset):
        type_ (None | str | Unset):
        extraction_reasoning (None | str | Unset):
        citations (CitationsSchemaOut | None | Unset):
    """

    id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    value: Any | Unset = UNSET
    is_locked: bool | None | Unset = UNSET
    extraction_status: None | str | Unset = UNSET
    creation_method: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    extraction_reasoning: None | str | Unset = UNSET
    citations: CitationsSchemaOut | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.citations_schema_out import CitationsSchemaOut

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        value = self.value

        is_locked: bool | None | Unset
        if isinstance(self.is_locked, Unset):
            is_locked = UNSET
        else:
            is_locked = self.is_locked

        extraction_status: None | str | Unset
        if isinstance(self.extraction_status, Unset):
            extraction_status = UNSET
        else:
            extraction_status = self.extraction_status

        creation_method: None | str | Unset
        if isinstance(self.creation_method, Unset):
            creation_method = UNSET
        else:
            creation_method = self.creation_method

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        extraction_reasoning: None | str | Unset
        if isinstance(self.extraction_reasoning, Unset):
            extraction_reasoning = UNSET
        else:
            extraction_reasoning = self.extraction_reasoning

        citations: dict[str, Any] | None | Unset
        if isinstance(self.citations, Unset):
            citations = UNSET
        elif isinstance(self.citations, CitationsSchemaOut):
            citations = self.citations.to_dict()
        else:
            citations = self.citations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked
        if extraction_status is not UNSET:
            field_dict["extraction_status"] = extraction_status
        if creation_method is not UNSET:
            field_dict["creation_method"] = creation_method
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if type_ is not UNSET:
            field_dict["type"] = type_
        if extraction_reasoning is not UNSET:
            field_dict["extraction_reasoning"] = extraction_reasoning
        if citations is not UNSET:
            field_dict["citations"] = citations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.citations_schema_out import CitationsSchemaOut

        d = dict(src_dict)

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        value = d.pop("value", UNSET)

        def _parse_is_locked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_locked = _parse_is_locked(d.pop("is_locked", UNSET))

        def _parse_extraction_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extraction_status = _parse_extraction_status(d.pop("extraction_status", UNSET))

        def _parse_creation_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        creation_method = _parse_creation_method(d.pop("creation_method", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_extraction_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extraction_reasoning = _parse_extraction_reasoning(d.pop("extraction_reasoning", UNSET))

        def _parse_citations(data: object) -> CitationsSchemaOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                citations_type_0 = CitationsSchemaOut.from_dict(data)

                return citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CitationsSchemaOut | None | Unset, data)

        citations = _parse_citations(d.pop("citations", UNSET))

        attribute_reviewed_data = cls(
            id=id,
            name=name,
            value=value,
            is_locked=is_locked,
            extraction_status=extraction_status,
            creation_method=creation_method,
            error_message=error_message,
            type_=type_,
            extraction_reasoning=extraction_reasoning,
            citations=citations,
        )

        attribute_reviewed_data.additional_properties = d
        return attribute_reviewed_data

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
