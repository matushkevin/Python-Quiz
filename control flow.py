# Ask for age and print "Adult" or "Minor".
age = int(input("How old are you? "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Ask for a number and check if it’s even or odd.
num = int(input("Enter any muber? "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
Ask for exam score and print:
A (80+)
B (60–79)
C (40–59)
F (<40)
"""
score = int(input("What is your score? "))
if score >= 80:
    print("A")
elif score >= 60:
    print("B")
elif score >= 40:
    print("C")
else:
    print("F")

# Ask for a password and validate it.
password = input("Enter your password? ")
if password.lower == "admin":
    print("You may enter")
else:
    print("Incorrect password!")

"""
Ask for temperature and print:
Cold
Warm
Hot
"""
temp = int(input("What is the current temperature? "))
if temp > 50:
    print("Hot")
elif temp > 30:
    print("Warm")
else:
    print("Cold")