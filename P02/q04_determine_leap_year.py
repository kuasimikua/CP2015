year= input("Enter year: ")
try:
    year=int(year)
except ValueError:
    print("That is not a valid input!")
    exit()

if year%4==0:
    if year%100!=0:
        print("Leap")
    else:
        print("Non-Leap")
else:
    print("Non-leap")
