def write_diary_tool(entry):
    with open("dairy.txt", "w") as file:
        file.write(entry)
    print("Diary is updated")

def read_tool():
    with open("dairy.txt", "r") as file:
        words = file.read()
        return words
    
print("Diary Agent is running....")
print("Let me read read what I wrote...")

write_diary_tool("I love learning new things related to tech, specially related to AI.")
write_diary_tool("My agent loves pizza!!")

memory = read_tool()

print("My Dairy says", memory)
print("My Diary Agent is sleeping...")
