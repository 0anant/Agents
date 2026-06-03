import requests

def cat_fact_tool():
    response = requests.get("https://catfact.ninja/fact")

    cat_data = response.json()
    print(cat_data["fact"])

def weather_tool(city):
    print("📞 Calling the Weather Computer for", city, "...")
    
    url = "https://wttr.in/" + city + "?format=%C+%t"

    response = requests.get(url)
    print(response)
    return response.text

print("🌤️Weather Agent is here!!")

city_name = input("What city do you want to check? ")

weather  = weather_tool(city_name)


print("The weather in", city_name, "is:",weather)
cat_fact_tool()
cat_fact_tool()

