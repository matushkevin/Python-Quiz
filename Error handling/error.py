try:
    num = int(input("Enter a number: "))
    print("Your number is", num)
except ValueError:
    print("Error")

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a / b)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    ("Can't be divided by zero")

while True:
    try:
        number = int(input("Enter a number: "))
        print("You entered:", number)
        break   # Exit loop if successful
    except ValueError:
        print("Invalid input. Please enter a valid number.")

try:
    c = int(input("Enter the number: "))
except ValueError:
    print("Invalid input!")
else:
    print("Your number is", c)
finally:
    print("Program executed.")