"""Unit tests for the parseio decorator."""

import pytest
from pydantic import BaseModel, ValidationError

from tektome.decorators import parseio


class InputModel(BaseModel):
    """Test input model."""

    name: str
    value: int


class OutputModel(BaseModel):
    """Test output model."""

    result: str
    computed: int


class TestParseioInputValidation:
    """Tests for input validation/coercion."""

    def test_accepts_pydantic_model_input(self):
        """parseio accepts Pydantic model instances as input."""

        @parseio
        def func(data: InputModel) -> dict:
            return {"name": data.name}

        result = func(InputModel(name="test", value=42))
        assert result == {"name": "test"}

    def test_coerces_dict_to_pydantic_model(self):
        """parseio coerces dict input to Pydantic model via validate_call."""

        @parseio
        def func(data: InputModel) -> dict:
            return {"name": data.name, "value": data.value}

        result = func({"name": "test", "value": 42})
        assert result == {"name": "test", "value": 42}

    def test_validates_dict_input_fields(self):
        """parseio raises ValidationError for invalid dict input."""

        @parseio
        def func(data: InputModel) -> dict:
            return {"name": data.name}

        with pytest.raises(ValidationError):
            func({"name": "test", "value": "not_an_int"})

    def test_validates_missing_required_fields(self):
        """parseio raises ValidationError for missing required fields."""

        @parseio
        def func(data: InputModel) -> dict:
            return {"name": data.name}

        with pytest.raises(ValidationError):
            func({"name": "test"})  # missing 'value'

    def test_accepts_primitive_inputs(self):
        """parseio accepts primitive type inputs."""

        @parseio
        def func(x: int, y: str) -> dict:
            return {"x": x, "y": y}

        result = func(42, "hello")
        assert result == {"x": 42, "y": "hello"}

    def test_validates_primitive_input_types(self):
        """parseio validates primitive input types."""

        @parseio
        def func(x: int) -> dict:
            return {"x": x}

        # pydantic will coerce string "42" to int 42
        result = func("42")
        assert result == {"x": 42}

    def test_multiple_model_inputs(self):
        """parseio handles multiple Pydantic model inputs."""

        class OtherModel(BaseModel):
            flag: bool

        @parseio
        def func(a: InputModel, b: OtherModel) -> dict:
            return {"name": a.name, "flag": b.flag}

        result = func({"name": "test", "value": 1}, {"flag": True})
        assert result == {"name": "test", "flag": True}


class TestParseioOutputConversion:
    """Tests for output conversion."""

    def test_converts_pydantic_model_to_dict(self):
        """parseio converts Pydantic model output to dict via model_dump()."""

        @parseio
        def func(x: int) -> OutputModel:
            return OutputModel(result="hello", computed=x * 2)

        result = func(21)
        assert isinstance(result, dict)
        assert result == {"result": "hello", "computed": 42}

    def test_passes_dict_output_unchanged(self):
        """parseio passes dict output through unchanged."""

        @parseio
        def func(x: int) -> dict:
            return {"value": x}

        result = func(42)
        assert result == {"value": 42}

    def test_validates_dict_when_model_annotated(self):
        """parseio validates dict against annotated Pydantic model and returns dict."""

        @parseio
        def func(x: int) -> OutputModel:
            return {"result": "hello", "computed": x * 2}  # type: ignore # Returns dict, validated against OutputModel

        result = func(21)
        assert isinstance(result, dict)
        assert result == {"result": "hello", "computed": 42}

    def test_rejects_non_dict_non_model_output(self):
        """parseio raises TypeError for non-dict, non-model output."""

        @parseio
        def func(x: int) -> int:
            return x * 2

        with pytest.raises(
            TypeError, match="Expected return type to be dict or Pydantic model"
        ):
            func(21)

    def test_rejects_string_output(self):
        """parseio raises TypeError for string output."""

        @parseio
        def func() -> str:
            return "hello"

        with pytest.raises(
            TypeError, match="Expected return type to be dict or Pydantic model"
        ):
            func()

    def test_rejects_list_output(self):
        """parseio raises TypeError for list output."""

        @parseio
        def func() -> list:
            return [1, 2, 3]

        with pytest.raises(
            TypeError, match="Expected return type to be dict or Pydantic model"
        ):
            func()

    def test_rejects_none_output(self):
        """parseio raises TypeError for None output."""

        @parseio
        def func() -> None:
            return None

        with pytest.raises(
            TypeError, match="Expected return type to be dict or Pydantic model"
        ):
            func()


class TestParseioNestedModels:
    """Tests for nested Pydantic models."""

    def test_nested_model_output(self):
        """parseio handles nested Pydantic models in output."""

        class Inner(BaseModel):
            value: int

        class Outer(BaseModel):
            inner: Inner
            name: str

        @parseio
        def func() -> Outer:
            return Outer(inner=Inner(value=42), name="test")

        result = func()
        assert isinstance(result, dict)
        assert result == {"inner": {"value": 42}, "name": "test"}

    def test_list_of_models_in_output(self):
        """parseio handles list of Pydantic models in output."""

        class Item(BaseModel):
            id: int

        class Container(BaseModel):
            items: list[Item]

        @parseio
        def func() -> Container:
            return Container(items=[Item(id=1), Item(id=2)])

        result = func()
        assert result == {"items": [{"id": 1}, {"id": 2}]}


