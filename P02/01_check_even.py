number=input("Please enter a POSITIVE integer: ")
try:
    number=int(number)
except ValueError:
    print("That is not a positive integer!")

if number%2==0:
    print(str(number) + " is even!")
else:
    print(str(number) + " is not even!")
