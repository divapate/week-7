'''
Script to load geographical data into a pandas DataFrame, and save it as a CSV file.
'''


import pandas as pd


def get_geolocator(agent='h501-student'):
    """
    Initiate a Nominatim geolocator instance given an `agent`.

    Parameters
    ----------
    agent : str, optional
        Agent name for Nominatim, by default 'h501-student'
    """
    from geopy.geocoders import Nominatim
    return Nominatim(user_agent=agent)

def fetch_location_data(geolocator,loc):
    location = geolocator.geocode(loc)

    if location is None:
        return None
    
    return {"location": loc, "latitude": location.latitude, "longitude": location.longitude, "type": location.raw.get('type', 'unknown')}

def build_geo_dataframe(geolocator, locations):
    geo_data = [fetch_location_data(geolocator, loc) for loc in locations]
    geo_data = [g for g in geo_data if g is not None]
 
    return pd.DataFrame(geo_data)


if __name__ == "__main__":
    geo = get_geolocator()

    locations = ["Museum of Modern Art", "iuyt8765(*&)", "Alaska", "Franklin's Barbecue", "Burj Khalifa"]

    df = build_geo_dataframe(geo, locations)

    df.to_csv("./geo_data.csv")
