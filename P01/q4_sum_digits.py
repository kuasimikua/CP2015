integer=int(input("Please enter a number between 0 and 1000: "))
ones_digit=integer%10
minus_ones=integer//10
tens_digit=minus_ones%10
hundreds_digit=minus_ones//10
sum_digits=ones_digit + tens_digit +hundreds_digit
if integer<1000:
    print("The sum of digits is "+str((sum_digits)))
elif integer>=1000:
    print("Please follow the parameter >:(")
