vowels = "aeiou"
totals = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
amount = 0
word = input("WORD?").lower()

for i in word:
    if i in vowels:
        amount += 1
        totals[i] += 1

print(amount)
print(totals)
