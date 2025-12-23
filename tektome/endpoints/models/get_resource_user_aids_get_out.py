from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_resource_user_aids_image_get_out import GetResourceUserAidsImageGetOut
    from ..models.get_resource_user_aids_pdf_get_out import GetResourceUserAidsPDFGetOut


T = TypeVar("T", bound="GetResourceUserAidsGetOut")


@_attrs_define
class GetResourceUserAidsGetOut:
    """
    Attributes:
        pdf_user_aids (GetResourceUserAidsPDFGetOut | None): User aids for PDF resources.
        image_user_aids (GetResourceUserAidsImageGetOut | None): User aids for Image resources.
    """

    pdf_user_aids: GetResourceUserAidsPDFGetOut | None
    image_user_aids: GetResourceUserAidsImageGetOut | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_resource_user_aids_image_get_out import GetResourceUserAidsImageGetOut
        from ..models.get_resource_user_aids_pdf_get_out import GetResourceUserAidsPDFGetOut

        pdf_user_aids: dict[str, Any] | None
        if isinstance(self.pdf_user_aids, GetResourceUserAidsPDFGetOut):
            pdf_user_aids = self.pdf_user_aids.to_dict()
        else:
            pdf_user_aids = self.pdf_user_aids

        image_user_aids: dict[str, Any] | None
        if isinstance(self.image_user_aids, GetResourceUserAidsImageGetOut):
            image_user_aids = self.image_user_aids.to_dict()
        else:
            image_user_aids = self.image_user_aids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pdf_user_aids": pdf_user_aids,
                "image_user_aids": image_user_aids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_resource_user_aids_image_get_out import GetResourceUserAidsImageGetOut
        from ..models.get_resource_user_aids_pdf_get_out import GetResourceUserAidsPDFGetOut

        d = dict(src_dict)

        def _parse_pdf_user_aids(data: object) -> GetResourceUserAidsPDFGetOut | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pdf_user_aids_type_0 = GetResourceUserAidsPDFGetOut.from_dict(data)

                return pdf_user_aids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetResourceUserAidsPDFGetOut | None, data)

        pdf_user_aids = _parse_pdf_user_aids(d.pop("pdf_user_aids"))

        def _parse_image_user_aids(data: object) -> GetResourceUserAidsImageGetOut | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_user_aids_type_0 = GetResourceUserAidsImageGetOut.from_dict(data)

                return image_user_aids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetResourceUserAidsImageGetOut | None, data)

        image_user_aids = _parse_image_user_aids(d.pop("image_user_aids"))

        get_resource_user_aids_get_out = cls(
            pdf_user_aids=pdf_user_aids,
            image_user_aids=image_user_aids,
        )

        get_resource_user_aids_get_out.additional_properties = d
        return get_resource_user_aids_get_out

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
