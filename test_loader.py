import unittest
import pandas as pd
from loader import get_geolocator, fetch_location_data, build_geo_dataframe

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        locations = ["Museum of Modern Art", "USS Alabama Battleship Memorial Park"]
        geolocator = get_geolocator()
        df = build_geo_dataframe(geolocator, locations)

        self.assertEqual(len(df), 2)

        moma = df[df["location"] == "Museum of Modern Art"].iloc[0]
        self.assertAlmostEqual(moma["latitude"], 40.7615, places=2) 
        self.assertAlmostEqual(moma["longitude"], -73.9775, places=2)
        self.assertEqual(moma["type"], "museum")

        uss = df[df["location"] == "USS Alabama Battleship Memorial Park"].iloc[0]
        self.assertAlmostEqual(uss["latitude"], 30.6843, places=2)
        self.assertAlmostEqual(uss["longitude"], -88.0153, places=2)
        self.assertEqual(uss["type"], "park")

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

    
        self.assertIsNone(result, "A nonexistent location should return None.")

if __name__ == "__main__":
    unittest.main()
