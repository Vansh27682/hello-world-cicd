
import unittest
from app import hello_devops


class TestHelloDevops(unittest.TestCase):
    def test_hello_devops_message(self):
        self.assertEqual(
            hello_devops(),
            "Hello, Git!"
        )

    def test_hello_devops_returns_string(self):
        self.assertIsInstance(hello_devops(), str)


if __name__ == "__main__":
    unittest.main()
