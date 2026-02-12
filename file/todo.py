with open("todo.txt", "a") as file:
    for i in range(1, 4):
        task = input(f"Task {i}: ")
        file.write(f"{i}. {task}.\n")

with open("todo.txt", "r") as file:
    for line in file:
        print(line.strip())