class TestParseioEdgeCases:
    """Edge case tests."""

    def test_empty_dict_output(self):
        """parseio handles empty dict output."""

        @parseio
        def func() -> dict:
            return {}

        result = func()
        assert result == {}

    def test_preserves_function_metadata(self):
        """parseio preserves function name and docstring."""

        @parseio
        def my_function(x: int) -> dict:
            """My docstring."""
            return {"x": x}

        assert my_function.__name__ == "my_function"
        assert my_function.__doc__ == """My docstring."""

    def test_keyword_arguments(self):
        """parseio works with keyword arguments."""

        @parseio
        def func(data: InputModel) -> dict:
            return {"name": data.name}

        result = func(data={"name": "test", "value": 42})  # type: ignore
        assert result == {"name": "test"}

    def test_mixed_positional_and_keyword(self):
        """parseio works with mixed positional and keyword arguments."""

        @parseio
        def func(a: InputModel, b: int) -> dict:
            return {"name": a.name, "b": b}

        result = func({"name": "test", "value": 1}, b=42)  # type: ignore
        assert result == {"name": "test", "b": 42}

    def test_optional_fields_in_model(self):
        """parseio handles optional fields in models."""

        class ModelWithOptional(BaseModel):
            required: str
            optional: int | None = None

        @parseio
        def func(data: ModelWithOptional) -> dict:
            return {"required": data.required, "optional": data.optional}

        result = func({"required": "test"})  # type: ignore
        assert result == {"required": "test", "optional": None}

    def test_default_values_in_model(self):
        """parseio handles default values in models."""

        class ModelWithDefault(BaseModel):
            name: str
            count: int = 0

        @parseio
        def func(data: ModelWithDefault) -> dict:
            return {"name": data.name, "count": data.count}

        result = func({"name": "test"})  # type: ignore
        assert result == {"name": "test", "count": 0}


class TestParseioParameters:
    """Tests for parseio decorator parameters."""

    def test_decorator_with_empty_parentheses(self):
        """parseio() with empty parentheses works like @parseio."""

        @parseio()
        def func(x: int) -> dict:
            return {"x": x}

        result = func(42)
        assert result == {"x": 42}

    def test_return_dict_true_converts_model_to_dict(self):
        """parseio(return_dict=True) converts Pydantic model to dict."""

        @parseio(return_dict=True)
        def func(x: int) -> OutputModel:
            return OutputModel(result="hello", computed=x * 2)

        result = func(21)
        assert isinstance(result, dict)
        assert result == {"result": "hello", "computed": 42}

    def test_return_dict_false_keeps_model(self):
        """parseio(return_dict=False) returns Pydantic model instance."""

        @parseio(return_dict=False)
        def func(x: int) -> OutputModel:
            return OutputModel(result="hello", computed=x * 2)

        result = func(21)
        assert isinstance(result, OutputModel)
        assert result.result == "hello"
        assert result.computed == 42

    def test_return_dict_false_with_dict_input_validates_and_returns_model(self):
        """parseio(return_dict=False) validates dict and returns model when annotated."""

        @parseio(return_dict=False)
        def func(x: int) -> OutputModel:
            return {"result": "hello", "computed": x * 2}  # type: ignore

        result = func(21)
        assert isinstance(result, OutputModel)
        assert result.result == "hello"
        assert result.computed == 42

    def test_validate_json_serializable_true_rejects_non_serializable(self):
        """parseio(validate_json_serializable=True) rejects non-JSON-serializable values."""

        @parseio(validate_json_serializable=True)
        def func() -> dict:
            return {"func": lambda x: x}  # functions are not JSON serializable

        with pytest.raises(TypeError, match="not JSON serializable"):
            func()

    def test_validate_json_serializable_false_allows_non_serializable(self):
        """parseio(validate_json_serializable=False) allows non-JSON-serializable values."""

        @parseio(validate_json_serializable=False)
        def func() -> dict:
            return {"func": lambda x: x}

        result = func()
        assert "func" in result
        assert callable(result["func"])

    def test_validate_json_serializable_default_rejects_non_serializable(self):
        """parseio by default rejects non-JSON-serializable values."""

        @parseio
        def func() -> dict:
            return {"data": {1, 2, 3}}  # sets are not JSON serializable

        with pytest.raises(TypeError, match="not JSON serializable"):
            func()

    def test_both_parameters_false(self):
        """parseio(return_dict=False, validate_json_serializable=False) works."""

        @parseio(return_dict=False, validate_json_serializable=False)
        def func() -> OutputModel:
            return OutputModel(result="test", computed=100)

        result = func()
        assert isinstance(result, OutputModel)
        assert result.result == "test"

    def test_return_dict_false_with_plain_dict_return(self):
        """parseio(return_dict=False) with dict return type returns dict."""

        @parseio(return_dict=False)
        def func() -> dict:
            return {"key": "value"}

        result = func()
        assert isinstance(result, dict)
        assert result == {"key": "value"}
