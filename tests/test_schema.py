"""Test suite for openflow_schema schema classes."""
import unittest
from openflow_schema import Resource, Resources
from pydantic import validate_call


class TestResource(unittest.TestCase):
    """Test Resource class."""

    def test_resource_minimal(self):
        """Test creating a Resource with minimal required fields."""
        resource = Resource(name="test-resource")
        self.assertEqual(resource.name, "test-resource")
        self.assertIsNone(resource.id)
        self.assertIsNone(resource.type)
        self.assertIsNone(resource.description)
        self.assertEqual(resource.metadata, {})

    def test_resource_full(self):
        """Test creating a Resource with all fields."""
        resource = Resource(
            id="res-123",
            name="test-resource",
            type="compute",
            description="A test resource",
            metadata={"key": "value", "number": 42}
        )
        self.assertEqual(resource.id, "res-123")
        self.assertEqual(resource.name, "test-resource")
        self.assertEqual(resource.type, "compute")
        self.assertEqual(resource.description, "A test resource")
        self.assertEqual(resource.metadata, {"key": "value", "number": 42})

    def test_resource_from_dict(self):
        """Test creating a Resource from a dictionary."""
        data = {
            "id": "res-456",
            "name": "dict-resource",
            "type": "storage"
        }
        resource = Resource(**data)
        self.assertEqual(resource.id, "res-456")
        self.assertEqual(resource.name, "dict-resource")
        self.assertEqual(resource.type, "storage")

    def test_resource_extra_fields(self):
        """Test that Resource allows extra fields."""
        resource = Resource(
            name="test",
            custom_field="custom_value",
            another_field=123
        )
        self.assertEqual(resource.name, "test")
        # Extra fields are allowed by the config

    def test_resource_to_dict(self):
        """Test converting Resource to dictionary."""
        resource = Resource(
            id="res-789",
            name="test-resource",
            type="network"
        )
        data = resource.model_dump()
        self.assertEqual(data["id"], "res-789")
        self.assertEqual(data["name"], "test-resource")
        self.assertEqual(data["type"], "network")


class TestResources(unittest.TestCase):
    """Test Resources class."""

    def test_resources_empty(self):
        """Test creating an empty Resources collection."""
        resources = Resources()
        self.assertEqual(resources.resources, [])
        self.assertIsNone(resources.total)

    def test_resources_with_items(self):
        """Test creating Resources with multiple Resource items."""
        r1 = Resource(name="resource-1")
        r2 = Resource(name="resource-2")
        resources = Resources(
            resources=[r1, r2],
            total=2
        )
        self.assertEqual(len(resources.resources), 2)
        self.assertEqual(resources.total, 2)
        self.assertEqual(resources.resources[0].name, "resource-1")
        self.assertEqual(resources.resources[1].name, "resource-2")

    def test_resources_from_dict(self):
        """Test creating Resources from a dictionary."""
        data = {
            "resources": [
                {"name": "res-1", "type": "type1"},
                {"name": "res-2", "type": "type2"}
            ],
            "total": 2
        }
        resources = Resources(**data)
        self.assertEqual(len(resources.resources), 2)
        self.assertEqual(resources.total, 2)
        self.assertIsInstance(resources.resources[0], Resource)
        self.assertEqual(resources.resources[0].name, "res-1")


class TestValidateCall(unittest.TestCase):
    """Test validate_call decorator with Resource."""

    def test_validate_call_with_dict(self):
        """Test that validate_call converts dict to Resource."""
        @validate_call
        def process_resource(resource: Resource):
            return resource

        # Pass a dictionary, should be converted to Resource
        result = process_resource(resource={"name": "test-resource"})
        self.assertIsInstance(result, Resource)
        self.assertEqual(result.name, "test-resource")

    def test_validate_call_with_resource(self):
        """Test that validate_call accepts Resource directly."""
        @validate_call
        def process_resource(resource: Resource):
            return resource

        # Pass a Resource instance
        resource = Resource(name="test-resource")
        result = process_resource(resource=resource)
        self.assertIsInstance(result, Resource)
        self.assertEqual(result.name, "test-resource")


if __name__ == '__main__':
    unittest.main()
