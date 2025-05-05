# Write your solution here
def distinct_numbers(ip_list):
    new_list = []
    for item in ip_list:
        if item not in new_list:
            new_list.append(item)
    return sorted(new_list)