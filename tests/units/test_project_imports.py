"""Tests for device classes."""
import unittest


class TestImports(unittest.TestCase):
    def test_module_imports(self):
        import mitsuba_client.cli as cli  # noqa: F401
        import mitsuba_client.client as client  # noqa: F401
        import mitsuba_client.utils as utils  # noqa: F401

        self.assertTrue(True)
