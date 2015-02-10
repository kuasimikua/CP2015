score=input("Please enter a score (integer) from 0 to 100: ")
try:
    score=int(score)
except ValueError:
    print("Invalid! Score must be an integer within 0 - 100.")
    exit()

if 0<=score<=35:
    print("Your grade is a U")
elif 35<=score<=44:
    print("Your grade is an S")
elif 45<=score<=49:
    print("Your grade is an E")
elif 50<=score<=54:
    print("Your grade is a D")
elif 55<=score<=59:
    print("Your grade is a C")
elif 60<=score<=69:
    print("Your grade is a B")
elif 70<=score<=100:
    print("Your grade is an A")
else:
    print("That is not a valid score.")
