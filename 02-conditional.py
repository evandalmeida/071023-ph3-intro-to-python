# let name = "Bob"
name = "Bob"



# if (name === "Bob") {
#     console.log("OMG it's Bob!")
# } else {
#     console.log(`Hello ${name} the raccoon`)
# } 
if name == "Bob" :
    print("It's that mf Bob")
else :
    print(f"Hello {name} you raccoon")



# name = "Raphael"
# if (name === "Donatello" || name === "Raphael") {
#     console.log("Cowabunga dude!")
# } else if (name === "Leonardo" || name === "Michelangelo") {
#     console.log("It's turtle time!")
# }
name == "Raphael"
if name == "Donatello"  or  name == "Raphael" :
    print("Cowabunga dude!")
elif name == "Leonardo" or name == "Michelangelo" :
    print("It's turtle time!")
else :
    print("I'am a human")



# let weekday = "Tuesday"
# let pizza = weekday === "Tuesday" ? "Pineapple Pizza" : "Pepperoni Pizza"
weekday = "Tuesday"
pizza = "Pineapple Pizza" if weekday == "Tuesday" else ("Pineapple Pizza")
# ternary statement for PYTHON ^
print(pizza)