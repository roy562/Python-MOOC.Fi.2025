# Write your solution here
input_string = input("Please type in a word:")
substring = input("Please type in a character:")

index = input_string.find(substring)
#print(index)

if index >= 0 and (len(input_string) - index) >=3:
    print(input_string[index:index+3])
