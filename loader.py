"""
Script to load geographical data into a pandas DataFrame
and save it as a CSV file.
"""

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError
import pandas as pd


def get_geolocator(agent: str = "h501-student") -> Nominatim:
    """
    Create and return a Nominatim geolocator instance.
    """
    return Nominatim(user_agent=agent)


def fetch_location_data(geo, location_name: str):
    """
    Fetch latitude, longitude, and type for a given location.
    """
    try:
        location = geo.geocode(location_name)

        if location is None:
            return None

        return {
            "location": location_name,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "type": getattr(location, "geo_type", None),
        }

    except GeocoderServiceError:
        return None
    except Exception:
        return None


def build_geo_dataframe(geolocator, locations):
    """
    Build a pandas DataFrame from a list of location names.
    """
    geo_data = [fetch_location_data(geolocator, loc) for loc in locations]

    for loc in locations:
        data = fetch_location_data(geo, loc)
        if data is not None:
            geo_data.append(data)

    return pd.DataFrame(geo_data)


if __name__ == "__main__":
    geolocator_instance = get_geolocator()

    locations = [
        "Museum of Modern Art",
        "iuyt8765(*&)",
        "Alaska",
        "Franklin's Barbecue",
        "Burj Khalifa",
    ]

    df = build_geo_dataframe(geolocator_instance, locations)

    df.to_csv("./geo_data.csv", index=False)

    print("Geo data saved to geo_data.csv")
