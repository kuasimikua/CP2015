n_one=input("Please enter the first number: ")
try:
    int(n_one)
except ValueError:
    print("That is not a valid input")
    exit()
n_two=input("Please enter the second number: ")
try:
    int(n_two)
except ValueError:
    print("That is not a valid input")
    exit()

if n_one<n_two:
    d=n_one
elif n_one>n_two:
    d=n_two
else:
    print("The greatest common divisor is %s" % n_one)
    exit()

temp_one= (n_one)
temp_two= (n_two)
if temp_one%d==0 and temp_two%d==0:
    print("The greatest common divisor is "+ str(d))

else:
    while temp_one%d!=0 or temp_two%d!=0:
        d=d-1
    print("The greatest common divisor is "+ str(d))

