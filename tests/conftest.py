"""Shared fixtures for tests."""
import uuid
from datetime import date, datetime
import pytest


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
