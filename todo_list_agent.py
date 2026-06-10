def planner(task):
    """
    The Agent's TO-DO List Maker!
    Takes a task, returns a list of steps.
    """

    plans = {
        "homework": [
            "Ask what subject and due date",
            "Break into small chunks",
            "Estimate time for each chunk",
            "Make a daily schedule",
            "Start with the hardest part"
        ],
        "birthday party": [
            "Ask how many guests and budget.",
            "Choose location and theme",
            "Send Invites",
            "Order cake and snacks",
            "Plan games and music",
            "Buy decorations"
            "set up early"
        ],
        "clean room": [
            "Pick up toys and clothes",
            "Make the bed",
            "Organnize desk",
            "Vacuum or sweep",
            "Take a photo - admmire your work!"
        ]
    }

    if task in plans:
        return plans[task]
    
    else:
        return [
            f"Understand the what the '{task} means",
            "Ask questions if I'm confused",
            "Break it into 3 small steps",
            "Do step 1, then check",
            "Do step 2, then check",
            "Do step 3, then check",
            "Ask: Did it work ? If not, try again!"
        ]
    
user_task = input("What do you need help with?")
my_plan = planner(user_task)

print(f"\n Task: {user_task}")
print("YUour Agent's Plan:")
for i, step in enumerate(my_plan, 1):
    print(f" {i}. {step}")