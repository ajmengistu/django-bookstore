from django.test import TestCase

class HomeTestCase(TestCase):
    def test_home(self):
        """Testing Home page"""
        self.assertEqual('hello', 'hello')
        self.assertNotEqual('hello', 'bye')