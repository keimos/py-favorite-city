import unittest
from io import StringIO
import sys

# This is a Python script for Favorite City

def favorite_city(name):
    if name == "Chicago":
        print("One of my favorite cities is The Windy City, " + name)
    elif name == "New York":
        print("One of my favorite cities is The Big Apple, " + name)
    elif name == "Boston":
        print("One of my favorite cities is Beantown,  " + name)

# Test cases
class TestFavoriteCity(unittest.TestCase):
    
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_chicago(self):
        favorite_city("Chicago")
        self.assertEqual(self.held_output.getvalue().strip(), "One of my favorite cities is The Windy City, Chicago")
        
    def test_new_york(self):
        favorite_city("New York")
        self.assertEqual(self.held_output.getvalue().strip(), "One of my favorite cities is The Big Apple, New York")
        
    def test_boston(self):
        favorite_city("Boston")
        self.assertEqual(self.held_output.getvalue().strip(), "One of my favorite cities is Beantown,  Boston")
        
    def test_invalid_city(self):
        favorite_city("Los Angeles")
        self.assertEqual(self.held_output.getvalue().strip(), "")

# Run the tests
if __name__ == "__main__":
    unittest.main()
