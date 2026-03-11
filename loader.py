"""
loader.py

Module for retrieving geographical location data using OpenStreetMap's
Nominatim service via geopy and converting the results into a pandas DataFrame.

The module provides helper functions to:
- Initialize a geolocator
- Fetch latitude, longitude, and location type
- Build a DataFrame from a list of location names
"""

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd


def get_geolocator(agent: str = "h501-student") -> Nominatim:
    """
    Create and return a Nominatim geolocator instance.

    Args:
        agent (str): User agent name required by Nominatim.

    Returns:
        Nominatim: Configured geolocator instance.
    """
    return Nominatim(user_agent=agent)


def fetch_location_data(geocode, location_name: str) -> dict | None:
    """
    Retrieve geographic data for a given location name.

    Args:
        geocode: A geocoding function (e.g., RateLimiter-wrapped geocode).
        location_name (str): Name of the location to search.

    Returns:
        dict | None:
            Dictionary containing:
                - location (str)
                - latitude (float)
                - longitude (float)
                - type (str)
            Returns None if the location is not found.
    """
    location = geocode(location_name)

    if location is None:
        return None

    return {
        "location": location_name,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "type": location.raw.get("type"),
    }


def build_geo_dataframe(geolocator: Nominatim, locations: list[str]) -> pd.DataFrame:
    """
    Build a pandas DataFrame containing geographic data for multiple locations.

    Args:
        geolocator (Nominatim): Geolocator instance.
        locations (list[str]): List of location names.

    Returns:
        pd.DataFrame:
            DataFrame with columns:
                - location
                - latitude
                - longitude
                - type
    """
    # Add rate limiting to respect Nominatim usage policy
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    geo_data = [
        fetch_location_data(geocode, loc)
        for loc in locations
    ]

    # Remove None values (invalid locations)
    geo_data = [entry for entry in geo_data if entry is not None]

    return pd.DataFrame(geo_data)


if __name__ == "__main__":
    """
    Example usage:
    Fetch geographic data for sample locations and save to CSV.
    """
    geolocator = get_geolocator()

    sample_locations = [
        "Museum of Modern Art",
        "iuyt8765(*&)",
        "Alaska",
        "Franklin's Barbecue",
        "Burj Khalifa",
    ]

    df = build_geo_dataframe(geolocator, sample_locations)
    df.to_csv("geo_data.csv", index=False)