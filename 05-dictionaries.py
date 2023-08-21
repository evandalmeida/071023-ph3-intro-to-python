# const teacher = {
#     name: "Chett",
#     city: "Brooklyn",
#     numberOfCats: 2
# }

teacher = {
    "name": "Chett",
    "city": "Brooklyn",
    "numberOfCats": 2
}

# console.log(teacher)
print(teacher)

# console.log(teacher.name)
print(teacher["name"])



# teacher.name = "Mohammad"
# console.log(teacher.name)
teacher["name"] = "Mohammad"
print(teacher["name"])



# const teacher.catNames = ["Octavia", "Ursula"]
# const firstPet = teacher.catNames[0]
# console.log( `Teacher's First Pet: ${firstPet}` )
teacher["catNames"] = ["Octavia", "Ursula"]
first_pet = teacher["catNames"][0]
print(f"Teacher's First Pet: {first_pet}")



# const doesNotExist = teacher.age
# console.log(doesNotExist)
does_not_exist = teacher["age"]
print(does_not_exist)



# teacher = {...teacher, age: 500}
# console.log(teacher)
teacher["age"] = 500
print(teacher)
