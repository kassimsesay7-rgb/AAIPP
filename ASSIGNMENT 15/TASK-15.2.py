import requests
import json

def get_weather_with_error_handling(city):
    api_key = "e09cd24b12714af0f1d8e297e8973824"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=4))

    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")
def test_task2():
    # 1. Function must be callable
    assert callable(get_weather_with_error_handling)

    # 2. Should NOT crash on invalid city
    try:
        get_weather_with_error_handling("abcdefgxyz123")
    except Exception:
        assert False, "Function should handle invalid city errors"

    # 3. Dummy assertion
    assert True
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather_with_error_handling(city_name)
