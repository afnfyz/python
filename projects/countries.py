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
    continent = data[0]['continents']
    landlocked = data[0]['landlocked']
    flag = data[0]['flag']
    flag_des = data[0]['flags']['alt']
    population = data[0]['population']
    formatted_population = '{:.2f}M'.format(population/1000000)

    currencies = data[0]['currencies']
    currency_code = list(currencies.keys())[0] 
    currency_name = currencies[currency_code]['name']
    currency_symbol = currencies[currency_code]['symbol']
    
    