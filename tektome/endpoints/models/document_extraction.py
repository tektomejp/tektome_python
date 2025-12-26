from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_type_enum import DataTypeEnum
from ..models.document_extractor_enum import DocumentExtractorEnum
from ..models.document_source_enum import DocumentSourceEnum
from ..models.embedding_model_enum import EmbeddingModelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_extraction_callback_payload import DocumentExtractionCallbackPayload


T = TypeVar("T", bound="DocumentExtraction")


@_attrs_define
class DocumentExtraction:
    """Model for handling document extraction configuration and metadata.

    Attributes:
        project_id (str): The ID of the project associated with this document extraction.
        data_type (DataTypeEnum):
        data_type_version (str): The version of the data type, must match the allowed versions for the specified data
            type.
        embedding_model (EmbeddingModelEnum):
        data_space_id (None | str | Unset): The ID of the data space, optional field.
        file_id (UUID | Unset): The unique identifier for the file, automatically generated if not provided.
        document_source (DocumentSourceEnum | Unset):  Default: DocumentSourceEnum.TEKTOME.
        document_url (None | str | Unset): The URL where the document can be accessed, required if document_source is
            'tektome'.
        document_loader (None | Unset): Loader for the document; currently not implemented (set to None).
        create_ai_search_index (bool | Unset): Flag indicating whether an AI search index should be created for the
            document. Default: False.
        document_extractor (DocumentExtractorEnum | Unset):  Default: DocumentExtractorEnum.AZURE_FORM_RECOGNIZER.
        upsert_batch_size (int | Unset): The batch size for upsert operations to Azure AI search, default is 5. Default:
            5.
        group_chunk_batch_size (int | Unset): The batch size for grouping document chunks to create chunk-groups,
            default is 5. Default: 5.
        backup (bool | Unset): Flag indicating whether to keep a backup of the ocr json to blob storage, default is
            True. Default: True.
        callback_url (None | str | Unset): The URL to send callbacks to after processing is complete.
        callback_payload (DocumentExtractionCallbackPayload | Unset): The payload sent along with the callback, default
            is an empty dictionary.
        skip_vector_upload (bool | Unset): Flag indicating whether to skip vector uploads to Azure AI search chunk-group
            index. Default: False.
        skip_page_summary (bool | Unset): Flag indicating whether to skip generating a summary for each page, default is
            True. Default: True.
    """

    project_id: str
    data_type: DataTypeEnum
    data_type_version: str
    embedding_model: EmbeddingModelEnum
    data_space_id: None | str | Unset = UNSET
    file_id: UUID | Unset = UNSET
    document_source: DocumentSourceEnum | Unset = DocumentSourceEnum.TEKTOME
    document_url: None | str | Unset = UNSET
    document_loader: None | Unset = UNSET
    create_ai_search_index: bool | Unset = False
    document_extractor: DocumentExtractorEnum | Unset = DocumentExtractorEnum.AZURE_FORM_RECOGNIZER
    upsert_batch_size: int | Unset = 5
    group_chunk_batch_size: int | Unset = 5
    backup: bool | Unset = True
    callback_url: None | str | Unset = UNSET
    callback_payload: DocumentExtractionCallbackPayload | Unset = UNSET
    skip_vector_upload: bool | Unset = False
    skip_page_summary: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        data_type = self.data_type.value

        data_type_version = self.data_type_version

        embedding_model = self.embedding_model.value

        data_space_id: None | str | Unset
        if isinstance(self.data_space_id, Unset):
            data_space_id = UNSET
        else:
            data_space_id = self.data_space_id

        file_id: str | Unset = UNSET
        if not isinstance(self.file_id, Unset):
            file_id = str(self.file_id)

        document_source: str | Unset = UNSET
        if not isinstance(self.document_source, Unset):
            document_source = self.document_source.value

        document_url: None | str | Unset
        if isinstance(self.document_url, Unset):
            document_url = UNSET
        else:
            document_url = self.document_url

        document_loader = self.document_loader

        create_ai_search_index = self.create_ai_search_index

        document_extractor: str | Unset = UNSET
        if not isinstance(self.document_extractor, Unset):
            document_extractor = self.document_extractor.value

        upsert_batch_size = self.upsert_batch_size

        group_chunk_batch_size = self.group_chunk_batch_size

        backup = self.backup

        callback_url: None | str | Unset
        if isinstance(self.callback_url, Unset):
            callback_url = UNSET
        else:
            callback_url = self.callback_url

        callback_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback_payload, Unset):
            callback_payload = self.callback_payload.to_dict()

        skip_vector_upload = self.skip_vector_upload

        skip_page_summary = self.skip_page_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "data_type": data_type,
                "data_type_version": data_type_version,
                "embedding_model": embedding_model,
            }
        )
        if data_space_id is not UNSET:
            field_dict["data_space_id"] = data_space_id
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if document_source is not UNSET:
            field_dict["document_source"] = document_source
        if document_url is not UNSET:
            field_dict["document_url"] = document_url
        if document_loader is not UNSET:
            field_dict["document_loader"] = document_loader
        if create_ai_search_index is not UNSET:
            field_dict["create_ai_search_index"] = create_ai_search_index
        if document_extractor is not UNSET:
            field_dict["document_extractor"] = document_extractor
        if upsert_batch_size is not UNSET:
            field_dict["upsert_batch_size"] = upsert_batch_size
        if group_chunk_batch_size is not UNSET:
            field_dict["group_chunk_batch_size"] = group_chunk_batch_size
        if backup is not UNSET:
            field_dict["backup"] = backup
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url
        if callback_payload is not UNSET:
            field_dict["callback_payload"] = callback_payload
        if skip_vector_upload is not UNSET:
            field_dict["skip_vector_upload"] = skip_vector_upload
        if skip_page_summary is not UNSET:
            field_dict["skip_page_summary"] = skip_page_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_extraction_callback_payload import DocumentExtractionCallbackPayload

        d = dict(src_dict)
        project_id = d.pop("project_id")

        data_type = DataTypeEnum(d.pop("data_type"))

        data_type_version = d.pop("data_type_version")

        embedding_model = EmbeddingModelEnum(d.pop("embedding_model"))

        def _parse_data_space_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_space_id = _parse_data_space_id(d.pop("data_space_id", UNSET))

        _file_id = d.pop("file_id", UNSET)
        file_id: UUID | Unset
        if isinstance(_file_id, Unset):
            file_id = UNSET
        else:
            file_id = UUID(_file_id)

        _document_source = d.pop("document_source", UNSET)
        document_source: DocumentSourceEnum | Unset
        if isinstance(_document_source, Unset):
            document_source = UNSET
        else:
            document_source = DocumentSourceEnum(_document_source)

        def _parse_document_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_url = _parse_document_url(d.pop("document_url", UNSET))

        document_loader = d.pop("document_loader", UNSET)

        create_ai_search_index = d.pop("create_ai_search_index", UNSET)

        _document_extractor = d.pop("document_extractor", UNSET)
        document_extractor: DocumentExtractorEnum | Unset
        if isinstance(_document_extractor, Unset):
            document_extractor = UNSET
        else:
            document_extractor = DocumentExtractorEnum(_document_extractor)

        upsert_batch_size = d.pop("upsert_batch_size", UNSET)

        group_chunk_batch_size = d.pop("group_chunk_batch_size", UNSET)

        backup = d.pop("backup", UNSET)

        def _parse_callback_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        callback_url = _parse_callback_url(d.pop("callback_url", UNSET))

        _callback_payload = d.pop("callback_payload", UNSET)
        callback_payload: DocumentExtractionCallbackPayload | Unset
        if isinstance(_callback_payload, Unset):
            callback_payload = UNSET
        else:
            callback_payload = DocumentExtractionCallbackPayload.from_dict(_callback_payload)

        skip_vector_upload = d.pop("skip_vector_upload", UNSET)

        skip_page_summary = d.pop("skip_page_summary", UNSET)

        document_extraction = cls(
            project_id=project_id,
            data_type=data_type,
            data_type_version=data_type_version,
            embedding_model=embedding_model,
            data_space_id=data_space_id,
            file_id=file_id,
            document_source=document_source,
            document_url=document_url,
            document_loader=document_loader,
            create_ai_search_index=create_ai_search_index,
            document_extractor=document_extractor,
            upsert_batch_size=upsert_batch_size,
            group_chunk_batch_size=group_chunk_batch_size,
            backup=backup,
            callback_url=callback_url,
            callback_payload=callback_payload,
            skip_vector_upload=skip_vector_upload,
            skip_page_summary=skip_page_summary,
        )

        document_extraction.additional_properties = d
        return document_extraction

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
