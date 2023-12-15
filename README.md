# Route Planner Application

This application is a MVP designed to provide routing solutions in the Netherlands, with a specific focus on avoiding Low Emission Zones (LEZ) when required.

## Getting Started

To get started with this project, clone the repository and install the required dependencies listed in `requirements.txt`.

### Prerequisites

- Python 3.9+
- Streamlit
- Se more on: `requirements.txt`

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/tamagusko/ADJUSTWITHREPO
   ```
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the application, navigate to the project directory and execute:
```
streamlit run main.py
```

## Features

- Input origin and destination postal codes in the Netherlands.
- Option to avoid Low Emission Zones (LEZ) in routing.
- Visualization of routes.

## Notes

### LEZ by Plate

For information on Low Emission Zones based on vehicle plates, visit:
[https://www.milieuzones.nl/check](https://www.milieuzones.nl/check)

### OSM LEZ Information

Learn more about Low Emission Zones in OpenStreetMap:
[http://wiki.openstreetmap.org/wiki/Low_emission_zone](http://wiki.openstreetmap.org/wiki/Low_emission_zone)

### Overpass LEZ Query

Explore LEZ data using Overpass Turbo:
[https://overpass-turbo.eu/s/1etD](https://overpass-turbo.eu/s/1etD)

