import unittest
from pathlib import Path

from handlers.files import get_file_content, update_file, apply_changes


class TestFileHandling(unittest.TestCase):
    def setUp(self):
        self.mock_file: Path = Path.cwd() / "tests/mock/sample_text.txt"

    def test_get_file_content(self):
        content: str = get_file_content(self.mock_file)

        self.assertIsInstance(content, str)
        self.assertEqual(content, "content\n")

    def test_update_file(self):
        update_file(self.mock_file, "more content\n")

        content: str = get_file_content(self.mock_file)
        self.assertEqual(content, "more content\n")

        update_file(self.mock_file, "content\n")

    def test_apply_changes(self):
        content = "something in the ()\nsomething in the way, []"
        modified_content: str = apply_changes(
            content,
            [
                (r"\(\)", "way"),
                (r"\[\]", "yeah"),
            ],
        )

        self.assertEqual(
            modified_content,
            "something in the way\nsomething in the way, yeah",
        )


if __name__ == "__main__":
    unittest.main()
