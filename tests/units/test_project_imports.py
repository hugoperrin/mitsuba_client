import unittest


class TestImports(unittest.TestCase):
    def test_module_imports(self):
        import mitsuba_client.cli as cli
        import mitsuba_client.client as client
        import mitsuba_client.utils as utils

        self.assertTrue(True)
