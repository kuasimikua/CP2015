def is_leap(n):
    if (int(year)%4==0) and (int(year)%100!=0):
        return True
    else:
        return False


month=input("Please enter a month (mm): ")
if int(month)>12 or int(month)<0:
    print("That is not a valid month")
    exit()
year=input("Please enter a year (yyyy): ")
if int(year)<0:
    print("That is not a valid year")
    exit()

if int(month) in [1,3,5,7,8,10,12]:
    days=31
elif int(month) in [4,6,9,11]:
    days=30
else:
    if is_leap(int(year)):
        days=29
    else:
        days=28

month_names={1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

print("There are "+ str(days) + " days in " +(month_names[int(month)]) + ", year " + year)
