import folium
import json
from streamlit_folium import st_folium

def create_map(center_point: list, lez_geojson_path='data/20231214_LEZ_NL.geojson'):
    """Create a folium map based on a center point and add LEZ layer.

    Args:
        center_point (list): Center of the map in format [latitude, longitude].
        lez_geojson_path (str): Path to the LEZ GeoJSON file.

    Returns:
        folium.Map: A folium map object.
    """
    map = folium.Map(
        location=center_point,
        tiles='OpenStreetMap',
        zoom_start=12,
        zoom_control=True,
        dragging=True,
        width=700,
        height=510,
        scrollWheelZoom=True,
    )

    # Load and add LEZ GeoJSON layer
    try:
        with open(lez_geojson_path) as f:
            lez_geojson = json.load(f)
        folium.GeoJson(lez_geojson, name="LEZ").add_to(map)
    except FileNotFoundError:
        print(f"File not found: {lez_geojson_path}")

    folium.LayerControl().add_to(map)
    return map

