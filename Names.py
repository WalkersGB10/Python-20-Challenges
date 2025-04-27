def pos(people):
    ans = int(input("What position would you like?"))
    print(people[ans-1])
def sec(people):
    lower = int(input("What is the starting position?"))
    upper = int(input("What is the ending position?"))
    print(people[lower-1:upper])
def rem(people):
    ans = input("Who would you like to remove?")
    people.pop(ans)
def clean(people):
    for i in people:
        people[i] = people[i].lower()

print("To stop adding to a list at any time enter STOP")
people = []

while True:
    ans = input("What is the next name?")
    if ans == "STOP":
        break
    else:
        people.append(ans)
        
ans = int(input("""Would you like to
1. choose a position in the list
2. choose a section of the list
3. remove an item from the list
4. make the list lowercase"""))
if ans == 1:
    pos(people)
elif ans == 2:
    sec(people)
elif ans == 3:
    rem(people)
elif ans == 4:
    clean(people)
