from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embedding_model_enum import EmbeddingModelEnum
from ..models.large_language_model_enum import LargeLanguageModelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents import Documents
    from ..models.file_attribute import FileAttribute


T = TypeVar("T", bound="FileAttributesExtraction")


@_attrs_define
class FileAttributesExtraction:
    """
    Attributes:
        model_name (LargeLanguageModelEnum):
        embedding_model (EmbeddingModelEnum):
        documents (Documents):
        attributes (list[FileAttribute]):
        project_id (None | str | Unset):
        file_id (None | Unset | UUID):
        data_space_id (None | str | Unset):
        system_prompt (None | str | Unset):
        position (str | Unset):  Default: 'auto'.
        skip_vector_upload (bool | Unset):  Default: False.
    """

    model_name: LargeLanguageModelEnum
    embedding_model: EmbeddingModelEnum
    documents: Documents
    attributes: list[FileAttribute]
    project_id: None | str | Unset = UNSET
    file_id: None | Unset | UUID = UNSET
    data_space_id: None | str | Unset = UNSET
    system_prompt: None | str | Unset = UNSET
    position: str | Unset = "auto"
    skip_vector_upload: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name.value

        embedding_model = self.embedding_model.value

        documents = self.documents.to_dict()

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        elif isinstance(self.file_id, UUID):
            file_id = str(self.file_id)
        else:
            file_id = self.file_id

        data_space_id: None | str | Unset
        if isinstance(self.data_space_id, Unset):
            data_space_id = UNSET
        else:
            data_space_id = self.data_space_id

        system_prompt: None | str | Unset
        if isinstance(self.system_prompt, Unset):
            system_prompt = UNSET
        else:
            system_prompt = self.system_prompt

        position = self.position

        skip_vector_upload = self.skip_vector_upload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_name": model_name,
                "embedding_model": embedding_model,
                "documents": documents,
                "attributes": attributes,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if data_space_id is not UNSET:
            field_dict["data_space_id"] = data_space_id
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if position is not UNSET:
            field_dict["position"] = position
        if skip_vector_upload is not UNSET:
            field_dict["skip_vector_upload"] = skip_vector_upload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documents import Documents
        from ..models.file_attribute import FileAttribute

        d = dict(src_dict)
        model_name = LargeLanguageModelEnum(d.pop("model_name"))

        embedding_model = EmbeddingModelEnum(d.pop("embedding_model"))

        documents = Documents.from_dict(d.pop("documents"))

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = FileAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_file_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_id_type_0 = UUID(data)

                return file_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        def _parse_data_space_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_space_id = _parse_data_space_id(d.pop("data_space_id", UNSET))

        def _parse_system_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_prompt = _parse_system_prompt(d.pop("system_prompt", UNSET))

        position = d.pop("position", UNSET)

        skip_vector_upload = d.pop("skip_vector_upload", UNSET)

        file_attributes_extraction = cls(
            model_name=model_name,
            embedding_model=embedding_model,
            documents=documents,
            attributes=attributes,
            project_id=project_id,
            file_id=file_id,
            data_space_id=data_space_id,
            system_prompt=system_prompt,
            position=position,
            skip_vector_upload=skip_vector_upload,
        )

        file_attributes_extraction.additional_properties = d
        return file_attributes_extraction

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
