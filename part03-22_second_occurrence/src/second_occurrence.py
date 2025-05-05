# Write your solution here

input_string = input("Please type in a string:")
substring = input("Please type in a substring:")

first_index = input_string.find(substring)  #Find first occurence
second_index=0

if(first_index>=0):  #First occurence found
    second_index = first_index+len(substring)
    input_string = input_string[second_index:]
    second_occur = input_string.find(substring)
    if second_occur>=0:
       second_index+=second_occur
       print(f"The second occurrence of the substring is at index {second_index}.")
    else:
       print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")