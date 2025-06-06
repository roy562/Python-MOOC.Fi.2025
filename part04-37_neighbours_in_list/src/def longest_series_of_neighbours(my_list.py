def longest_series_of_neighbours(my_list: list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest

my_list = [1, 2, 5, 7, 6, 5, 9, 2, 3, 2, 1]
print(longest_series_of_neighbours(my_list))