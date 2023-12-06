import requests


def get_weather(city_name):
    api_key = '280012c2e58b03240737597523d9b14d'

    response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric')

    if response.status_code == 200:
        data = response.json()
        weather = {
            'Main': {
                'Temperature': data['main']['temp'],
                'Humidity': data['main']['humidity'],
                'Pressure': data['main']['pressure'],
            'Visibility': data['visibility'],

            'Wind': {
                'Speed': data['wind']['speed'],
            'Clouds': {
                'All': data['clouds']['all'],
            }
            }
            }
        }

        return weather
    else:
        return None



city_name = str(input("The city:"))
weather_data = get_weather(city_name)

if weather_data:
    print(f"The weather for {city_name}:")
    print(f"Temperature: {weather_data['Main']['Temperature']}°C")
    print(f"Humidity: {weather_data['Main']['Humidity']}%")
    print(f"Pressure: {weather_data['Main']['Pressure']} hPa")
    print(f"Visibility: {weather_data['Main']['Visibility']} km")
    print(f"Wind Speed: {weather_data['Main']['Wind']['Speed']} m/s")
    print(f"Clouds All: {weather_data['Main']['Wind']['Clouds']['All']}%")

else:
    print("ERROR")


