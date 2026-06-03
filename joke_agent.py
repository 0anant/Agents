import requests

def joke_tool():
    print("Calling the joke computer!!")

    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()

    setup = joke_data["setup"]
    punchline = joke_data["punchline"]

    return setup, punchline

print("Joke Agent is starting ...")

setup, punchline = joke_tool()

print("Here is a joke for you!!")
print(setup)
print(punchline)

print("Ha ha ha !!!..")