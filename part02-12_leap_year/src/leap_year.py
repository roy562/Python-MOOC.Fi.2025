# Write your solution here
year = int(input("Please type in a year:"))

leapYear = True

if year%4 != 0:
    leapYear=False
else:
    if year%100 == 0 and year%400 != 0:
        leapYear=False
    
if leapYear:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")