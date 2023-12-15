# (c) Tiago Tamagusko 2022

import networkx as nx
import osmnx as ox
from osmnx.distance import nearest_nodes

ox.config(use_cache=True, log_console=True)

def get_osm_data():
    """Fetches OSM data for routing. This can be optimized based on specific area or requirements."""
    try:
        G = ox.graph_from_place('Amsterdam, Netherlands', network_type='drive')
        return G
    except Exception as e:
        print(f"Error fetching OSM data: {e}")
        return None

def shortest_route(G, start_lat, start_long, end_lat, end_long, avoid_lez=False):
    """Find the shortest route considering LEZ avoidance if required.
    Args:
        G: Graph (networkx)
        start_lat: latitude of origin node
        start_long: longitude of origin node
        end_lat: latitude of destination node
        end_long: longitude of destination node
        avoid_lez (bool): Whether to avoid LEZ areas.
    """
    if G is None:
        return None

    start_node = nearest_nodes(G, start_long, start_lat)
    end_node = nearest_nodes(G, end_long, end_lat)

    if avoid_lez:
        G_modified = modify_graph_for_lez(G)
        route = nx.shortest_path(G_modified, start_node, end_node, weight='length')
    else:
        route = nx.shortest_path(G, start_node, end_node, weight='length')

    return route

def shortest_route_length(G, start_lat, start_long, end_lat, end_long):
    """Find the length of the shortest route based on two nodes (start and end).
    Args:
        G: Graph (networkx)
        start_lat: latitude of origin node
        start_long: longitude of origin node
        end_lat: latitude of destination node
        end_long: longitude of destination node
    """
    if G is None:
        return None

    start_node = nearest_nodes(G, start_long, start_lat)
    end_node = nearest_nodes(G, end_long, end_lat)
    weight = 'travel_time'
    try:
        length = nx.shortest_path_length(G, start_node, end_node, weight)
        return length
    except nx.NetworkXNoPath:
        print("No path found between the given nodes.")
        return None

def modify_graph_for_lez(G):
    """Modify the graph to account for LEZ areas.
    Args:
        G: Graph (networkx)
    Returns:
        Modified graph with LEZ areas considered.
    """
    G_modified = G.copy()
    for u, v, d in G_modified.edges(data=True):
        if is_in_lez(u, v, G_modified):
            d['length'] *= 10
    return G_modified

def is_in_lez(u, v, G):
    """Check if an edge is in an LEZ area.
    Args:
        u, v: Node identifiers
        G: Graph (networkx)
    Returns:
        bool: True if the edge is in an LEZ area, False otherwise.
    """
    # Implement logic to determine if an edge is in an LEZ area
    return False  # Placeholder implementation

if __name__ == '__main__':
    # Example usage
    G = get_osm_data()
    if G:
        start_lat, start_long = 52.3676, 4.9041  # Amsterdam coordinates
        end_lat, end_long = 52.3702, 4.8952  # Another point in Amsterdam
        route = shortest_route(G, start_lat, start_long, end_lat, end_long, avoid_lez=True)
        length = shortest_route_length(G, start_lat, start_long, end_lat, end_long)
        if route:
            print("Route:", route)
            print("Length:", length)
        else:
            print("No route found.")
    else:
        print("Failed to load OSM data.")

