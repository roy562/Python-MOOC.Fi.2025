# Write your solution here
def length_of_longest(ip_list):
    longest = 0
    for item in ip_list:
        if len(item) > longest:
            longest=len(item)
    return longest
