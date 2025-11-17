"""Test suite for DateTime class."""
from datetime import datetime
import pytest
from pydantic import ValidationError
from tektome import DateTime


class TestDateTimeCreation:
    """Test DateTime creation."""

    def test_create_datetime_with_valid_data(self, sample_datetime):
        """Test creating a DateTime with valid data."""
        datetime_obj = DateTime(value=sample_datetime, kind="datetime")
        assert datetime_obj.value == sample_datetime
        assert datetime_obj.kind == "datetime"

    def test_create_datetime_from_dict(self, sample_datetime):
        """Test creating a DateTime from a dictionary."""
        data = {
            "value": sample_datetime,
            "kind": "datetime",
        }
        datetime_obj = DateTime(**data)
        assert datetime_obj.value == sample_datetime
        assert datetime_obj.kind == "datetime"

    def test_create_datetime_with_string_value(self):
        """Test creating a DateTime with string datetime value."""
        datetime_obj = DateTime(value="2025-11-17T14:30:00", kind="datetime")
        assert datetime_obj.value == datetime(2025, 11, 17, 14, 30, 0)
        assert datetime_obj.kind == "datetime"

    def test_create_datetime_with_different_datetimes(self):
        """Test creating DateTime with different datetime values."""
        datetimes = [
            datetime(2025, 1, 1, 0, 0, 0),
            datetime(2000, 12, 31, 23, 59, 59),
            datetime(1970, 1, 1, 12, 0, 0),
        ]
        for dt in datetimes:
            datetime_obj = DateTime(value=dt, kind="datetime")
            assert datetime_obj.value == dt


class TestDateTimeValidation:
    """Test DateTime validation."""

    def test_value_is_required(self):
        """Test that value field is required."""
        with pytest.raises(ValidationError) as exc_info:
            DateTime(kind="datetime")
        assert "value" in str(exc_info.value)

    def test_kind_is_required(self, sample_datetime):
        """Test that kind field is required."""
        with pytest.raises(ValidationError) as exc_info:
            DateTime(value=sample_datetime)
        assert "kind" in str(exc_info.value)

    def test_kind_must_be_datetime(self, sample_datetime):
        """Test that kind must be 'datetime'."""
        with pytest.raises(ValidationError) as exc_info:
            DateTime(value=sample_datetime, kind="date")
        assert "kind must be 'datetime'" in str(exc_info.value)

    def test_kind_cannot_be_empty(self, sample_datetime):
        """Test that kind cannot be empty string."""
        with pytest.raises(ValidationError) as exc_info:
            DateTime(value=sample_datetime, kind="")
        assert "kind must be 'datetime'" in str(exc_info.value)

    def test_invalid_datetime_format(self):
        """Test that invalid datetime format raises error."""
        with pytest.raises(ValidationError):
            DateTime(value="not-a-datetime", kind="datetime")

    def test_none_values_not_allowed(self, sample_datetime):
        """Test that None values are not allowed for required fields."""
        with pytest.raises(ValidationError):
            DateTime(value=None, kind="datetime")

        with pytest.raises(ValidationError):
            DateTime(value=sample_datetime, kind=None)


class TestDateTimeSerialization:
    """Test DateTime serialization."""

    def test_model_dump(self, sample_datetime):
        """Test converting DateTime to dictionary."""
        datetime_obj = DateTime(value=sample_datetime, kind="datetime")
        data = datetime_obj.model_dump()
        assert data["value"] == sample_datetime
        assert data["kind"] == "datetime"

    def test_model_dump_json(self, sample_datetime):
        """Test converting DateTime to JSON string."""
        datetime_obj = DateTime(value=sample_datetime, kind="datetime")
        json_str = datetime_obj.model_dump_json()
        assert "2025-11-17" in json_str
        assert "datetime" in json_str

    def test_model_dump_with_mode_json(self, sample_datetime):
        """Test model_dump with mode='json'."""
        datetime_obj = DateTime(value=sample_datetime, kind="datetime")
        data = datetime_obj.model_dump(mode="json")
        assert isinstance(data["value"], str)
        assert "2025-11-17T14:30:00" in data["value"]
        assert isinstance(data["kind"], str)


