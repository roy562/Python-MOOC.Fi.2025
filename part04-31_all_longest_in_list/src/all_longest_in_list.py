# Write your solution here
def all_the_longest(my_list):
    new_list = []
    longest_length = 0

    for item in my_list:
        if len(item) >= longest_length:
            longest_length = len(item)

    for item in my_list:
        if len(item) == longest_length:
            new_list.append(item)
    
    return new_list