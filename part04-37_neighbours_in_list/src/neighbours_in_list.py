# Write your solution here
def longest_series_of_neighbours(my_list):
    series_lengths = []
    count = 1

    for i in range(1,len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            count+=1
            if i == len(my_list)-1:
                series_lengths.append(count)
        else:
            series_lengths.append(count)
            count = 1
    print(series_lengths)
    return max(series_lengths)
