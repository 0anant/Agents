import requests
import datetime

def greeting_tool():
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 6:
        return "Shhh... still nighttime!"
    elif hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!!"
    
def weather_call_tool(city):
    print("Calling the Weather Computer for", city, "....")

    url = "https://wttr.in/" + city + "?format=%t+%w"

    try:
        response = requests.get(url)
        weather_text = response.text.strip()
        return weather_text
    except:
        return "Could not get weather. Is the internet working."
    
def clothing_advisor_tool(weather_text):

    temp_string = weather_text.replace("+","").replace("°C", "").strip()
    # print(temp_string)
    temp_wind = temp_string.split()
    # print(temp_wind[0])

    try:
        temp = int(temp_wind[0])
    except:
        return "I am confused by the weather. Wear layers!"
    
    if temp < 10:
        return "It is COLD! Wear a warm coat, hat, and gloves! And it is windy hold on to your hat!"
    elif temp < 20:
        return "It is COOL. Wear a jacket or sweater!"
    elif temp < 30:
        return "It is WARM. A t-shirt is perfect!"
    else:
        return "IT is HOT! Wear shorts and drink water!"

def save_weather_tool(city, weather, advice):
    with open("weather_diary.txt", "a") as file:
        file.write("City:" + city + "\n")
        file.write("Weather:" + weather + "\n")
        file.write("Advice:" + advice + "\n")
        file.write("---\n")
    print("Saved to weather diary!")

print("=" * 40)
print("WELCOME TO THE WEATHER AGENT! ")
print("=" * 40)

greeting = greeting_tool()
print(greeting)

city = input("What city do you want to check? ")

weather = weather_call_tool(city)
print("The weather shows:", weather)

advice = clothing_advisor_tool(weather)
print(advice)

save_weather_tool(city, weather, advice)

print("=" * 40)
print("Stay comfy! Have a wonderful day!")
print("=" * 40)
