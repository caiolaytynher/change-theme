import unittest

from update_files import update_str


class TestFileHandling(unittest.TestCase):
    def setUp(self):
        self.text = "something in the ()\nsomething in the way, []"

    def test_update_str(self):
        modified_text: str = update_str(
            self.text,
            [
                (r"\(\)", "way"),
                (r"\[\]", "yeah"),
            ],
        )

        self.assertEqual(
            modified_text,
            "something in the way\nsomething in the way, yeah",
        )


if __name__ == "__main__":
    unittest.main()
