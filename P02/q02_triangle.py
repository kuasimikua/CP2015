print("Hello! Please enter the three lengths of your triangle!")
#INPUTS
length_a=input("Edge A (cm)= ")
try:
    length_a=float(length_a)
except ValueError:
    print("Please enter a positive number!")
    exit()
length_b=input("Edge B (cm)= ")

try:
    length_b=float(length_b)
except ValueError:
    print("Please enter a positive number!")
    exit()

length_c=input("Edge C (cm)= ")

try:
    length_c=float(length_c)
except ValueError:
    print("Please enter a positive number!")
    exit()
#TESTING THE LENGTHS
sum_ab=length_a+length_b
if sum_ab<length_c:
    print("Your inputs cannot form a triangle :(")
else:
    sum_ab=sum_ab

sum_ac=length_a+length_c
if sum_ac<length_b:
    print("Your inputs cannot form a triangle :(")
else:
    sum_ac=sum_ac

sum_bc=length_b+length_c
if sum_bc<length_a:
    print("Your inputs cannot form a triangle :(")
else:
    sum_bc=sum_bc

#CALCULATING PERIMETER
perimeter=length_a+length_b+length_c
print("The perimeter of this triangle is= "+str(perimeter)+"cm")
