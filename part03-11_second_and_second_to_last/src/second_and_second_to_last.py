# Write your solution here
input_string = input("Please type in a string:")

#counter = len(input_string)

if input_string[1] == input_string[-2]:
    print("The second and the second to last characters are", input_string[1])
else:
    print("The second and the second to last characters are different")