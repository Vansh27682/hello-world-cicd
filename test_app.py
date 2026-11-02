
import unittest
from app import hello_devops, welcome_message


class TestHelloDevops(unittest.TestCase):
    def test_hello_devops_message(self):
        self.assertEqual(
            hello_devops(),
            "Hello, Git!"
        )

    def test_hello_devops_returns_string(self):
        self.assertIsInstance(hello_devops(), str)

    def test_welcome_message_vansh(self):
        self.assertEqual(welcome_message("Vansh"), "Welcome to DevOps, Vansh!")

    def test_welcome_message_jatin(self):
        self.assertEqual(welcome_message("Jatin"), "Welcome to DevOps, Jatin!")


if __name__ == "__main__":
    unittest.main()
