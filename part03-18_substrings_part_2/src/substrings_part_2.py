# Write your solution here
# Write your solution here
input_string = input("Please type in a string:")

string_length = len(input_string)
counter=string_length-1

while counter >=0:
    print(input_string[counter:])
    counter-=1