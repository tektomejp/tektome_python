"""Decorators for input/output validation and transformation."""

import json
from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar, overload

from pydantic import BaseModel, validate_call

P = ParamSpec("P")
T = TypeVar("T")


def _validate_json_serializable(data: dict[str, Any]) -> dict[str, Any]:
    """Validate that data is JSON serializable."""
    try:
        json.dumps(data)
    except (TypeError, ValueError) as e:
        raise TypeError(f"Return value is not JSON serializable: {e}") from e
    return data


# Overload for @parseio (without parentheses)
@overload
def parseio(func: Callable[P, T]) -> Callable[P, dict[str, Any]]: ...


# Overload for @parseio() or @parseio(return_dict=..., ...)
@overload
def parseio(
    func: None = None,
    *,
    return_dict: bool = True,
    validate_json_serializable: bool = True,
) -> Callable[[Callable[P, T]], Callable[P, dict[str, Any] | T]]: ...


def parseio(
    func: Callable[P, T] | None = None,
    *,
    return_dict: bool = True,
    validate_json_serializable: bool = True,
) -> (
    Callable[P, dict[str, Any] | T]
    | Callable[[Callable[P, T]], Callable[P, dict[str, Any] | T]]
):
    """Decorator that validates inputs with pydantic and ensures JSON-serializable output.

    - Inputs: Validated/coerced using pydantic's @validate_call (dicts become models)
    - Outputs: If return type is a Pydantic model and result is a dict, validates against the model
    - Return value: Converted to dict via .model_dump() if it's a Pydantic model (when return_dict=True)

    Can be used as @parseio or @parseio() or @parseio(return_dict=False).

    Args:
        func: The function to decorate (when used without parentheses).
        return_dict: If True, convert Pydantic models to dict via model_dump(). Defaults to True.
        validate_json_serializable: If True, validate that return value is JSON serializable. Defaults to True.

    Returns:
        Decorated function with input validation and optional output conversion.
    """

    def decorator(fn: Callable[P, T]) -> Callable[P, dict[str, Any] | T]:
        validated_func = validate_call(fn)

        # Get the return type annotation
        return_type = fn.__annotations__.get("return")
        return_is_pydantic_model = isinstance(return_type, type) and issubclass(
            return_type, BaseModel
        )

        @wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> dict[str, Any] | T:
            result = validated_func(*args, **kwargs)
            if isinstance(result, BaseModel):
                if return_dict:
                    output = result.model_dump()
                    if validate_json_serializable:
                        return _validate_json_serializable(output)
                    return output
                return result  # type: ignore
            if isinstance(result, dict):
                # If return type is a Pydantic model, validate the dict against it
                if return_is_pydantic_model:
                    validated = return_type.model_validate(result)  # type: ignore
                    if return_dict:
                        output = validated.model_dump()
                        if validate_json_serializable:
                            return _validate_json_serializable(output)
                        return output
                    return validated  # type: ignore
                if validate_json_serializable:
                    return _validate_json_serializable(result)
                return result
            raise TypeError(
                f"Expected return type to be dict or Pydantic model, got {type(result)}"
            )

        return wrapper

    # Support both @parseio and @parseio() syntax
    if func is not None:
        return decorator(func)
    return decorator
