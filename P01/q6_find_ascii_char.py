ascii=int(input("Please enter an ASCII code (between 0 & 127): "))
if ascii>=0 and ascii<=127:
    print("The character tied to ths code is " + (chr(ascii)))
else:
    print("Please follow the given parameters!")
