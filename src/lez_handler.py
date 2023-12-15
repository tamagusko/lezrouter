# (c) Tiago Tamagusko 2023

import json
import os
from shapely.geometry import shape, LineString

def load_lez_data(file_path='data/20231214_LEZ_NL.geojson'):
    """Load LEZ data from a GeoJSON file.

    Args:
        file_path (str): Path to the GeoJSON file.

    Returns:
        list: A list of LEZ area polygons.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    lez_areas = [shape(feature['geometry']) for feature in data['features']]
    return lez_areas

def check_lez_intersection(route, lez_areas):
    """Check if the given route intersects with any LEZ area.

    Args:
        route (list): A list of [latitude, longitude] points representing the route.
        lez_areas (list): A list of LEZ area polygons.

    Returns:
        bool: True if the route intersects any LEZ area, False otherwise.
    """
    route_line = LineString(route)
    for area in lez_areas:
        if route_line.intersects(area):
            return True
    return False

if __name__ == '__main__':
    # Example usage
    lez_areas = load_lez_data()
    test_route = [[52.3702, 4.8952], [52.3676, 4.9041]]  # Example route points in Amsterdam
    intersects = check_lez_intersection(test_route, lez_areas)
    print(f"Route intersects with LEZ: {intersects}")

