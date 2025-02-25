from random import randint
difficulty = input("Would you like easy mode, normal or hard?").lower()[0]
if difficulty == "n":
    dig1, dig2, dig3, dig4 = str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9))
    tries = 0
   
    while True:
        tries += 1
        ans = input("what is your guess?")
        correct = 0
        if dig1 in ans:
            correct += 1
        if dig2 in ans:
            correct += 1
        if dig3 in ans:
            correct +=1
        if dig4 in ans:
            correct += 1
        
        if ans == dig1+dig2+dig3+dig4:
            break
        else:
            print("You got", correct, "correct")
elif difficulty == "e":        
    dig1, dig2, dig3, dig4 = str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9))
    tries = 0
   
    while True:
        tries += 1
        ans = input("what is your guess?")
        correct = 0
        if dig1 == ans[0]:
            print("First digit correct")
        if dig2 == ans[1]:
            print("Second digit correct")
        if dig3 == ans[2]:
            print("Third digit correct")
        if dig4 == ans[3]:
            print("Fourth digit correct")
        
        if ans == dig1+dig2+dig3+dig4:
            break
        else:
            print("You got", correct, "correct")
elif difficulty == "h":        
    dig1, dig2, dig3, dig4, dig5 = str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9))
    tries = 0
    
    while True:
        tries += 1
        ans = input("what is your guess?")
        correct = 0
        if dig1 in ans:
            correct += 1
        if dig2 in ans:
            correct += 1
        if dig3 in ans:
            correct +=1
        if dig4 in ans:
            correct += 1
        if dig5 in ans:
            correct += 1
        
        if ans == dig1+dig2+dig3+dig4:
            break
        else:
            print("You got", correct, "correct")
print("Congratulations")
print("That took you", tries, "attempts")

name = input("What is your name?")

f = open("Highscores.txt", "a")

f.write(name + "-" + str(tries) + "-")

f.close()

f = open("Highscores.txt", "r")
stuff = f.read()
scores = stuff.split("-")

for i in range(0, len(scores)-1, 2):
    print(scores[i], scores[i+1])
    

f.close()