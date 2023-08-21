# const animals = ["Aardvark", "Bobcat", "Cardinal", "Deer"]
# console.log(animals)
animals = ["Aardvark", "Bobcat", "Cardinal", "Deer"]
print( animals )



# console.log(`First animal: ${animals[0]}`)
print( f"First animal: {animals[0]}" )



# animals.push("Elephant")
# console.log(animals)
animals.append("Elephant")
print(animals)



# animals.pop()
# console.log(animals)
animals.pop()
print(animals)



# console.log(`There are ${animals.length} animals`)
print( f"There are {len(animals)} animals" )
#len is a default function 



# const randomAnimal = animals[Math.floor(Math.random() * animals.length())]
# console.log(randomAnimal)
import random
random_animal = random.choice(animals)
print(random_animal)
# random needs to be improted becasue it a module (random.choice selects a rando choice and random.shuffle reorganizes the list)


# const firstTwoAnimals = animals.slice(0, 2)
# console.log(`First two animals: ${firstTwoAnimals}`)
firts_two_animals = animals[:2]
print(f"First two animals {firts_two_animals}")
# this returns First two animals ['Aardvark', 'Bobcat'] to fix that:
animal_names = " and ".join(firts_two_animals)
print(f"First two animals {animal_names}")
#indexing works the same way as js



# const lastAnimal = animals[animals.length - 1]
# console.log(lastAnimal)
last_animal = animals[-1]
print(last_animal)



# function printEachAnimal() {
#     for (let i = 0; i < animals.length; i++) {
#         console.log( animals[i] )
#     }
# }
# printEachAnimal()
def print_each_animal():
    for animal in animals:
        print(animal)

print_each_animal()



# const animalsToLowerCase = animals.map( animal => animal.toLowerCase() )
# console.log(animalsToLowerCase)
animal_to_lowercase = [animal.lower() for animal in animals]
print(animal_to_lowercase)
#this is called "list comprehension" similar to a .map but the logic is backwards so [function... for... in...]



# const setOfNumbers = new Set(1,2,3,3,4,4,5)
# console.log(setOfNumbers) // will return Set [1,2,3]
set_of_numbers = {1, 2, 3, 3, 4, 4, 5}
print(set_of_numbers)


# A SET IN PY will never have duplicates and is declared with {} so the set from JS if ran in PY will return wo duplicates 