# Write your solution here
input_string = input("Please type in a string:")

string_length = len(input_string)
counter=1

while counter <= string_length:
    print(input_string[:counter])
    counter+=1