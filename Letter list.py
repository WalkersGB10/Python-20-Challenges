words = ["tacocat", "racecar", "oliver", "bradford", "high", "mill", "pneumonoultramicroscopicsilicovolcanoconiosis", "hippopotomonstrosesquippedaliophobia", "oyster", "wellington", "word", "can", "they", "be", "numbers", "fifteen"]

letter = input("What is your letter?").lower()[0]

accepted = []
for i in words:
    if i[0] == letter:
        accepted.append(i)
for i in accepted:
    print(i)
if len(accepted) == 0:
    print("No words in the list start with", letter)

else:
    print("All begin with", letter)
