# pyright: reportCallIssue=false
"""Test suite for Context class."""
import uuid
import pytest
from pydantic import ValidationError
from tektome import Context


class TestContextCreation:
    """Test Context creation."""

    def test_create_context_with_valid_data(self, sample_uuid):
        """Test creating a Context with valid data."""
        context = Context(
            system_user_api_key="test_api_key_12345",
            system_base_url="https://example.tektome.com",
            system_execution_id=sample_uuid,

        )
        assert context.system_user_api_key == "test_api_key_12345"
        assert str(context.system_base_url) == "https://example.tektome.com/"
        assert context.system_execution_id == sample_uuid

    def test_create_context_from_dict(self, sample_uuid_str):
        """Test creating a Context from a dictionary."""
        data = {
            "system_user_api_key": "test_api_key_12345",
            "system_base_url": "https://example.tektome.com",
            "system_execution_id": sample_uuid_str,
        }
        context = Context(**data)
        assert context.system_user_api_key == "test_api_key_12345"
        assert str(context.system_base_url) == "https://example.tektome.com/"
        assert str(context.system_execution_id) == sample_uuid_str

    def test_create_context_with_different_system_base_urls(self, sample_uuid):
        """Test creating Context with different base URL formats."""
        urls = [
            ("https://domain.tld", "https://domain.tld/"),
            ("https://api.example.com", "https://api.example.com/"),
            ("http://localhost:8000", "http://localhost:8000/"),
        ]
        for url_input, url_expected in urls:
            context = Context(
                system_user_api_key="key",
                system_base_url=url_input,
                system_execution_id=sample_uuid,

            )
            assert str(context.system_base_url) == url_expected


