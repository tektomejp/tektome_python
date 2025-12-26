from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_extraction_status import DocumentExtractionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_callback_payload import DocumentCallbackPayload
    from ..models.document_extracted_content_type_0 import DocumentExtractedContentType0
    from ..models.document_log import DocumentLog


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """Document dataclass

    Attributes:
        file_id (UUID | Unset):
        url (None | str | Unset):
        extractor (None | str | Unset):
        extracted_content (DocumentExtractedContentType0 | None | Unset):
        log (DocumentLog | Unset):
        callback_payload (DocumentCallbackPayload | Unset):
        extraction_status (DocumentExtractionStatus | Unset): Document extraction status Default:
            DocumentExtractionStatus.IN_PROGRESS.
    """

    file_id: UUID | Unset = UNSET
    url: None | str | Unset = UNSET
    extractor: None | str | Unset = UNSET
    extracted_content: DocumentExtractedContentType0 | None | Unset = UNSET
    log: DocumentLog | Unset = UNSET
    callback_payload: DocumentCallbackPayload | Unset = UNSET
    extraction_status: DocumentExtractionStatus | Unset = DocumentExtractionStatus.IN_PROGRESS
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.document_extracted_content_type_0 import DocumentExtractedContentType0

        file_id: str | Unset = UNSET
        if not isinstance(self.file_id, Unset):
            file_id = str(self.file_id)

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        extractor: None | str | Unset
        if isinstance(self.extractor, Unset):
            extractor = UNSET
        else:
            extractor = self.extractor

        extracted_content: dict[str, Any] | None | Unset
        if isinstance(self.extracted_content, Unset):
            extracted_content = UNSET
        elif isinstance(self.extracted_content, DocumentExtractedContentType0):
            extracted_content = self.extracted_content.to_dict()
        else:
            extracted_content = self.extracted_content

        log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log, Unset):
            log = self.log.to_dict()

        callback_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback_payload, Unset):
            callback_payload = self.callback_payload.to_dict()

        extraction_status: str | Unset = UNSET
        if not isinstance(self.extraction_status, Unset):
            extraction_status = self.extraction_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if url is not UNSET:
            field_dict["url"] = url
        if extractor is not UNSET:
            field_dict["extractor"] = extractor
        if extracted_content is not UNSET:
            field_dict["extracted_content"] = extracted_content
        if log is not UNSET:
            field_dict["log"] = log
        if callback_payload is not UNSET:
            field_dict["callback_payload"] = callback_payload
        if extraction_status is not UNSET:
            field_dict["extraction_status"] = extraction_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_callback_payload import DocumentCallbackPayload
        from ..models.document_extracted_content_type_0 import DocumentExtractedContentType0
        from ..models.document_log import DocumentLog

        d = dict(src_dict)
        _file_id = d.pop("file_id", UNSET)
        file_id: UUID | Unset
        if isinstance(_file_id, Unset):
            file_id = UNSET
        else:
            file_id = UUID(_file_id)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_extractor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extractor = _parse_extractor(d.pop("extractor", UNSET))

        def _parse_extracted_content(data: object) -> DocumentExtractedContentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extracted_content_type_0 = DocumentExtractedContentType0.from_dict(data)

                return extracted_content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DocumentExtractedContentType0 | None | Unset, data)

        extracted_content = _parse_extracted_content(d.pop("extracted_content", UNSET))

        _log = d.pop("log", UNSET)
        log: DocumentLog | Unset
        if isinstance(_log, Unset):
            log = UNSET
        else:
            log = DocumentLog.from_dict(_log)

        _callback_payload = d.pop("callback_payload", UNSET)
        callback_payload: DocumentCallbackPayload | Unset
        if isinstance(_callback_payload, Unset):
            callback_payload = UNSET
        else:
            callback_payload = DocumentCallbackPayload.from_dict(_callback_payload)

        _extraction_status = d.pop("extraction_status", UNSET)
        extraction_status: DocumentExtractionStatus | Unset
        if isinstance(_extraction_status, Unset):
            extraction_status = UNSET
        else:
            extraction_status = DocumentExtractionStatus(_extraction_status)

        document = cls(
            file_id=file_id,
            url=url,
            extractor=extractor,
            extracted_content=extracted_content,
            log=log,
            callback_payload=callback_payload,
            extraction_status=extraction_status,
        )

        document.additional_properties = d
        return document

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
