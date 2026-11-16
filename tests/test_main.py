import unittest
from main import diagnose


class VenvDoctorTests(unittest.TestCase):
    def test_detects_virtual_environment(self):
        active, issues = diagnose("/project/.venv", "/usr", "/project/.venv")
        self.assertTrue(active)
        self.assertEqual(issues, [])

    def test_detects_activation_mismatch(self):
        active, issues = diagnose("/project/.venv", "/usr", "/other/env")
        self.assertTrue(active)
        self.assertTrue(any("does not match" in item for item in issues))

    def test_reports_global_interpreter(self):
        active, issues = diagnose("/usr", "/usr", None)
        self.assertFalse(active)
        self.assertTrue(any("not running inside" in item for item in issues))


if __name__ == "__main__":
    unittest.main()
