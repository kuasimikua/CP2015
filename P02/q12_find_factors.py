#input
integer=input("Please enter a positive integer: ")
try:
    integer=int(integer)
except ValueError:
    print("That is not a valid input")
    exit()

#main
factors=[]

x=2
remainder=integer
while remainder/x:
    if remainder%x==0:
        factors.append(x)
        remainder=remainder/x
    elif x>=integer:
        print(str(factors)[1:-1])
        exit()
    elif remainder%x!=0:
        x=x+1
