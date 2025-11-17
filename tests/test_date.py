"""Test suite for Date class."""
from datetime import date
import pytest
from pydantic import ValidationError
from tektome import Date


class TestDateCreation:
    """Test Date creation."""

    def test_create_date_with_valid_data(self, sample_date):
        """Test creating a Date with valid data."""
        date_obj = Date(value=sample_date, kind="date")
        assert date_obj.value == sample_date
        assert date_obj.kind == "date"

    def test_create_date_from_dict(self, sample_date):
        """Test creating a Date from a dictionary."""
        data = {
            "value": sample_date,
            "kind": "date",
        }
        date_obj = Date(**data)
        assert date_obj.value == sample_date
        assert date_obj.kind == "date"

    def test_create_date_with_string_value(self):
        """Test creating a Date with string date value."""
        date_obj = Date(value="2025-11-17", kind="date")
        assert date_obj.value == date(2025, 11, 17)
        assert date_obj.kind == "date"

    def test_create_date_with_different_dates(self):
        """Test creating Date with different date values."""
        dates = [
            date(2025, 1, 1),
            date(2000, 12, 31),
            date(1970, 1, 1),
        ]
        for d in dates:
            date_obj = Date(value=d, kind="date")
            assert date_obj.value == d


class TestDateValidation:
    """Test Date validation."""

    def test_value_is_required(self):
        """Test that value field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Date(kind="date")
        assert "value" in str(exc_info.value)

    def test_kind_is_required(self, sample_date):
        """Test that kind field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Date(value=sample_date)
        assert "kind" in str(exc_info.value)

    def test_kind_must_be_date(self, sample_date):
        """Test that kind must be 'date'."""
        with pytest.raises(ValidationError) as exc_info:
            Date(value=sample_date, kind="datetime")
        assert "kind must be 'date'" in str(exc_info.value)

    def test_kind_cannot_be_empty(self, sample_date):
        """Test that kind cannot be empty string."""
        with pytest.raises(ValidationError) as exc_info:
            Date(value=sample_date, kind="")
        assert "kind must be 'date'" in str(exc_info.value)

    def test_invalid_date_format(self):
        """Test that invalid date format raises error."""
        with pytest.raises(ValidationError):
            Date(value="not-a-date", kind="date")

    def test_none_values_not_allowed(self, sample_date):
        """Test that None values are not allowed for required fields."""
        with pytest.raises(ValidationError):
            Date(value=None, kind="date")

        with pytest.raises(ValidationError):
            Date(value=sample_date, kind=None)


class TestDateSerialization:
    """Test Date serialization."""

    def test_model_dump(self, sample_date):
        """Test converting Date to dictionary."""
        date_obj = Date(value=sample_date, kind="date")
        data = date_obj.model_dump()
        assert data["value"] == sample_date
        assert data["kind"] == "date"

    def test_model_dump_json(self, sample_date):
        """Test converting Date to JSON string."""
        date_obj = Date(value=sample_date, kind="date")
        json_str = date_obj.model_dump_json()
        assert "2025-11-17" in json_str
        assert "date" in json_str

    def test_model_dump_with_mode_json(self, sample_date):
        """Test model_dump with mode='json'."""
        date_obj = Date(value=sample_date, kind="date")
        data = date_obj.model_dump(mode="json")
        assert isinstance(data["value"], str)
        assert data["value"] == "2025-11-17"
        assert isinstance(data["kind"], str)


class TestDateEquality:
    """Test Date equality."""

    def test_dates_with_same_values_are_equal(self, sample_date):
        """Test that Dates with same values are equal."""
        date1 = Date(value=sample_date, kind="date")
        date2 = Date(value=sample_date, kind="date")
        assert date1 == date2

    def test_dates_with_different_values_are_not_equal(self):
        """Test that Dates with different values are not equal."""
        date1 = Date(value=date(2025, 11, 17), kind="date")
        date2 = Date(value=date(2025, 11, 18), kind="date")
        assert date1 != date2


class TestDateEdgeCases:
    """Test Date edge cases."""

    def test_date_is_mutable_by_default(self, sample_date):
        """Test that Date fields can be modified (Pydantic v2 default)."""
        date_obj = Date(value=sample_date, kind="date")
        new_date = date(2026, 1, 1)
        date_obj.value = new_date
        assert date_obj.value == new_date

    def test_extra_fields_not_allowed_by_default(self, sample_date):
        """Test that extra fields are not allowed by default."""
        # BaseSchema forbids extra fields
        with pytest.raises(ValidationError) as exc_info:
            Date(
                value=sample_date,
                kind="date",
                extra_field="value",
            )
        assert "extra_field" in str(exc_info.value)

    def test_date_type_preservation(self, sample_date):
        """Test that date type is preserved."""
        date_obj = Date(value=sample_date, kind="date")
        assert isinstance(date_obj.value, date)
        assert date_obj.value == sample_date


class TestDateValidateCall:
    """Test Date with validate_call decorator."""

    def test_validate_call_with_dict(self, sample_date):
        """Test that validate_call converts dict to Date."""
        from pydantic import validate_call

        @validate_call
        def process_date(d: Date):
            return d

        result = process_date(
            d={
                "value": sample_date,
                "kind": "date",
            }
        )
        assert isinstance(result, Date)
        assert result.value == sample_date
        assert result.kind == "date"

    def test_validate_call_with_date_instance(self, sample_date):
        """Test that validate_call accepts Date directly."""
        from pydantic import validate_call

        @validate_call
        def process_date(d: Date):
            return d

        date_obj = Date(value=sample_date, kind="date")
        result = process_date(d=date_obj)
        assert isinstance(result, Date)
        assert result.value == sample_date


class TestDateDocumentation:
    """Test Date documentation and usage."""

    def test_class_docstring_exists(self):
        """Test that class has proper documentation."""
        assert Date.__doc__ is not None
        assert "date" in Date.__doc__.lower()

    def test_field_descriptions(self, sample_date):
        """Test that fields have proper descriptions."""
        date_obj = Date(value=sample_date, kind="date")
        schema = date_obj.model_json_schema()
        assert "value" in schema["properties"]
        assert "kind" in schema["properties"]

    def test_value_description(self):
        """Test that value has the correct description."""
        schema = Date.model_json_schema()
        assert "date value" in schema["properties"]["value"]["description"].lower()

    def test_kind_description(self):
        """Test that kind has the correct description."""
        schema = Date.model_json_schema()
        assert "date" in schema["properties"]["kind"]["description"].lower()
