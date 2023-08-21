# function doStuff() {
#   return "This function does stuff!"
# }
def doStuff():
  return "This function does stuff"



# console.log( doStuff() )
print( doStuff() )



# function addition(x,y) {
#   return x + y
# }
def addition(x,y):
  return x + y

# console.log( addition(1,2) )
print( addition(1,2) )

# console.log( addition("3", 4) )
print( addition("3", str(4)) ) 
# returns 34 when you string it because it puts the strings together so to get 3 + 4 = 7
print( addition(int("3"), 4) )

# console.log( addition(5.6, 7) )
print( addition(5.6, 7) )



# let name = "Bob"
name = "Bob"

# function sayHiBob() {
#   return `Hello ${name}`
# }
def sayHiBob():
  return f"Hello {name}"

# console.log( sayHiBob() )
print( sayHiBob() )



# function countdown(number) {
#   let i = number
#   while (i > 0) {
#     console.log(i)
#     i -= 1
#   }
#   console.log('HAPPY NEW YEAR!')
# }
def countdown(number):
  i = number
  while i > 0 :
    print(i)
    i -= 1
  print("HAPPY NEW YEAR")

countdown(99999999999999)