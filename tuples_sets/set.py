num = {1, 2, 2, 3, 4}
print(num)

food = {"Ugali", "meat", "rice", "fruits"}
pref = input("What is your favourite food? ")

if pref.lower() in food:
    print("The food is available.")
else:
    print("Sorry, the food is not available")

A = {2, 4, 6, 8, 10}
B = {12, 4, 16, 18, 2}
print(A | B)
print(A & B)
print(A - B)