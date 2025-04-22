while True:
    word = input("What is your word?")
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")