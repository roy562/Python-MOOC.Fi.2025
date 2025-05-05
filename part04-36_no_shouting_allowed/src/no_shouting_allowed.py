# Write your solution here
def no_shouting(my_list):
    new_list = []

    for item in my_list:
        if item.isupper() == False:
            new_list.append(item)

    return new_list