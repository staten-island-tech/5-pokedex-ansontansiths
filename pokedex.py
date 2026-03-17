import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
print(data[0])

def pokemondictionary():

 print(input("What language would you like to set the pokedex to? (english, japanese, chinese, french)"))
 if input == "english":
  print("language has been set to english")
 elif input == "japanese":
  print("language has been set to japanese")
 elif input == "chinese":
  print("language has been set to chinese")
 elif input == "french":
  print("language has been set to french")
 else: print("we do not have that language, please try again")

if input == "english" or input == "japanese" or input == "chinese" or input == "french":
  print("what pokemon would you like to search for")
  if input == json.load(pokedex)["name"]["english"]:
   print("pokemon found")
  else: print("pokemon not found, please try again")

  pokemondictionary()