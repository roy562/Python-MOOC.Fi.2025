# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
total=0

negative = 0
positive = 0

while True:
    number = int(input("Number:"))

    if number == 0:
        break
    elif number <0:
        negative+=1
    else:
        positive+=1

    count+=1
    total+=number

print("... the program asks for numbers")
print("Numbers typed in", count)
print("The sum of the numbers is", total)
print("The mean of the numbers is", str(total/count))
print("Positive numbers", positive)
print("Negative numbers", negative)