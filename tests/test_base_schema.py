"""Test suite for BaseSchema class."""
import pytest
from pydantic import ValidationError, Field
from tektome import BaseSchema


class TestBaseSchemaConfiguration:
    """Test BaseSchema configuration."""

    def test_base_schema_forbids_extra_fields(self):
        """Test that BaseSchema forbids extra fields."""

        class TestModel(BaseSchema):
            name: str
            value: int

        # Extra fields should raise ValidationError
        with pytest.raises(ValidationError) as exc_info:
            TestModel(name="test", value=42, extra_field="not allowed")

        assert "extra_field" in str(exc_info.value)
        assert "Extra inputs are not permitted" in str(exc_info.value)

    def test_base_schema_allows_defined_fields(self):
        """Test that BaseSchema allows all defined fields."""

        class TestModel(BaseSchema):
            name: str
            value: int
            optional: str | None = None

        # All defined fields should work
        model = TestModel(name="test", value=42, optional="optional")
        assert model.name == "test"
        assert model.value == 42
        assert model.optional == "optional"

    def test_base_schema_with_field_descriptions(self):
        """Test that BaseSchema works with Field descriptions."""

        class TestModel(BaseSchema):
            name: str = Field(..., description="The name field")
            value: int = Field(..., description="The value field")

        model = TestModel(name="test", value=42)
        assert model.name == "test"
        assert model.value == 42

        schema = model.model_json_schema()
        assert "name" in schema["properties"]
        assert "value" in schema["properties"]


class TestBaseSchemaInheritance:
    """Test BaseSchema inheritance."""

    def test_subclass_inherits_forbid_extra(self):
        """Test that subclasses inherit the forbid extra configuration."""

        class ParentModel(BaseSchema):
            parent_field: str

        class ChildModel(ParentModel):
            child_field: int

        # Child should also forbid extra fields
        with pytest.raises(ValidationError) as exc_info:
            ChildModel(parent_field="test", child_field=42, extra="not allowed")

        assert "extra" in str(exc_info.value)

    def test_subclass_can_add_fields(self):
        """Test that subclasses can add their own fields."""

        class ParentModel(BaseSchema):
            parent_field: str

        class ChildModel(ParentModel):
            child_field: int

        model = ChildModel(parent_field="test", child_field=42)
        assert model.parent_field == "test"
        assert model.child_field == 42


class TestBaseSchemaValidation:
    """Test BaseSchema validation behavior."""

    def test_required_fields_are_enforced(self):
        """Test that required fields are enforced."""

        class TestModel(BaseSchema):
            required_field: str
            optional_field: str | None = None

        with pytest.raises(ValidationError) as exc_info:
            TestModel(optional_field="test")

        assert "required_field" in str(exc_info.value)

    def test_type_validation_is_enforced(self):
        """Test that type validation is enforced."""

        class TestModel(BaseSchema):
            int_field: int
            str_field: str

        with pytest.raises(ValidationError):
            TestModel(int_field="not an int", str_field="valid string")

    def test_none_not_allowed_for_required_fields(self):
        """Test that None is not allowed for required fields."""

        class TestModel(BaseSchema):
            required_field: str

        with pytest.raises(ValidationError):
            TestModel(required_field=None)


class TestBaseSchemaFromDict:
    """Test creating BaseSchema instances from dictionaries."""

    def test_create_from_dict_with_valid_data(self):
        """Test creating a BaseSchema instance from a valid dictionary."""

        class TestModel(BaseSchema):
            name: str
            value: int

        data = {"name": "test", "value": 42}
        model = TestModel(**data)
        assert model.name == "test"
        assert model.value == 42

    def test_create_from_dict_with_extra_fields_raises_error(self):
        """Test that extra fields in dict raise ValidationError."""

        class TestModel(BaseSchema):
            name: str
            value: int

        data = {"name": "test", "value": 42, "extra": "not allowed"}
        with pytest.raises(ValidationError) as exc_info:
            TestModel(**data)

        assert "extra" in str(exc_info.value)


class TestBaseSchemaDocumentation:
    """Test BaseSchema documentation."""

    def test_base_schema_has_docstring(self):
        """Test that BaseSchema has a docstring."""
        assert BaseSchema.__doc__ is not None
        assert "base" in BaseSchema.__doc__.lower()
        assert "forbid" in BaseSchema.__doc__.lower()

    def test_subclass_can_have_docstring(self):
        """Test that subclasses can have their own docstrings."""

        class TestModel(BaseSchema):
            """Test model docstring."""
            name: str

        assert TestModel.__doc__ == "Test model docstring."


class TestBaseSchemaModelDump:
    """Test BaseSchema model_dump functionality."""

    def test_model_dump_returns_dict(self):
        """Test that model_dump returns a dictionary."""

        class TestModel(BaseSchema):
            name: str
            value: int

        model = TestModel(name="test", value=42)
        data = model.model_dump()
        assert isinstance(data, dict)
        assert data == {"name": "test", "value": 42}

    def test_model_dump_json_returns_string(self):
        """Test that model_dump_json returns a JSON string."""

        class TestModel(BaseSchema):
            name: str
            value: int

        model = TestModel(name="test", value=42)
        json_str = model.model_dump_json()
        assert isinstance(json_str, str)
        assert "test" in json_str
        assert "42" in json_str


class TestBaseSchemaEquality:
    """Test BaseSchema equality."""

    def test_models_with_same_values_are_equal(self):
        """Test that models with same values are equal."""

        class TestModel(BaseSchema):
            name: str
            value: int

        model1 = TestModel(name="test", value=42)
        model2 = TestModel(name="test", value=42)
        assert model1 == model2

    def test_models_with_different_values_are_not_equal(self):
        """Test that models with different values are not equal."""

        class TestModel(BaseSchema):
            name: str
            value: int

        model1 = TestModel(name="test", value=42)
        model2 = TestModel(name="test", value=43)
        assert model1 != model2
