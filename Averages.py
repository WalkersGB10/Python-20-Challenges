import statistics
numbers = []
print("If you want to stop at any time, enter STOP")
while True:
    ans = input("What is your number?")
    if ans == "STOP":
        break
    else:
        numbers.append(int(ans))
numbers.sort()

total = 0
for num in range(0, len(numbers)):
    total += numbers[num]
print("The mean of your numbers was", total/len(numbers))
print("The median of your numbers was", statistics.median(numbers))
print("The mode of your numbers was", statistics.mode(numbers))

ans = input("Would you like to save your numbers to a text file?")
if ans.lower()[0] == "y":
    ans =input("Would you like to save your numbers or read them?")
    if ans.lower()[0] == "s":
        f = open("averages.txt", "w")
        for num in numbers:
            f.write(str(num) + " ")
        f.close()
    else:
        f = open("averages.txt", "r")
        stuff = f.read()
        print(stuff.split())
        f.close()
