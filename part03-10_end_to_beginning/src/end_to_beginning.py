# Write your solution here
input_string = input("Please type in a string:")

counter = len(input_string)

while counter > 0:
    print(input_string[counter-1])
    counter-=1

