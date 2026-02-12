with open("profile.txt", "w") as file:
    file.write("Kevin\n")
    file.write("23\n")
    file.write("Ruiru\n")

with open("profile.txt", "r") as file:
    content = file.read()
    print(content)

with open("profile.txt", "a") as file:
    file.write("Learning Python seriously.\n")