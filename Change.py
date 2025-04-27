while True:
  cost = float(input("How much did it cost?")) * 100
  paid = float(input("How much did you pay?")) * 100
  
  change = paid - cost
  
  coins = {1: 0, 2: 0, 5:0, 10:0, 20:0, 50:0, 100:0, 200:0}
  
  while change >= 200:
    coins[200] += 1
    change -= 200
  
  while change >= 100:
    coins[100] += 1
    change -= 100
  
  while change >= 50:
    coins[50] += 1
    change -= 50
  
  while change >= 20:
    coins[20] += 1
    change -= 20
  
  while change >= 10:
    coins[10] += 1
    change -= 10
  
  while change >= 5:
    coins[5] += 1
    change -= 5
  
  while change >= 2:
    coins[2] += 1
    change -= 2
  
  while change >= 1:
    coins[1] += 1
    change -= 1
  
  print(coins)
