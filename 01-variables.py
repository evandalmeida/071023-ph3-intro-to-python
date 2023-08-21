# JS:
# let name = "Bob"
# console.log(name)
name = "Bob"
print(name)



# let species = "Raccoon"
# console.log(species)
species = "Raccoon"
print(species)



# let rabid = false
# console.log(rabid)
rabid = False



# name = `Bob the ${species}` BACKTICKS ARE NOT VALID CHARACTERS IN PY
# console.log(name)
print(f"Bob the {species}")



# let numberOfRaccoonsInNYC = "300"
# console.log( `number of raccoons in NYC: ${numberOfRaccoonsInNewYork}` )
numberOfRaccoonsInNYC = 300 
print(f"Number of raccoons in NYC: { numberOfRaccoonsInNYC } ")



# numberOfRaccoonsInNewYork = parseInt( numberOfRaccoonsInNewYork )
numberOfRaccoonsInNYC = int(numberOfRaccoonsInNYC)
print(type(numberOfRaccoonsInNYC)) 



# numberOfRaccoonsInNewYork += 1
# console.log( `number of raccoons in NYC: ${numberOfRaccoonsInNewYork}` )
numberOfRaccoonsInNYC += 1
print (numberOfRaccoonsInNYC)