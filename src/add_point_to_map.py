import folium

def add_point_to_map(G, point, label):
    """Add a point to the folium map.

    Args:
        f_map (folium.Map): The folium map object.
        point (tuple): A tuple of (latitude, longitude).
        label (str): Label for the point ('O' for origin, 'D' for destination).
    """
    folium.Marker(
        location=point,
        popup=label,
        icon=folium.Icon(color="blue" if label == 'O' else "red", icon='info-sign')
    ).add_to(G)

