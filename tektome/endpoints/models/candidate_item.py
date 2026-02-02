from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.candidate_item_kind import CandidateItemKind

if TYPE_CHECKING:
    from ..models.attribute_candidate_payload import AttributeCandidatePayload
    from ..models.file_upload_candidate_payload import FileUploadCandidatePayload


T = TypeVar("T", bound="CandidateItem")


@_attrs_define
class CandidateItem:
    """
    Attributes:
        data (AttributeCandidatePayload | FileUploadCandidatePayload):
        kind (CandidateItemKind):
    """

    data: AttributeCandidatePayload | FileUploadCandidatePayload
    kind: CandidateItemKind
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attribute_candidate_payload import AttributeCandidatePayload

        data: dict[str, Any]
        if isinstance(self.data, AttributeCandidatePayload):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribute_candidate_payload import AttributeCandidatePayload
        from ..models.file_upload_candidate_payload import FileUploadCandidatePayload

        d = dict(src_dict)

        def _parse_data(data: object) -> AttributeCandidatePayload | FileUploadCandidatePayload:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = AttributeCandidatePayload.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = FileUploadCandidatePayload.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data"))

        kind = CandidateItemKind(d.pop("kind"))

        candidate_item = cls(
            data=data,
            kind=kind,
        )

        candidate_item.additional_properties = d
        return candidate_item

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
