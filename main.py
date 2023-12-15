# (c) Tiago Tamagusko 2023

import streamlit as st
from streamlit_folium import st_folium
from src.router import get_osm_data, shortest_route
from src.map_viewer import create_map
from src.coordinates import get_coordinates
from src.add_point_to_map import add_point_to_map

# Streamlit UI
st.title("Route Planner")

# Default map centered on Amsterdam
default_center = [52.3676, 4.9041]
folium_map = create_map(default_center)

origin_address = st.text_input("Enter origin address", "Stationsplein, 1012 AB Amsterdam, Netherlands")
destination_address = st.text_input("Enter destination address", "Kalverstraat 92, 1012 PH Amsterdam, Netherlands")
avoid_lez = st.checkbox("Avoid Low Emission Zones (LEZ)")

# Add markers for origin and destination if addresses are provided
if origin_address:
    origin_coords = get_coordinates(origin_address)
    if origin_coords:
        add_point_to_map(folium_map, origin_coords, 'O')

if destination_address:
    destination_coords = get_coordinates(destination_address)
    if destination_coords:
        add_point_to_map(folium_map, destination_coords, 'D')

# Calculate and display the route when the button is clicked
if st.button("Calculate Route"):
    st.info("Not implemented yet")
    # The following code is commented out as the functionality is not implemented yet
    # if origin_coords and destination_coords:
    #     G = get_osm_data()
    #     if G:
    #         route = shortest_route(G, *origin_coords, *destination_coords, avoid_lez)
    #         if route:
    #             route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]
    #             folium.PolyLine(route_coords, color="blue" if avoid_lez else "green", weight=2.5, opacity=1).add_to(folium_map)

# Render the map in Streamlit using st_folium
st_folium(folium_map, width=700, height=510)

