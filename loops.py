#Print numbers 1–10 using a for loop.
for i in range(1, 11, 1):
    print(i)
#Print numbers 10–1 using a while loop.
count = 10
while count >= 1:
    print(count)
    count -= 1
#Ask for a number and print its multiplication table.
num = int(input("Provide a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#Print only even numbers between 1 and 50.
for Num in range(1, 50):
    if Num % 2 == 0:
        print(Num)
#Loop through a name and print each character.
for u in "banana":
    print(u)