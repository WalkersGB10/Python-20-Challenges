f = open("Passwords.txt", "r")
stuff = f.read().split()
users = {}
for i in range(0, len(stuff)-1, 2):
    users[stuff[i]] = stuff[i+1]

print(users)

f.close()

ans = input("Would you like to\n1. see your password\n2. set your password")
if ans == "1":
    user = input("What is your username?")
    if user in users.keys():
        print(users[user])
else:

    f = open("Passwords.txt", "a")

    user = input("What is your name?")
    password = input("What is your password?")
    
    f.write(user + " " + password + " ")
    
    f.close()