class TestDateTimeEquality:
    """Test DateTime equality."""

    def test_datetimes_with_same_values_are_equal(self, sample_datetime):
        """Test that DateTimes with same values are equal."""
        datetime1 = DateTime(value=sample_datetime, kind="datetime")
        datetime2 = DateTime(value=sample_datetime, kind="datetime")
        assert datetime1 == datetime2

    def test_datetimes_with_different_values_are_not_equal(self):
        """Test that DateTimes with different values are not equal."""
        datetime1 = DateTime(value=datetime(2025, 11, 17, 14, 30, 0), kind="datetime")
        datetime2 = DateTime(value=datetime(2025, 11, 17, 14, 30, 1), kind="datetime")
        assert datetime1 != datetime2


class TestDateTimeEdgeCases:
    """Test DateTime edge cases."""

    def test_datetime_is_mutable_by_default(self, sample_datetime):
        """Test that DateTime fields can be modified (Pydantic v2 default)."""
        datetime_obj = DateTime(value=sample_datetime, kind="datetime")
        new_datetime = datetime(2026, 1, 1, 0, 0, 0)
        datetime_obj.value = new_datetime
        assert datetime_obj.value == new_datetime

    def test_extra_fields_not_allowed_by_default(self, sample_datetime):
        """Test that extra fields are not allowed by default."""
        # BaseSchema forbids extra fields
        with pytest.raises(ValidationError) as exc_info:
            DateTime(
                value=sample_datetime,
                kind="datetime",
                extra_field="value",
            )
        assert "extra_field" in str(exc_info.value)

    def test_datetime_type_preservation(self, sample_datetime):
        """Test that datetime type is preserved."""
        datetime_obj = DateTime(value=sample_datetime, kind="datetime")
        assert isinstance(datetime_obj.value, datetime)
        assert datetime_obj.value == sample_datetime

    def test_datetime_with_microseconds(self):
        """Test datetime with microseconds."""
        dt = datetime(2025, 11, 17, 14, 30, 0, 123456)
        datetime_obj = DateTime(value=dt, kind="datetime")
        assert datetime_obj.value.microsecond == 123456


class TestDateTimeValidateCall:
    """Test DateTime with validate_call decorator."""

    def test_validate_call_with_dict(self, sample_datetime):
        """Test that validate_call converts dict to DateTime."""
        from pydantic import validate_call

        @validate_call
        def process_datetime(dt: DateTime):
            return dt

        result = process_datetime(
            dt={
                "value": sample_datetime,
                "kind": "datetime",
            }
        )
        assert isinstance(result, DateTime)
        assert result.value == sample_datetime
        assert result.kind == "datetime"

    def test_validate_call_with_datetime_instance(self, sample_datetime):
        """Test that validate_call accepts DateTime directly."""
        from pydantic import validate_call

        @validate_call
        def process_datetime(dt: DateTime):
            return dt

        datetime_obj = DateTime(value=sample_datetime, kind="datetime")
        result = process_datetime(dt=datetime_obj)
        assert isinstance(result, DateTime)
        assert result.value == sample_datetime


class TestDateTimeDocumentation:
    """Test DateTime documentation and usage."""

    def test_class_docstring_exists(self):
        """Test that class has proper documentation."""
        assert DateTime.__doc__ is not None
        assert "datetime" in DateTime.__doc__.lower()

    def test_field_descriptions(self, sample_datetime):
        """Test that fields have proper descriptions."""
        datetime_obj = DateTime(value=sample_datetime, kind="datetime")
        schema = datetime_obj.model_json_schema()
        assert "value" in schema["properties"]
        assert "kind" in schema["properties"]

    def test_value_description(self):
        """Test that value has the correct description."""
        schema = DateTime.model_json_schema()
        assert "datetime value" in schema["properties"]["value"]["description"].lower()

    def test_kind_description(self):
        """Test that kind has the correct description."""
        schema = DateTime.model_json_schema()
        assert "datetime" in schema["properties"]["kind"]["description"].lower()
