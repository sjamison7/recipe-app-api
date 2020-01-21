# use the following terminal command for running this test
# docker-compose run app sh -c "python manage.py test && flake8"
from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted together"""
        self.assertEqual(subtract(11, 8), 3)
