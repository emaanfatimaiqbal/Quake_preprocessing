"""Task 1: fetch the USGS GeoJSON feed and turn it into a DataFrame."""
import pandas as pd

BASE = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary"


def fetch_feed(feed: str = "all_week") -> dict:
    """GET {BASE}/{feed}.geojson and return the parsed dict.

    Use a timeout and raise_for_status(). A misspelled feed name returns
    HTTP 200 with a plain-text body, so raise a clear error if the body
    is not valid JSON.
    """
    ...
    url = f"{BASE}/{feed}.geojson"

    response = requests.get(url, timeout=15)

    response.raise_for_status()

    try:
        return response.json()
    except ValueError:
        raise ValueError("The response is not valid JSON. Check the feed name.")


    


def geojson_to_df(payload: dict) -> pd.DataFrame:
    """One row per event.

    Columns: 'id' (top level of each feature), every key in 'properties',
    plus 'lon', 'lat', 'depth_km' from geometry.coordinates = [lon, lat, depth].
    """
    ...
    rows = []

    for feature in payload["features"]:

        row = {}

        # Get event ID
        row["id"] = feature["id"]

        # Get properties
        row.update(feature.get("properties", {}))

        # Get coordinates
        coordinates = feature.get("geometry", {}).get("coordinates", [None, None, None])

        row["lon"] = coordinates[0]
        row["lat"] = coordinates[1]
        row["depth_km"] = coordinates[2]

        rows.append(row)

    return pd.DataFrame(rows)
print("Fetch.py Run Completed")