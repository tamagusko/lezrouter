Example API Call and Functionality

# API Endpoint:

`POST /api/v1/calculate-route`

# Request Body:

The API would accept a JSON payload with the following structure:

```json
{
  "origin": "Stationsplein, 1012 AB Amsterdam, Netherlands",
  "destinations": [
    "Kalverstraat 92, 1012 PH Amsterdam, Netherlands",
    "Another Address, Amsterdam, Netherlands"
  ],
  "avoid_lez": true
}
```

- `origin`: The starting point of the route.
- `destinations`: A list of destination addresses. The API will calculate the best route through these points.
- `avoid_lez`: A boolean indicating whether to avoid Low Emission Zones.

# Response:

The API would return a JSON object containing the optimized route:

```json
{
  "status": "success",
  "route": [
    {
      "address": "Stationsplein, 1012 AB Amsterdam, Netherlands",
      "coordinates": [52.3786, 4.9009]
    },
    {
      "address": "Kalverstraat 92, 1012 PH Amsterdam, Netherlands",
      "coordinates": [52.3691, 4.8898]
    },
    {
      "address": "Another Address, Amsterdam, Netherlands",
      "coordinates": [52.3702, 4.8953]
    }
  ],
  "total_distance": "5.6 km",
  "estimated_time": "15 minutes"
}
```

- `status`: Indicates the success or failure of the request.
- `route`: An ordered list of waypoints, including addresses and their coordinates.
- `total_distance`: The total distance of the route.
- `estimated_time`: Estimated time to complete the route.

# Functionality:

- When a client sends a request to this endpoint with the required data, the API processes the origin, list of destinations, and LEZ avoidance preference.
- The API then responds with the optimized route, including each waypoint's address and coordinates, along with the total distance and estimated travel time.

