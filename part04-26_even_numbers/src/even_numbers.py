# Write your solution here
def even_numbers(ip_list):
    new_list = []
    for item in ip_list:
        if item%2 == 0:
            new_list.append(item)
    return new_list