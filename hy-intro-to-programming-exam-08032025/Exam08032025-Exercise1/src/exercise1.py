#Function to take user input
def get_user_input():
    user_numbers = []
    while True:
        #User Inputs a number
        user_number = int(input("Type in a number: "))

        #If user input is 0, break the loop
        if user_number == 0:
            break
        else:
        #Add number to a list
            user_numbers.append(user_number)

    return user_numbers
    
#Function to find most repeated item from the input list
def most_repeated(numbers:list):
    #Define two local variable with first items from list as value
    repeated_item = numbers[0]
    repeated_count = numbers.count(numbers[0])

    #Loop over the list to find most repeated item
    for num in numbers:
        if repeated_item == num:
                continue
        current_num_count = numbers.count(num)
        if current_num_count > repeated_count:
             repeated_count = current_num_count
             repeated_item = num
    
    return repeated_item

user_numbers = get_user_input()

print(f"Biggest: {max(user_numbers)}")
print(f"Smallest: {min(user_numbers)}")
print(f"Number of numbers: {len(user_numbers)}")
print(f"Sum: {sum(user_numbers)}")
print(f"Most repeated: {most_repeated(user_numbers)}")