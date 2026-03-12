
from utils import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    """Checks if 0C is really 32F -> conversion rate"""
    assert celsius_to_fahrenheit(0) == 32