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
    print("Country found!")
    data = response.json()
    name = data[0]['name']['official']
    landlocked = data[0]['landlocked']
    flag = data[0]['flag']
    population = data[0]['population']
    formatted_population = '{:.2f}M'.format(population/1000000)
    print(formatted_population)
    