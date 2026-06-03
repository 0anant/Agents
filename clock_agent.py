import datetime

def lunch_tool():
    now = datetime.datetime.now()
    hour = now.hour

    if hour == 12:
        return "It is exactly lunchtime! Time for pizza!"
    elif hour < 12:
        return "It is not 12 yet. Maybe a small snack?"
    else:
        return "We already have pizza and now we are sleepy!!"

def greeting_tool():
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 6:
        return "Shh.. it is still nighttime. Go back to sleep"
    elif hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"
    
print("The Clock Agent checking wristwatch...")

message = greeting_tool()
print(message)
print(lunch_tool())

print("I hope you have a wonderful day!")