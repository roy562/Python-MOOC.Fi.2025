# Write your solution here
while True:
    number = int(input("Please type in a number:"))

    if number <=0:
        break
    
    fact = 1
    i=number

    while i>0:
        fact*=i
        i-=1
    print(f"The factorial of the number {number} is {fact}")

print("Thanks and bye!")