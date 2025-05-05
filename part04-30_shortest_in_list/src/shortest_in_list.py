# Write your solution here
def shortest(ip_list):
    shortest_word = ""
    shortest_length= len(ip_list[0])
    for item in ip_list:
        if len(item) <= shortest_length:
            shortest_length = len(item)
            shortest_word = item
    return shortest_word