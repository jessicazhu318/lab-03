import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "2d240f66bf074de66058678fb6764057"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
def make_joke() -> Dict:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    return response.json()

def main():
    # weather API
    temp = get_weather("London")
    print(temp)
    
    # random joke API
    joke = make_joke()
    print("Joke: " + joke["setup"])
    print("Answer: " + joke["punchline"])

if __name__ == "__main__":
    main()
