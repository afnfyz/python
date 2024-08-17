import pandas as pd
import json
import os

# Path to your JSON file
json_file_path = "/Users/afnanfoyez/Documents/Data/turo_car_listings.json"

# Read the JSON data from the file
with open(json_file_path, 'r') as file:
    response = json.load(file)

# Parse the JSON response
vehicles = response.get("vehicles", [])

# Create a list of dictionaries with the relevant data
data = []
for vehicle in vehicles:
    data.append({
        "ID": vehicle.get("id"),
        "Make": vehicle.get("make"),
        "Model": vehicle.get("model"),
        "Year": vehicle.get("year"),
        "Type": vehicle.get("type"),
        "Avg Daily Price (USD)": vehicle.get("avgDailyPrice", {}).get("amount"),
        "Rating": vehicle.get("rating"),
        "Completed Trips": vehicle.get("completedTrips"),
        "Host ID": vehicle.get("hostId"),
        "Image URL": vehicle.get("images", [{}])[0].get("originalImageUrl"),
        "Location City": vehicle.get("location", {}).get("city"),
        "Location State": vehicle.get("location", {}).get("state"),
        "Location Country": vehicle.get("location", {}).get("country"),
        "Distance (miles)": vehicle.get("location", {}).get("distance", {}).get("value"),
        "Is All Star Host": vehicle.get("isAllStarHost"),
        "Tags": ", ".join(tag.get("label") for tag in vehicle.get("tags", []))
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV with a custom path, appending if the file exists
csv_file_path = "/Users/afnanfoyez/Documents/Data/vehicles_data.csv"

# Check if file exists to decide the header parameter
if not os.path.isfile(csv_file_path):
    df.to_csv(csv_file_path, index=False, mode='w', header=True)
else:
    df.to_csv(csv_file_path, index=False, mode='a', header=False)

print(f"CSV file created successfully at {csv_file_path}.")
