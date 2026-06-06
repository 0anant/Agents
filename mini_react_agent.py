import requests
import json

def weather_tool(city):
    print("  [TOOL] Calling weather for", city, "...")

    try:
        url = "https://wttr.in/" + city + "?format=%C+%t"
        response = requests.get(url)
        return response.text.strip()
    except:
        return "Weather unavailable"
    

def math_tool(expression):
    print("  [TOOL] Calculating:", expression, "....")
    try:

        safe = all(c in "01223456789+-/(). " for c in expression)
        if not safe:
            return "I can only do simple maths!"
        result = eval(expression)
        return str(result)
    except:
        return "Math error!"
    
def memory_tool(action, key, value=None):
    print("   [TOOL] MEMORY",action, "for", key, "...")

    try:
        with open("react_memory.json", "r") as file:
            memories = json.load(file)
    except:
        memories = {}

    if action == "save":
        memories[key] = value
        with open("react_memory.json", "w") as file:
            json.dump(memories, file, indent=4)
        return "Saved!"
    
    elif action == "find":
        if key in memories:
            return memories[key]
        else:
            return "Not found!"
        
    elif action == "show":
        return str(memories)
    
    else:
        return "Unknown memory action!"
    

def react_agent(question):
    print("\n" + "="*40)
    print("You asked:", question)
    print("\n" + "="*40)

    print("\n Reasoning...")
    question_lower = question.lower()

    weather_array = ["weather", "rain", "sunny", "temperature", "cold", "hot", "umbrella", "coat", "wear""weather", "rain", "sunny", "temperature", "cold", "hot", "umbrella", "coat", "wear"]

    city_array = ["london", "paris", "tokyo", "new york", "dubai", "moscow"]

    if any(word in question_lower for word in weather_array):
        print("   This is about WEATHER. I need the weather tool!")
        tool_choice = "weather"

        city = "London"
        for possible_city in city_array:
            if possible_city in question_lower:
                city = possible_city
                break

        print("\n ACTING...")
        observation = weather_tool(city)

        print("\n REASONING AGAIN...")
        print("  Weather says:", observation)

        if "rain" in observation.lower() or "drizzle" in observation.lower() or "shower" in observation.lower():
            answer = "Yes It looks rainy in " + city + ".Bring an umbrella! -- (" + observation + ")"

        


