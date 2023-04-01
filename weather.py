import requests
import sys

api_key = "cb366054d7442875a35ee1da791b58a0"

user_input = input("Enter city or zip code: ")

data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=imperial"
)

while data.status_code != 200:
    print("No City Found Please Try Again.")
    print()
    user_input = input("Enter city or zip code: ")
    data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=imperial"
    )
else:
    weather = data.json()['weather'][0]['main']
    temp = round(data.json()['main']['temp'])
    temp_feels = round(data.json()['main']['feels_like'])
    temp_min = round(data.json()['main']['temp_min'])
    temp_max = round(data.json()['main']['temp_max'])



    print()
    print(f"The current weather in {user_input} is:")
    print(f"{weather}")
    print()
    print(f"Temperature: {temp} ºF")
    print(f"Feels like: {temp_feels} ºF")
    print()
    print(f"High: {temp_max} ºF\nLow: {temp_min} ºF")
    print()

    if 'speed' in data.json()['wind']:
        wind_speed = round(data.json()['wind']['speed'])
        print(f"Wind speed: {wind_speed} mph")
    if 'gust' in data.json()['wind']:
        wind_gust = round(data.json()['wind']['gust'])
        print(f"Wind gust: {wind_gust} mph")
