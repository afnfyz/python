import csv
import json
import urllib
import requests

where = urllib.parse.quote_plus("""
{
    "Year": {
        "$gt": 1999
    }
}
""")
url = 'https://parseapi.back4app.com/classes/Car_Model_List?limit=999999999999999999999999&where=%s' % where
headers = {
    'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z',
    'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW'
}
response = requests.get(url, headers=headers)
data = json.loads(response.content.decode('utf-8'))

# Check if the request was successful
if response.status_code == 200:
    # Specify the CSV file name
    csv_filename = 'cars.csv'

    # Extract data from the 'results' key in the JSON response
    car_data = data.get('results', [])

    # Write data to CSV file
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write header row
        if car_data:
            header_row = car_data[0].keys()
            csv_writer.writerow(header_row)

            # Write data rows
            for row in car_data:
                csv_writer.writerow(row.values())

    print(f'Data has been written to {csv_filename}')
else:
    print(f'Request failed with status code: {response.status_code}')
    print(json.dumps(data, indent=2))
