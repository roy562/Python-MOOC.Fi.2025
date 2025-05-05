# Write your solution here
def most_common_character(ip_string):
    largest_count = 0
    largest_char = ""

    for char in ip_string:
        if largest_count == 0 or ip_string.count(char) > largest_count:
            largest_count = ip_string.count(char)
            largest_char = char

    return largest_char
