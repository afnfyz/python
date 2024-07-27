import requests
import json

# Define the API URL
url = "https://turo.com/api/v2/search"

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Define the payload
payload = {
    "filters": {
        "dates": {
            "start": "2024-07-29T10:00",
            "end": "2024-08-01T10:00"
        },
        "location": {
            "country": "US",
            "type": "boundingbox",
            "bottomLeft": {
                "lat": 40.53092577235968,
                "lng": -74.06605855679089
            },
            "topRight": {
                "lat": 40.86742488727127,
                "lng": -73.37391988491589
            }
        },
        "makes": ["Ford"],
        "types": ["CAR", "SUV", "PASSENGER_MINIVAN", "MINIVAN"],
        "years": {
            "min": 2012,
            "max": 2025
        }
    },
    "sorts": {
        "direction": "ASC",
        "type": "RELEVANCE"
    }
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
