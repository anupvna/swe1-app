from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """A simple test to ensure the CI pipeline tracks coverage."""
        self.assertEqual(1 + 1, 2)
