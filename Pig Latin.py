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
        for x in range(0, len(letters)):
            if letters[x].lower() in consonents:
                break
            else:
                start.append(letters[x])
        break
                
for i in start:
    letters.append(i)

for i in letters:
    print(i, end="")
