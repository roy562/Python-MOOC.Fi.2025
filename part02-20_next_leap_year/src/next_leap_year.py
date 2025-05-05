# Write your solution here

year = int(input("Year:"))
next_leap = year

while True:
    next_leap+=1
    leapYear = False

    if next_leap%100 ==0:
        if next_leap%400 == 0:
            leapYear = True
        else:
            leapYear = False
    elif next_leap%4 == 0:
        leapYear = True
    else:
        leapYear = False
    
    if leapYear:
        print(f"The next leap year after {year} is {next_leap}")
        break