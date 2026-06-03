import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

joke_data = response.json()

print(joke_data["setup"])
print(joke_data["punchline"])