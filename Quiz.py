q = ["what is jamesNC?", "what does arlo do?", "how is Oliver?"]
a = ["cool", "smell", "great"]

score = 0
for i in range (0, len(q)):
    ans = input(q[i])
    if ans == a[i]:
        score +=1
print(score, "/ 3")
