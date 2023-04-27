import requests

country = input("Input country name: ")
base_url= "https://restcountries.com/v3.1/name/"

url = base_url + str(country)

response = requests.get(url)

while response.status_code != 200 :
    print("No country found, please try again.")
    country = input("Input country name: ")
    url = base_url + str(country)
    response = requests.get(url)
else:
    print("country found")
