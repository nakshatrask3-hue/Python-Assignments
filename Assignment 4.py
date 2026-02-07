# To create a dictionary of data of a student in MIT

info = {
    "name": "Nakshatra",
    "age": 19,
    "is_adult": True,
    "topics": ("list","tuple"),
    "subjects": ["python", "c", "java"],
    "language": "Python Language",
    "marks": 98.76
}

# Printing Values of the dictionary with the help of the keys
print(info["name"])
print(info["age"])
print(info["is_adult"])
print(info["topics"])
print(info["subjects"])
print(info["language"])
print(info["marks"])

#Adding extra information in the  dictionary
info["result"] = "pass"
print(info["result"])                      #Printing the information