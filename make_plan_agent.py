def make_plan(task):
    """
    This is the Planner Brain!
    It looks at the task and returns a list of steps.
    """

    if task == "homework":
        return [
            "1. Ask what subject",
            "2. Ask when it's due",
            "3. Break into small chunks",
            "4. Make a schedule",
            "5. Check if the plan looks good"
        ]
    elif task == "pack lunch":
        return [
            "1. Check what's in the fridge",
            "2. Pick a main, a fruit, and a drink",
            "3. Put it in the lunchbox",
            "4. Close the lid tight!"
        ]
    else:
        return ["1. Think about the task",
                "2. Break it into small steps"]


def smart_plannner(task):
    plan = [
        f"1. Understand the task: '{task}'",
        "2. Think about what I need to know",
        "3. Break it innto 3 small steps",
        "4. Do step 1",
        "5. Do step 2",
        "6. Do step 3",
        "7. Check if it looks good"
    ]
    return plan
print(smart_plannner("Build a lego castle"))
print(smart_plannner("plan a birthday party"))

my_task = "homework"
plan = make_plan(my_task)

print(f" Task: {my_task}")
print("My Plan:")
for step in plan:
    print(f"     {step}")