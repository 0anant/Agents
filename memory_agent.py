import json

def save_memory_tool(key, value):

    try:
        with open("memory_palace.json", "r") as file:
            memories = json.load(file)
    except:
        memories = {}

    memories[key] = value

    with open("memory_palace.json", "w") as file:
        json.dump(memories, file, indent=4)

    print("Remember:", key, "=", value)

def find_memory_tool(key):
    try:
        with open("memory_palace.json", "r") as file:
            memories = json.load(file)

        if key in memories:
            return memories[key]
        else:
            return "I dont remember that yet!"
        
    except:
        return "I dont have any memories yet!"
    
def show_all_memories_tool():
    try:
        with open("memory_palace.json", "r") as file:
            memories = json.load(file)

        print("My Memory Palace:")
        for key, value in memories.items():
            print(" ", key, ":", value)
        
    except:
        print("My Memory Palaace is empty!")


print("="*40)
print("WELCOME TO THE MEMORY PALACE!!")
print("="*40)

name = input("What is your nname??")

old_color = find_memory_tool(name + "_color")

if old_color != "I dont have any memories yet!":
    print("I remember you:", name, "!")
    print("Your favorite color is", old_color, "!")
else:
    print("Nice to meet you", name, "!")

color = input("What is your favorite color?")
save_memory_tool(name + "_color", color)

pet = input("What is your pet's name ? (or 'none') ")
if pet != "none":
    save_memory_tool(name + "_pet", pet)


print("\nLet me check my palace...")
show_all_memories_tool()

print("\nGoodbye! I will remember you forever!")