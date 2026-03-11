"""
test_loader.py

Unit tests for the loader module.

Tests include:
- Validation of known real-world locations
- Handling of invalid location input
"""

import unittest
from loader import get_geolocator, fetch_location_data, build_geo_dataframe


class TestLoader(unittest.TestCase):
    """Test cases for geographic data loading functions."""

    def test_valid_locations(self):
        """
        Ensure valid locations return expected coordinates and types.
        """
        locations = [
            "Museum of Modern Art",
            "USS Alabama Battleship Memorial Park"
        ]

        geolocator = get_geolocator()
        df = build_geo_dataframe(geolocator, locations)

        # Ensure both valid locations were returned
        self.assertEqual(len(df), 2)

        # Test Museum of Modern Art
        moma = df[df["location"] == "Museum of Modern Art"].iloc[0]
        self.assertAlmostEqual(moma["latitude"], 40.7615, places=2)
        self.assertAlmostEqual(moma["longitude"], -73.9775, places=2)
        self.assertEqual(moma["type"], "museum")

        # Test USS Alabama
        uss = df[df["location"] == "USS Alabama Battleship Memorial Park"].iloc[0]
        self.assertAlmostEqual(uss["latitude"], 30.6843, places=2)
        self.assertAlmostEqual(uss["longitude"], -88.0153, places=2)
        self.assertEqual(uss["type"], "park")

    def test_invalid_location(self):
        """
        Ensure invalid locations return None.
        """
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator.geocode, "asdfqwer1234")

        self.assertIsNone(
            result,
            "A nonexistent location should return None."
        )


if __name__ == "__main__":
    unittest.main()