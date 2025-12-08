import requests

def fetch_weather(city):
    api_key = "e09cd24b12714af0f1d8e297e8973824"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("City:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Weather:", description)

    except:
        print("Error: City not found. Please enter a valid city.")
def test_task4():
    # 1. Function must exist
    assert callable(fetch_weather)

    # 2. Valid city should not crash
    fetch_weather("Mumbai")

    # 3. Invalid city should not crash
    fetch_weather("xyz123invalidcity")

    assert True
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    fetch_weather(city_name)
