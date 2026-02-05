#Create a dictionary with name, age, and city.
dict1 = {
    "name" : "Kevin",
    "age" : 23,
    "city" : "Ruiru"
}
#Update one value in the dictionary.
dict1["city"] = "Nairobi"
#Loop through keys and values.
for key, value in dict1.items():
    print(key, ":", value)
#Remove one key from a dictionary.
del dict1["age"]
#Create a nested dictionary (student + grades)
student = {
    "name" : "Khisa",
    "grades" : {
        "math" : 90,
        "eng" : 85,
        "science" : 80
    }
}