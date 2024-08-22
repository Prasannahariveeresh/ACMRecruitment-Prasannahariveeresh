import os
import json
import requests

from datetime import datetime

config_fp = open('config.json', 'r')
config = json.load(config_fp)

def get_weather_data(mode):
    if mode == '1':
        city = input("Enter the name of the city: ")
        url = config["rapid_api_urls"]["city"].format(c=city.lower())

    elif mode == '2':
        latitude = input("Enter the latitude: ")
        longitude = input("Enter the longitude: ")
        url = config["rapid_api_urls"]["latlon"].format(lat=latitude, lon=longitude)

    elif mode == '3':
        latitude = input("Enter the latitude: ")
        longitude = input("Enter the longitude: ")
        url = config["rapid_api_urls"]["5dayForecast"].format(lat=latitude, lon=longitude)

    else:
        return None

    resp = requests.get(url, headers=config["rapid_api_headers"])
    weather = resp.json()

    return weather

def display_weather_data(weather):
    os.system('clear' if os.name == 'posix' else 'cls')

    msg = "\n"
    msg += f"Timezone: UTC {weather['timezone']/3600}\n" if 'timezone' in weather else ""
    msg += f"Name: {weather['name']}\n" if 'name' in weather else ""
    msg += f"Date: {datetime.fromtimestamp(weather['dt'])}\n\n" if 'dt' in weather else ""

    msg += f"Weather: {config['icon_mapping'][weather['weather'][0]['icon']]}\n\n" if 'icon' in weather['weather'][0] else ""

    msg += f"Sunrise: {datetime.fromtimestamp(weather['sys']['sunrise'])}\n" if 'sunrise' in weather['sys'] else ""
    msg += f"Sunset: {datetime.fromtimestamp(weather['sys']['sunset'])}\n\n" if 'sunset' in weather['sys'] else ""

    msg += f"Wind Speed: {weather['wind']['speed']}\n" if 'speed' in weather['wind'] else ""
    msg += f"Wind Degree: {weather['wind']['deg']}\n" if 'deg' in weather['wind'] else ""
    msg += f"Wind Gust: {weather['wind']['gust']}\n\n" if 'gust' in weather['wind'] else ""

    msg += f"Temperature: {weather['main']['temp']}\n" if 'temp' in weather['main'] else ""
    msg += f"Feels like: {weather['main']['feels_like']}\n" if 'feels_like' in weather['main'] else ""
    msg += f"Min. Temperature: {weather['main']['temp_min']}\n" if 'temp_min' in weather['main'] else ""
    msg += f"Max. Temperature: {weather['main']['temp_max']}\n" if 'temp_max' in weather['main'] else ""
    msg += f"Pressure: {weather['main']['pressure']}\n" if 'pressure' in weather['main'] else ""
    msg += f"Humidity: {weather['main']['humidity']}\n" if 'humidity' in weather['main'] else ""

    print(msg)

if __name__ == '__main__':
    while True:
        print("WELCOME TO WEATHER APP\n")
        print("Press 1,2,3,4 for following actions")
        print("1. To see weather based on city")
        print("2. To see weather based on latitude/longitude")
        print("3. To see weather based on latitude/longitude for 5 days")
        print("4. Exit\n")

        ip = input("Enter the number: ")
        weather = get_weather_data(ip)

        if weather['cod'] != 200:
            print(f"ERROR !!! Reason: {weather['message']}")
            continue

        if ip == '3':
            for i in weather['list']:
                display_weather_data(i)
                print("="*30)

        elif ip == '4':
            break

        elif ip == '1' or ip == '2':
            display_weather_data(weather)
            print("="*30)

        else:
            print(f"Unknown input: {ip}")
            continue