# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Tektome Python SDK - Utilities and API client for handling Tektome Resources. The package provides:
- Pydantic schema classes for validating Tektome data structures
- HTTP client (sync/async) for authenticated API requests
- Auto-generated endpoint functions for Tektome API operations

## Commands

```bash
# Install dependencies
uv sync

# Run all tests
uv run pytest

# Run single test file
uv run pytest tests/test_resource.py

# Run tests with coverage
uv run pytest --cov=tektome --cov-report=term-missing
```

## Architecture

### Package Structure

```
tektome/
├── __init__.py       # Main exports: BaseSchema, Resource, Resources, Project,
│                     #   Projects, AttributeDefinitions, Context, Date, DateTime
├── schema.py         # Core Pydantic schema classes with validation
└── endpoints/        # AUTO-GENERATED - Do not edit directly
    ├── client.py     # Client and AuthenticatedClient (httpx-based)
    ├── api/          # 40 API endpoint modules organized by domain
    └── models/       # 700+ Pydantic models for request/response types
```

### Key Design Patterns

**Schema Classes** (`tektome/schema.py`):
- All inherit from `BaseSchema` which uses `ConfigDict(extra="forbid")` to reject unexpected fields
- Each schema has a `kind` field with a field_validator enforcing exact string values
- Resources use `id: UUID` (single) or `ids: list[UUID]` (collection) patterns

**API Client** (`tektome/endpoints/client.py`):
- Built with `attrs` and `httpx`
- `Client` for unauthenticated requests, `AuthenticatedClient` adds Bearer token handling
- Both support sync (`with` context manager) and async (`async with`) usage

**Endpoints** (`tektome/endpoints/api/`):
- Auto-generated from OpenAPI spec via `tektome/gateway` - do not edit manually
- Organized by domain (account, resource, project, dataspace, etc.)
- Each module contains functions for specific API operations

## Important Notes

- The `tektome/endpoints/` directory is auto-generated and excluded from test coverage
- Python 3.13+ required
- Schema validation uses Pydantic v2
- Kind field values must match exactly: "resource", "resource[]", "project", "project[]", "attribute_definition[]", "date", "datetime"
