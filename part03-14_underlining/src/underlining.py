# Write your solution here
input_string=""

while True:
    input_string = input("Please type in a string:")

    if len(input_string) == 0:
        break
    else:
        print(input_string)
        print("-"*len(input_string))