from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bim_key_value_stats_out_bool_bucket_stats import BimKeyValueStatsOutBoolBucketStats
    from ..models.bim_key_value_stats_out_num_bucket_stats import BimKeyValueStatsOutNumBucketStats
    from ..models.bim_key_value_stats_out_text_bucket_stats import BimKeyValueStatsOutTextBucketStats


T = TypeVar("T", bound="BimKeyValueStatsOut")


@_attrs_define
class BimKeyValueStatsOut:
    """
    Attributes:
        text_bucket_stats (BimKeyValueStatsOutTextBucketStats): Statistics for text_buckets: {key: {values: [{value,
            count}], doc_count}}
        num_bucket_stats (BimKeyValueStatsOutNumBucketStats): Statistics for num_buckets: {key: {values: [{value,
            count}], doc_count}}
        bool_bucket_stats (BimKeyValueStatsOutBoolBucketStats): Statistics for bool_buckets: {key: {values: [{value,
            count}], doc_count}}
        total_documents (int): Total number of parent documents indexed
        total_unique_keys (int): Total number of unique keys across all bucket types
        element_type (str): Type of BIM element these stats represent
        bim_project_id (str): ID of the BIM project these stats belong to
        cached (bool): Whether the stats were retrieved from cache
    """

    text_bucket_stats: BimKeyValueStatsOutTextBucketStats
    num_bucket_stats: BimKeyValueStatsOutNumBucketStats
    bool_bucket_stats: BimKeyValueStatsOutBoolBucketStats
    total_documents: int
    total_unique_keys: int
    element_type: str
    bim_project_id: str
    cached: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_bucket_stats = self.text_bucket_stats.to_dict()

        num_bucket_stats = self.num_bucket_stats.to_dict()

        bool_bucket_stats = self.bool_bucket_stats.to_dict()

        total_documents = self.total_documents

        total_unique_keys = self.total_unique_keys

        element_type = self.element_type

        bim_project_id = self.bim_project_id

        cached = self.cached

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_bucket_stats": text_bucket_stats,
                "num_bucket_stats": num_bucket_stats,
                "bool_bucket_stats": bool_bucket_stats,
                "total_documents": total_documents,
                "total_unique_keys": total_unique_keys,
                "element_type": element_type,
                "bim_project_id": bim_project_id,
                "cached": cached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bim_key_value_stats_out_bool_bucket_stats import BimKeyValueStatsOutBoolBucketStats
        from ..models.bim_key_value_stats_out_num_bucket_stats import BimKeyValueStatsOutNumBucketStats
        from ..models.bim_key_value_stats_out_text_bucket_stats import BimKeyValueStatsOutTextBucketStats

        d = dict(src_dict)
        text_bucket_stats = BimKeyValueStatsOutTextBucketStats.from_dict(d.pop("text_bucket_stats"))

        num_bucket_stats = BimKeyValueStatsOutNumBucketStats.from_dict(d.pop("num_bucket_stats"))

        bool_bucket_stats = BimKeyValueStatsOutBoolBucketStats.from_dict(d.pop("bool_bucket_stats"))

        total_documents = d.pop("total_documents")

        total_unique_keys = d.pop("total_unique_keys")

        element_type = d.pop("element_type")

        bim_project_id = d.pop("bim_project_id")

        cached = d.pop("cached")

        bim_key_value_stats_out = cls(
            text_bucket_stats=text_bucket_stats,
            num_bucket_stats=num_bucket_stats,
            bool_bucket_stats=bool_bucket_stats,
            total_documents=total_documents,
            total_unique_keys=total_unique_keys,
            element_type=element_type,
            bim_project_id=bim_project_id,
            cached=cached,
        )

        bim_key_value_stats_out.additional_properties = d
        return bim_key_value_stats_out

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
