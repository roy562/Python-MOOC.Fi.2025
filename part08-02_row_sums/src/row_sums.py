# Write your solution here
def row_sums(my_matrix: list):
    for row in my_matrix:
        new_col = 0
        for col in row:
            new_col+=col
            col+=1
        row.append(new_col)

def main():
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)

#main()