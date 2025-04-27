f = open("emails.txt", "r")
while True:
    
    email = f.read().split("-")
    print(email)
    print("\n\n\n\n\n")
    e = []
    es = []
    for i in range(0, len(email)-1):
        for char in email[i]:
            e.append(char)
        es.append(e)
        e = []
    print(es)
    print("\n\n\n\n\n")
        
    for i in range(0, len(es)):
        email = es[i]
        full = ""
        for i in email:
            full += i
        if "." not in email:
            print(full, "is an invalid email: no dot")
        
        dot = email.index(".")
        atsign = email.index("@")
        if atsign > dot:
            print(full, "is an invalid email: atsign after dot")
            
        
        if full[dot+1:] == "":
            print(full, "is an invalid email: nothing after dot")
            
        
        if atsign == 0:
            print(full, "is an invalid email: nothing before atsign")
            
    break
f.close()
print("Finished")
