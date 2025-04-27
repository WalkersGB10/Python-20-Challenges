low = int(input("What should lower limit be?"))
high = int(input("What should the upper limit be?"))

nums = []

while True:
    num = int(input("What is your number?"))
    if num >= low and num <= high:
        nums.append(num)
    nums.sort()
    if len(nums) > 1:
        print("lowest num:", nums[0])
        print("highest num:", nums[-1])

