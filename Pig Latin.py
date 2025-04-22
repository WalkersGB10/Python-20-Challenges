word = input("What is your word?").lower()
letters = []
for i in word:
    letters.append(i)
consonents =  "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

start = ["-"]
a = 0
while a <1:
    if letters[0] in consonents:
        start.append(letters[0])
        letters.remove(letters[0])
        print(start)
        print(letters)
        for x in range(0, len(letters)):
            if letters[x].lower() in consonents:
                print(start)
                print(letters)
                break
            else:
                start.append(letters[x])
                print(start)
                print(letters)
        break
                
for i in start:
    letters.append(i)

for i in letters:
    print(i, end="")