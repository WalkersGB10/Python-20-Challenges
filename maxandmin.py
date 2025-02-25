low = int(input("What should lower limit be?"))
high = int(input("What should the upper limit be?"))

nums = []

while True:
    num = int(input("What is your number?"))
    if num >= low and num <= upper:
        nums.append(num)
    if len(nums) > 1:
        print(nums[0])
        print(nums[-1])
