import datetime

now = datetime.datetime.now()
hour = now.hour

print(now)
print(hour)

if hour < 12:
    print("Good morning! The birds are singing!")
elif hour < 18:
    print("Good afternoon! The sun is high!")
else:
    print("Good evening")
