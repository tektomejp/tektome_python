from __future__ import annotations

import datetime
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.chunk import Chunk


T = TypeVar("T", bound="ChunkGroupComponentSchemaGetOut")


@_attrs_define
class ChunkGroupComponentSchemaGetOut:
    """
    Attributes:
        chunks (list[Chunk]):
        created (datetime.datetime):
        updated (datetime.datetime):
        resource (UUID):
        id (None | Unset | UUID):
        lemma_vector_file (None | str | Unset):
        lemma_vector_binary (File | None | Unset):
        reading_vector_file (None | str | Unset):
        reading_vector_binary (File | None | Unset):
    """

    chunks: list[Chunk]
    created: datetime.datetime
    updated: datetime.datetime
    resource: UUID
    id: None | Unset | UUID = UNSET
    lemma_vector_file: None | str | Unset = UNSET
    lemma_vector_binary: File | None | Unset = UNSET
    reading_vector_file: None | str | Unset = UNSET
    reading_vector_binary: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chunks = []
        for chunks_item_data in self.chunks:
            chunks_item = chunks_item_data.to_dict()
            chunks.append(chunks_item)

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        resource = str(self.resource)

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        lemma_vector_file: None | str | Unset
        if isinstance(self.lemma_vector_file, Unset):
            lemma_vector_file = UNSET
        else:
            lemma_vector_file = self.lemma_vector_file

        lemma_vector_binary: FileTypes | None | Unset
        if isinstance(self.lemma_vector_binary, Unset):
            lemma_vector_binary = UNSET
        elif isinstance(self.lemma_vector_binary, File):
            lemma_vector_binary = self.lemma_vector_binary.to_tuple()

        else:
            lemma_vector_binary = self.lemma_vector_binary

        reading_vector_file: None | str | Unset
        if isinstance(self.reading_vector_file, Unset):
            reading_vector_file = UNSET
        else:
            reading_vector_file = self.reading_vector_file

        reading_vector_binary: FileTypes | None | Unset
        if isinstance(self.reading_vector_binary, Unset):
            reading_vector_binary = UNSET
        elif isinstance(self.reading_vector_binary, File):
            reading_vector_binary = self.reading_vector_binary.to_tuple()

        else:
            reading_vector_binary = self.reading_vector_binary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunks": chunks,
                "created": created,
                "updated": updated,
                "resource": resource,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if lemma_vector_file is not UNSET:
            field_dict["lemma_vector_file"] = lemma_vector_file
        if lemma_vector_binary is not UNSET:
            field_dict["lemma_vector_binary"] = lemma_vector_binary
        if reading_vector_file is not UNSET:
            field_dict["reading_vector_file"] = reading_vector_file
        if reading_vector_binary is not UNSET:
            field_dict["reading_vector_binary"] = reading_vector_binary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk import Chunk

        d = dict(src_dict)
        chunks = []
        _chunks = d.pop("chunks")
        for chunks_item_data in _chunks:
            chunks_item = Chunk.from_dict(chunks_item_data)

            chunks.append(chunks_item)

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        resource = UUID(d.pop("resource"))

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

        def _parse_lemma_vector_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lemma_vector_file = _parse_lemma_vector_file(d.pop("lemma_vector_file", UNSET))

        def _parse_lemma_vector_binary(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                lemma_vector_binary_type_0 = File(payload=BytesIO(data))

                return lemma_vector_binary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        lemma_vector_binary = _parse_lemma_vector_binary(d.pop("lemma_vector_binary", UNSET))

        def _parse_reading_vector_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reading_vector_file = _parse_reading_vector_file(d.pop("reading_vector_file", UNSET))

        def _parse_reading_vector_binary(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                reading_vector_binary_type_0 = File(payload=BytesIO(data))

                return reading_vector_binary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        reading_vector_binary = _parse_reading_vector_binary(d.pop("reading_vector_binary", UNSET))

        chunk_group_component_schema_get_out = cls(
            chunks=chunks,
            created=created,
            updated=updated,
            resource=resource,
            id=id,
            lemma_vector_file=lemma_vector_file,
            lemma_vector_binary=lemma_vector_binary,
            reading_vector_file=reading_vector_file,
            reading_vector_binary=reading_vector_binary,
        )

        chunk_group_component_schema_get_out.additional_properties = d
        return chunk_group_component_schema_get_out

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
