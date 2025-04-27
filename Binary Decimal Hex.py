hbvalues = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

def dec2bin(num):
  num = int(num)
  if num > 255 or num < 0:
    print("Invalid Input")
    return
  
  ans = ""
  checks = [127, 63, 31, 15, 7, 3, 1, 0]

  for i in range(0, 8):
    if num > checks[i]:
      ans += "1"
      num -= (checks[i] + 1)
    else:
      ans += "0"

  return ans

def bin2dec(num):
  num = num[::-1]
  ans = 0
  x = 1
  for i in num:
    ans += int(i) * x
    x *= 2

  return ans

def hex2bin(num):
  if len(num) != 2:
    print("Invalid input")
    return
  
  dig1 = hbvalues[num[0]]
  dig2 = hbvalues[num[1]]
  ans = dig1 + dig2

  return ans

def bin2hex(num):
  dig1 = num[0:4]
  dig2 = num[4:8]
  pos1 = list(hbvalues.values()).index(dig1)
  pos2 = list(hbvalues.values()).index(dig2)
  dig1 = list(hbvalues.keys())[pos1]
  dig2 = list(hbvalues.keys())[pos2]
  ans = dig1 + dig2

  return ans

while True:
  response = int(input("""Would you like to go from:
  1. decimal to binary
  2. decimal to hex
  3. binary to decimal
  4. binary to hex
  5. hex to decimal
  6. hex to binary
  7. QUIT"""))
  if response == 1:
    num = input("What is your decimal number?")
    result = dec2bin(num)
    print(num, "in binary is", result)
  elif response == 2:
    num = input("What is your decimal number")
    result = dec2bin(num)
    result = bin2hex(result)
    print(num, "in hex is", result)
  elif response == 3:
    num = input("What is your binary number?")
    result = bin2dec(num)
    print(num, "in decimal is", result)
  elif response == 4:
    num = input("What is your binary number?")
    result = bin2hex(num)
    print(num, "in hex is", result)
  elif response == 5:
    num = input("What is your hex number?")
    result = hex2bin(num)
    result = bin2dec(result)
    print(num, "in decimal is", result)
  elif response == 6:
    num = input("What is your hex number?")
    result = hex2bin(num)
    print(num, "in binary is", result)
  else:
    break
