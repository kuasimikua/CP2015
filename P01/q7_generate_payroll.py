name=input("Enter your name: ")

hours=input("Enter hours worked weekly: ")
if not hours.isdigit():
    print("That's not a positive integer! :(")
    exit()
else:
    int(hours)

pay_rate=input("Enter hourly pay rate: ")
try:
    float(pay_rate)
except ValueError:
    print("That's not a float!")
    exit() 

cpf=input("Enter CPF contribution rate(%): ")
try:
    float(cpf)
except ValueError:
    print("That's not a float!")
    exit()

print("Payroll statement for " + name)
print("Number of hours worked in a week = "+hours)
print("Hourly pay rate = $"+pay_rate)
print("Gross pay = $"+ str(float(hours)*float(pay_rate)))
gross_pay=float((float(hours))*(float(pay_rate)))
cpf_percent= (float(cpf))/100
cpf_contribution=gross_pay*cpf_percent
print(("CPF contribution at "+cpf+"% = $")+ str(cpf_contribution))
net_pay=str(gross_pay-cpf_contribution)
print("Net pay = $" + net_pay)
