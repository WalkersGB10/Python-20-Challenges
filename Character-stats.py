from random import randint
character = {}

forenames = ["Vladimir", "Joseph", "Georgy", "Nikita", "Leonid", "Yuri", "Konstantin", "Mikhail"]
surnames = ["Lenin", "Stalin", "Malenkov", "Kruschev", "Brezhnev", "Andropov", "Chernenko", "Gorbachev"]
types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ground", "Rock", "Flying", "Ghost", "Dark", "Bug", "Dragon", "Steel", "Fairy", "Psychic", "Ice", "Fighting", "Poison"]
name = forenames[randint(0, 7)] + " " + surnames[randint(0,7)]

bst = 1000
remaining = 6
stat = 5000

character["Name"] = name
while stat > (bst//remaining)+1:
    stat = randint(30, 200)
character["HP"] = randint(30, 200)
bst -= stat
remaining -= 1
stat = 5000

while stat > (bst//remaining)+1:
    stat = randint(30, 200)
character["Speed"] = randint(30, 200)
bst -= stat
remaining -= 1
stat = 5000

while stat > (bst//remaining)+1:
    stat = randint(30, 200)
character["Attack"] = randint(30,200)
bst -= stat
remaining -= 1
stat = 5000

while stat > (bst//remaining)+1:
    stat = randint(30, 200)
character["Defense"] = randint(30,200)
bst -= stat
remaining -= 1
stat = 5000

while stat > (bst//remaining)+1:
    stat = randint(30, 200)
character["SpD"] = randint(30,200)
bst -= stat
remaining -= 1
stat = 5000

while stat > (bst//remaining)+1:
    stat = randint(30, 200)
character["SpA"] = randint(30,200)

character["Type1"] = types[randint(0,len(types))]
types.remove(character["Type1"])
character["Type2"] = types[randint(0,len(types))]

print(character)

f = open("character-stats.txt", "a")
f.write(str(character["Name"])+"\n"+str(character["HP"])+"\n"+str(character["Speed"])+"\n"+str(character["Attack"])+"\n"+str(character["Defense"])+"\n"+str(character["SpD"])+"\n"+str(character["SpA"])+"\n"+str(character["Type1"])+"\n"+str(character["Type2"])+"\n")
f.close()