class TestContextValidation:
    """Test Context validation."""

    def test_system_user_api_key_is_required(self, sample_uuid):
        """Test that system_user_api_key field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Context(
                system_base_url="https://example.com",
                system_execution_id=sample_uuid,
                
            )
        assert "system_user_api_key" in str(exc_info.value)

    def test_system_base_url_is_required(self, sample_uuid):
        """Test that system_base_url field is required."""
        with pytest.raises(ValidationError) as exc_info:
            Context(
                system_user_api_key="key",
                system_execution_id=sample_uuid,
                
            )
        assert "system_base_url" in str(exc_info.value)

    def test_guarded_fields_are_optional_at_construction(self):
        """Test that guarded fields can be omitted at construction."""
        context = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
        )
        # Construction succeeds without guarded fields
        assert context.system_user_api_key == "key"

    def test_invalid_system_execution_id_format(self):
        """Test that invalid UUID format for system_execution_id raises error."""
        with pytest.raises(ValidationError):
            Context(
                system_user_api_key="key",
                system_base_url="https://example.com",
                system_execution_id="not-a-uuid",
                
            )

    def test_invalid_system_base_url_format(self, sample_uuid):
        """Test that invalid URL format raises error."""
        invalid_urls = [
            "not-a-url",
            "ftp://example.com",  # Invalid scheme
            "example.com",  # Missing scheme
        ]
        for invalid_url in invalid_urls:
            with pytest.raises(ValidationError):
                Context(
                    system_user_api_key="key",
                    system_base_url=invalid_url,
                    system_execution_id=sample_uuid,
                    
                )

    def test_none_values_not_allowed_for_required_fields(self, sample_uuid):
        """Test that None values are not allowed for required fields."""
        with pytest.raises(ValidationError):
            Context(
                system_user_api_key=None,
                system_base_url="https://example.com",
            )

        with pytest.raises(ValidationError):
            Context(
                system_user_api_key="key",
                system_base_url=None,
            )


class TestContextSerialization:
    """Test Context serialization."""

    def test_model_dump(self, sample_uuid):
        """Test converting Context to dictionary."""
        context = Context(
            system_user_api_key="test_api_key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,

        )
        data = context.model_dump()
        assert data["system_user_api_key"] == "test_api_key"
        assert str(data["system_base_url"]) == "https://example.com/"
        assert data["system_execution_id"] == sample_uuid

    def test_model_dump_json(self, sample_uuid):
        """Test converting Context to JSON string."""
        context = Context(
            system_user_api_key="test_api_key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,
            
        )
        json_str = context.model_dump_json()
        assert "test_api_key" in json_str
        assert "https://example.com" in json_str
        assert str(sample_uuid) in json_str

    def test_model_dump_with_mode_json(self, sample_uuid):
        """Test model_dump with mode='json'."""
        context = Context(
            system_user_api_key="test_api_key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,
            
        )
        data = context.model_dump(mode="json")
        assert isinstance(data["system_user_api_key"], str)
        assert isinstance(data["system_base_url"], str)
        assert isinstance(data["system_execution_id"], str)
        assert data["system_execution_id"] == str(sample_uuid)


class TestContextEquality:
    """Test Context equality."""

    def test_contexts_with_same_values_are_equal(self, sample_uuid):
        """Test that Contexts with same values are equal."""
        context1 = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,
            
        )
        context2 = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,
            
        )
        assert context1 == context2

    def test_contexts_with_different_api_keys_are_not_equal(self, sample_uuid):
        """Test that Contexts with different API keys are not equal."""
        context1 = Context(
            system_user_api_key="key1",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,
            
        )
        context2 = Context(
            system_user_api_key="key2",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,
            
        )
        assert context1 != context2

    def test_contexts_with_different_system_execution_ids_are_not_equal(self):
        """Test that Contexts with different execution IDs are not equal."""
        context1 = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_execution_id=uuid.uuid4(),
            
        )
        context2 = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_execution_id=uuid.uuid4(),
            
        )
        assert context1 != context2


class TestContextEdgeCases:
    """Test Context edge cases."""

    def test_context_is_mutable_by_default(self, sample_uuid):
        """Test that Context fields can be modified (Pydantic v2 default)."""
        context = Context(
            system_user_api_key="old_key",
            system_base_url="https://old.com",
            system_execution_id=sample_uuid,
            
        )
        # In Pydantic v2, models are mutable by default unless configured otherwise
        context.system_user_api_key = "new_key"
        assert context.system_user_api_key == "new_key"

    def test_extra_fields_not_allowed_by_default(self, sample_uuid):
        """Test that extra fields are not allowed by default."""
        # BaseSchema forbids extra fields
        with pytest.raises(ValidationError) as exc_info:
            Context(
                system_user_api_key="key",
                system_base_url="https://example.com",
                system_execution_id=sample_uuid,
                extra_field="value",
            )
        assert "extra_field" in str(exc_info.value)

    def test_uuid_type_preservation(self, sample_uuid):
        """Test that UUID type is preserved."""
        context = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,
            
        )
        assert isinstance(context.system_execution_id, uuid.UUID)
        assert context.system_execution_id == sample_uuid


class TestContextValidateCall:
    """Test Context with validate_call decorator."""

    def test_validate_call_with_dict(self, sample_uuid_str):
        """Test that validate_call converts dict to Context."""
        from pydantic import validate_call

        @validate_call
        def process_context(context: Context):
            return context

        result = process_context(
            context={
                "system_user_api_key": "key",
                "system_base_url": "https://example.com",
                "system_execution_id": sample_uuid_str,
            }
        )
        assert isinstance(result, Context)
        assert result.system_user_api_key == "key"
        assert str(result.system_base_url) == "https://example.com/"
        assert str(result.system_execution_id) == sample_uuid_str

    def test_validate_call_with_context_instance(self, sample_uuid):
        """Test that validate_call accepts Context directly."""
        from pydantic import validate_call

        @validate_call
        def process_context(context: Context):
            return context

        ctx = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,

        )
        result = process_context(context=ctx)
        assert isinstance(result, Context)
        assert result.system_user_api_key == "key"


class TestContextDocumentation:
    """Test Context documentation and usage."""

    def test_class_docstring_exists(self):
        """Test that class has proper documentation."""
        assert Context.__doc__ is not None
        assert "context" in Context.__doc__.lower()

    def test_field_descriptions(self, sample_uuid):
        """Test that fields have proper descriptions."""
        context = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,

        )
        schema = context.model_json_schema()
        assert "system_user_api_key" in schema["properties"]
        assert "system_base_url" in schema["properties"]
        assert "system_execution_id" in schema["properties"]

    def test_system_user_api_key_description(self):
        """Test that system_user_api_key has the correct description."""
        schema = Context.model_json_schema()
        assert "Authorization" in schema["properties"]["system_user_api_key"]["description"]
        assert "Bearer" in schema["properties"]["system_user_api_key"]["description"]

    def test_system_base_url_description(self):
        """Test that system_base_url has the correct description."""
        schema = Context.model_json_schema()
        assert "domain.tld" in schema["properties"]["system_base_url"]["description"]

    def test_system_execution_id_description(self):
        """Test that system_execution_id has the correct description."""
        schema = Context.model_json_schema()
        assert (
            "extraction context" in schema["properties"]["system_execution_id"]["description"]
        )


class TestContextGuardedFields:
    """Test Context guarded fields behavior."""

    @pytest.fixture
    def minimal_context(self):
        """Create a Context with only required fields."""
        return Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
        )

    @pytest.fixture
    def full_context(self, sample_uuid):
        """Create a Context with all fields set."""
        return Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_chatroom_id=sample_uuid,
            system_execution_id=sample_uuid,
            system_dataspace_id=sample_uuid,
            system_project_id=sample_uuid,
            system_resource_id=sample_uuid,
        )

    def test_guarded_fields_raise_when_none(self, minimal_context):
        """Test that accessing guarded fields raises AttributeError when None."""
        guarded_fields = ["system_chatroom_id", "system_execution_id", "system_dataspace_id", "system_project_id", "system_resource_id"]
        for field in guarded_fields:
            with pytest.raises(AttributeError) as exc_info:
                getattr(minimal_context, field)
            assert field in str(exc_info.value)

    def test_guarded_fields_return_value_when_set(self, full_context, sample_uuid):
        """Test that accessing guarded fields returns value when set."""
        assert full_context.system_chatroom_id == sample_uuid
        assert full_context.system_execution_id == sample_uuid
        assert full_context.system_dataspace_id == sample_uuid
        assert full_context.system_project_id == sample_uuid
        assert full_context.system_resource_id == sample_uuid

    def test_non_guarded_fields_work_normally(self, minimal_context):
        """Test that non-guarded fields are accessible without error."""
        assert minimal_context.system_user_api_key == "key"
        assert str(minimal_context.system_base_url) == "https://example.com/"

    def test_guarded_fields_can_be_set_individually(self, sample_uuid):
        """Test that guarded fields can be set individually."""
        context = Context(
            system_user_api_key="key",
            system_base_url="https://example.com",
            system_execution_id=sample_uuid,
        )
        # system_execution_id is set, should work
        assert context.system_execution_id == sample_uuid
        # system_chatroom_id is not set, should raise
        with pytest.raises(AttributeError):
            _ = context.system_chatroom_id

    def test_model_dump_includes_none_guarded_fields(self, minimal_context):
        """Test that model_dump includes guarded fields even when None."""
        data = minimal_context.model_dump()
        assert "system_chatroom_id" in data
        assert data["system_chatroom_id"] is None
        assert "system_execution_id" in data
        assert data["system_execution_id"] is None

    def test_model_dump_excludes_none_with_exclude_none(self, minimal_context):
        """Test that model_dump with exclude_none omits None guarded fields."""
        data = minimal_context.model_dump(exclude_none=True)
        assert "system_chatroom_id" not in data
        assert "system_execution_id" not in data
