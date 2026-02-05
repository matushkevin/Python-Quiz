#Create a list of 5 fruits and print the first and last.
fruits = ["apple", "banana", "cucumber", "dates", "fig"]
print(fruits[0])
print(fruits[4])
#Add two items to a list and print the updated list.
fruits.append("pineapple")
fruits.insert(1, "watermelon")

for fruit in fruits:
    print(fruit)
#Remove one item from a list.
fruits.remove("cucumber")
#Loop through a list and print each item.
for fruit in fruits:
    print(fruit)
#Ask the user for 5 names and store them in a list.
names = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)
print(names)