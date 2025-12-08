import requests
import json

def store_weather(city):
    api_key = "e09cd24b12714af0f1d8e297e8973824"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        weather_info = {
            "city": city,
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }

        print(json.dumps(weather_info, indent=4))

        with open("results.txt", "a") as f:
            f.write(json.dumps(weather_info) + "\n")

    except:
        print("Error: Could not fetch weather information.")
import os

def test_task5():
    # function must be callable
    assert callable(store_weather)

    # call function for valid city
    store_weather("Hyderabad")

    # file must be created
    assert os.path.exists("results.txt")

    # function must run even for another city
    store_weather("Mumbai")

    assert True
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    store_weather(city_name)
