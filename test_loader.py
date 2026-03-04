import unittest
import pandas as pd
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
    geolocator = get_geolocator()

    known_locations = {
        "Museum of Modern Art": {
            "latitude": 40.7618552,
            "longitude": -73.9782438,
            "type": "museum",
        },
        "USS Alabama Battleship Memorial Park": {
            "latitude": 30.684373,
            "longitude": -88.015316,
            "type": "park",
        },
    }

    for place, expected in known_locations.items():
        result = fetch_location_data(geolocator, place)

        # Ensure result exists
        self.assertIsNotNone(result, f"{place} should return valid data.")

        # Check latitude & longitude (allow small variation)
        self.assertAlmostEqual(
            result["latitude"],
            expected["latitude"],
            places=2,
            msg=f"Latitude mismatch for {place}",
        )

        self.assertAlmostEqual(
            result["longitude"],
            expected["longitude"],
            places=2,
            msg=f"Longitude mismatch for {place}",
        )

        # Type comparison (case-insensitive safety)
        self.assertEqual(
            result["type"].lower(),
            expected["type"],
            f"Type mismatch for {place}",
        )

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertIsNone(result, 
                          "A nonexistent location should have an empty result.")

if __name__ == "__main__":
    unittest.main()
