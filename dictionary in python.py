info = {
    "name":" MuhammadAon Rafay",
    "age":25,
    "city":"Karachi",
    "skills":["Python", "JavaScript", "HTML", "CSS"],
    "is_student":False,
    "Status":"Active",
    "Marks":{
        "Math": 85,
        "Science": 90,
        "English": 88
    }

}

print(info)  # Print the entire dictionary
print(info["name"])
print("Name:", info["name"])  # Access the value associated with the key "name"
print("Age:", info["age"])  # Access the value associated with the key "age 

print(info.keys())  # Print all keys in the dictionary
