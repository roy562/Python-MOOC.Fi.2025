# write your solution here
def read_input_file():
    file_matrix = []
    with open("matrix.txt") as ip_file:
        for line in ip_file:
            temp_list = []
            line = line.replace("\n","")
            numbers = line.split(",")
            for num in numbers:
                temp_list.append(int(num))
            file_matrix.append(temp_list)
    return file_matrix

def row_sum_max(ip_row:list):
    row_sum = 0
    row_max = 0
    for num in ip_row:
        row_sum+=num
        if num > row_max:
            row_max = num
    return row_sum, row_max

def matrix_sum():
    file_sum = 0
    input_file_matrix = read_input_file()
    for row in input_file_matrix:
        r_sum, r_max = row_sum_max(row)
        file_sum+=r_sum
    
    return file_sum

def matrix_max():
    file_max = 0
    input_file_matrix = read_input_file()
    for row in input_file_matrix:
        r_sum, r_max = row_sum_max(row)
        if r_max > file_max:
            file_max = r_max

    return file_max

def row_sums():
    row_sums = []
    input_file_matrix = read_input_file()
    for row in input_file_matrix:
        r_sum, r_max = row_sum_max(row)
        row_sums.append(r_sum)
    return row_sums

#print(row_sums())