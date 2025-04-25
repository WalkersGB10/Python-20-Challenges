stuff = []
shop = []
priority = []
pay = []
quantity = []

def add():
  item = input("What is the item?")
  stuff.append(item)
  location = input("Where will you purchase", item)
  shop.append(location)
  scale = input("On a scale of 1-10 what priority is", item)
  priority.append(scale)
  price = int(input("How much does", item, "cost"))
  pay.append(price)
  amount = int(input("How many", item, "will you buy"))
  quantity.append(amount)

def remove():
  item = input("What would you like to remove?")
  if item in stuff:
    pos = stuff.index(item)
    stuff.pop(pos)
    shop.pop(pos)
    priority.pop(pos)
    pay.pop(pos)
    quantity.pop(pos)

while True:
  ans = input("Would you like to view the list, add to shopping list or remove from it?").lower()[0]
  if ans == "a":
    add()
  elif ans == "r":
    remove()
  else:
    break

for i in range(0, len(stuff)):
  print("Item:", stuff[i])
  print("Location:", shop[i])
  print("Priority:", priority[i])
  print("Price:", pay[i])
  print("Quantity:", quantity[i])

total = 0

for i in range(0, len(stuff)):
  total += pay[i] * quantity[i]

print("Your total cost is:", total)
