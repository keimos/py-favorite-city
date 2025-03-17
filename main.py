import unittest
from io import StringIO
import sys

# This is a Python script for Favorite City
def favorite_city(name):
    city_map = {
        "Chiacgo": "The Windy City",
        "New York": "The Big Apple",
        "Boston": "Beantown"
    }
    if name in city_map:
        print(f"One of my favorite cities is {city_map[name]}, {name}")
    else:
        print(f"Sorry, {name} is NOT on the favorite cities list") # Handles invalid city input

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
