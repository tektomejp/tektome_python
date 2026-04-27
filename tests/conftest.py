"""Shared fixtures for tests."""
import uuid
from datetime import date, datetime
from unittest.mock import MagicMock

import pytest

from tektome import Context
from tektome.endpoints import AuthenticatedClient


@pytest.fixture
def sample_uuid():
    """Return a sample UUID for testing."""
    return uuid.uuid4()


@pytest.fixture
def sample_uuid_str():
    """Return a sample UUID string for testing."""
    return str(uuid.uuid4())


@pytest.fixture
def sample_uuid_list():
    """Return a list of sample UUIDs for testing."""
    return [uuid.uuid4() for _ in range(3)]


@pytest.fixture
def sample_date():
    """Return a sample date for testing."""
    return date(2025, 11, 17)


@pytest.fixture
def sample_datetime():
    """Return a sample datetime for testing."""
    return datetime(2025, 11, 17, 14, 30, 0)


@pytest.fixture
def dataspace_id():
    return uuid.uuid4()


@pytest.fixture
def resource_id():
    return uuid.uuid4()


@pytest.fixture
def execution_id():
    return uuid.uuid4()


@pytest.fixture
def context(dataspace_id, resource_id, execution_id):
    return Context(
        system_user_api_key="test_api_key",
        system_base_url="https://example.tektome.com",
        system_flow_type="general",
        system_dataspace_id=dataspace_id,
        system_resource_id=resource_id,
        system_execution_id=execution_id,
    )


@pytest.fixture
def client():
    return MagicMock(spec=AuthenticatedClient)
