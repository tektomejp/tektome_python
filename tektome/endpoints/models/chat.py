from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_extractor_enum import DocumentExtractorEnum
from ..models.large_language_model_enum import LargeLanguageModelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_chunks_type_0_item import ChatChunksType0Item
    from ..models.documents import Documents


T = TypeVar("T", bound="Chat")


@_attrs_define
class Chat:
    """
    Attributes:
        message (str):
        documents (Documents):
        system_prompt (None | str | Unset):
        model_name (LargeLanguageModelEnum | Unset):  Default: LargeLanguageModelEnum.OPENAI_GPT_4_OMNI.
        conversation_id (UUID | Unset):
        document_extractor (DocumentExtractorEnum | Unset):  Default: DocumentExtractorEnum.AZURE_FORM_RECOGNIZER.
        chunks (list[ChatChunksType0Item] | None | Unset):
        rerank_take (int | None | Unset):
    """

    message: str
    documents: Documents
    system_prompt: None | str | Unset = UNSET
    model_name: LargeLanguageModelEnum | Unset = LargeLanguageModelEnum.OPENAI_GPT_4_OMNI
    conversation_id: UUID | Unset = UNSET
    document_extractor: DocumentExtractorEnum | Unset = DocumentExtractorEnum.AZURE_FORM_RECOGNIZER
    chunks: list[ChatChunksType0Item] | None | Unset = UNSET
    rerank_take: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        documents = self.documents.to_dict()

        system_prompt: None | str | Unset
        if isinstance(self.system_prompt, Unset):
            system_prompt = UNSET
        else:
            system_prompt = self.system_prompt

        model_name: str | Unset = UNSET
        if not isinstance(self.model_name, Unset):
            model_name = self.model_name.value

        conversation_id: str | Unset = UNSET
        if not isinstance(self.conversation_id, Unset):
            conversation_id = str(self.conversation_id)

        document_extractor: str | Unset = UNSET
        if not isinstance(self.document_extractor, Unset):
            document_extractor = self.document_extractor.value

        chunks: list[dict[str, Any]] | None | Unset
        if isinstance(self.chunks, Unset):
            chunks = UNSET
        elif isinstance(self.chunks, list):
            chunks = []
            for chunks_type_0_item_data in self.chunks:
                chunks_type_0_item = chunks_type_0_item_data.to_dict()
                chunks.append(chunks_type_0_item)

        else:
            chunks = self.chunks

        rerank_take: int | None | Unset
        if isinstance(self.rerank_take, Unset):
            rerank_take = UNSET
        else:
            rerank_take = self.rerank_take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "documents": documents,
            }
        )
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if document_extractor is not UNSET:
            field_dict["document_extractor"] = document_extractor
        if chunks is not UNSET:
            field_dict["chunks"] = chunks
        if rerank_take is not UNSET:
            field_dict["rerank_take"] = rerank_take

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_chunks_type_0_item import ChatChunksType0Item
        from ..models.documents import Documents

        d = dict(src_dict)
        message = d.pop("message")

        documents = Documents.from_dict(d.pop("documents"))

        def _parse_system_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_prompt = _parse_system_prompt(d.pop("system_prompt", UNSET))

        _model_name = d.pop("model_name", UNSET)
        model_name: LargeLanguageModelEnum | Unset
        if isinstance(_model_name, Unset):
            model_name = UNSET
        else:
            model_name = LargeLanguageModelEnum(_model_name)

        _conversation_id = d.pop("conversation_id", UNSET)
        conversation_id: UUID | Unset
        if isinstance(_conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = UUID(_conversation_id)

        _document_extractor = d.pop("document_extractor", UNSET)
        document_extractor: DocumentExtractorEnum | Unset
        if isinstance(_document_extractor, Unset):
            document_extractor = UNSET
        else:
            document_extractor = DocumentExtractorEnum(_document_extractor)

        def _parse_chunks(data: object) -> list[ChatChunksType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chunks_type_0 = []
                _chunks_type_0 = data
                for chunks_type_0_item_data in _chunks_type_0:
                    chunks_type_0_item = ChatChunksType0Item.from_dict(chunks_type_0_item_data)

                    chunks_type_0.append(chunks_type_0_item)

                return chunks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatChunksType0Item] | None | Unset, data)

        chunks = _parse_chunks(d.pop("chunks", UNSET))

        def _parse_rerank_take(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rerank_take = _parse_rerank_take(d.pop("rerank_take", UNSET))

        chat = cls(
            message=message,
            documents=documents,
            system_prompt=system_prompt,
            model_name=model_name,
            conversation_id=conversation_id,
            document_extractor=document_extractor,
            chunks=chunks,
            rerank_take=rerank_take,
        )

        chat.additional_properties = d
        return chat

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
