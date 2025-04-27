from random import randint
words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"]

guessed = []

word = words[randint(0, 25)]
correct = 0
length = len(word)
lives = 6
display = []
for i in word:
  display.append("_")

while True:
  survive = 0
  again = 0
  for i in display:
    print(i, end = "")

  ans = input("\nWhat letter would you like to guess?").lower()[0]

  if ans in guessed:
    survive = 1
  elif ans not in guessed:
    guessed.append(ans)
    for i in range(0, length):
      if ans == word[i]:
        survive = 1
        correct += 1
        display[i] = ans

    if survive == 0:
      lives -= 1
      print("Not in word")
      print(lives, "lives remaining")
    
    if lives == 0:
      print("You lose")
      break 
    
    for i in display:
      if i == "_":
        again = 1
    
    if again == 0:
      break
    
if survive == 1:
  print("You Win")        
