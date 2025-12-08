import requests
import json

def get_weather_without_error_handling(city):
    api_key = "e09cd24b12714af0f1d8e297e8973824"  # replace this with your real API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    # Print pretty formatted JSON response
    print(json.dumps(data, indent=4))


# simple run
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather_without_error_handling(city_name)
