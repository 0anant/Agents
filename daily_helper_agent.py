import requests
import json
import datetime
from playwright.sync_api import sync_playwright

#--- TOOL 1: Weather Tool -------
def weather_tool(city):
    print("Checking weather for ", city, "...")

    try:
        url = "https://wttr.in/" + city + "?format=%C+%t"
        response = requests.get(url)
        return response.text.strip()
    except:
        return "Weather is not available.."
    
#--- TOOL 2: Browser Snapshot -------
def browser_tool(url, photo_name="snapshot.png"):
    print("Driving to", url , "...")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            page.screenshot(path=photo_name)
            title = page.title()
            browser.close()
        return "Photo saved as " + photo_name + "!Title: " + title
    except:
        return "Browser drive failed.."
    
#--- TOOL 3: Diary -----
def dairy_tool(report):
    print("Saving to diary....")

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d, %H:%M")

    entry = {
        "time": timestamp,
        "report": report
    }

    try:
        with open("daily_dairy.json", "r") as file:
            dairy = file.load(file)
    except:
        dairy = []

    dairy.append(report)

    with open("daily_dairy.json", "w") as file:
        json.dump(dairy, file, indent=4)
    return "Saved!"

#---- TOOL 4: Morning Report Builder -----
def build_report(weather, browser_result, city):
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greeting = "Good morning!.."
    elif hour < 18:
        greeting = "Good Afternoon!.."
    else:
        greeting = "Good Evening!..."

    temp_string = weather.replace("+","").replace("%C","").strip()
    try:
        temp = int(temp_string.split()[0])
        if temp < 10:
            advice = "Brrr! Wear a warm coat, hat, and gloves! "
        elif temp < 20:
            advice = "Chilly! A jacket or sweater is perfect.."
        elif temp < 30:
            advice = "Nice! A t-shirt or light clothes.."
        else:
            advice = "Hot! Wear shorts and dronk water!"
    
    except:
        advice = "Couldn't read temperature. Wear layers!"

    report = f"""
{'='* 40}
{greeting}t
{'='* 40}
Location: {city}
Weather: {weather}
Clothing Advice: {advice}
Browser Mmission: {browser_result}
Report Time: {now.strftime("%Y-%m-%d, %H:%M")}
{'=' * 40}
Have a wonderful day!
{'='*40}
"""
    return report

#------- THE MORNING ROUTINE ---------
def morning_routine(city="London",check_url="https://www.wikipedia.org"):
    print("\n" + "="*50)
    print("DAILY HELPER AGENT WAKING UP!")
    print("="*50)

    #Step 1: Check Weather
    print("\n STEP 1: Weather Check")
    weather = weather_tool(city)
    print("    Result:", weather)

    #Step 2: Browser mission
    print("\n STEP 2: Browser Snapshot")
    browser_result = browser_tool(check_url,"morning_snaphot.png")
    print("    RESULT:", browser_result)

    #Step 3: Build Report
    print("\n STEP 3: Building Report")
    report = build_report(weather, browser_result, city)

    #Step 5: Show report
    print("\n STEP 5: Your Morning Report")
    print(report)


    print("="*50)
    print("DAILY HELPER GOING BACK TO SLEEP !!!")
    print("="*50)

    #----- ON-DEMAND TOOLS -------
def quick_weather(city):
        """Ask for weather anytime!"""
        result = weather_tool(city)
        print(f"\n Weather in {city}: {result}\n")

def quick_snapshot(url):
        """Take a photo of any website anytime!"""
        result = browser_tool(url, "quick_snapshot.png")
        print(f"\n {result}\n")

def read_dairy():
        """Read all past reports!"""
        try:
            with open("daily_dairy.json", "r") as file:
                diary = json.load(file)
                print("\n Your Diary:")
                for i, entry in enumerate(diary, 1):
                    print(f"\n--- Entry {i} ----")
                    print(f"Time: {entry['time']}")
                    print(f"Report preview:{entry['report'][:100]}...")
        except:
            print("\n Diary is empty! Run morning routine first.\n")


#----- Run the AGENNT!------
print("="*50)
print("WELCOME TO THE DAILY HELPER AGENT!")
print("="*50)
print("\nWhat would you like to do?")
print("1. Run MORNING ROUTINE (full check)")
print("2.Quick Weather check")
print("3.Quick website snapshot")
print("4.Read DIARY")
print("5. EXIT")

while True:
    choice = input("\nYour choice (1-5): ").strip()

    if choice == "1":
        city = input("What city? (press Enter for London): ").strip()
        if not city:
            city = "London"
        url = input("What website to snapshot? (press Enter for Wikipedia): ").strip()
        if not url:
            url = "https://www.wikipedia.org"
        morning_routine(city, url)
    
    elif choice == "2":
        city = input("What city? ").strip()
        quick_weather(city)
    elif choice == "3":
        url = input("What website? ").strip()
        quick_snapshot(url)
        
    elif choice == "4":
        read_dairy()
        
    elif choice == "5":
        print("\n👋 Goodbye! Have a wonderful day!")
        break
        
    else:
        print("\n❓ Please type 1, 2, 3, 4, or 5!")