age = 22
certificate = False

if age >=18:
    if certificate == True:
        print("You will be hired")
    else:
        print("Cannot hire due to no certificate")
else:
    print("Cannot hire, age is less than 18")