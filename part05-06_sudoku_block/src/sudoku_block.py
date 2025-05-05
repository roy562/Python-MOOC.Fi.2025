# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    temp_list = []
    row_end = row_no+3
    col_end = column_no+3
    for i in range(row_no, row_end,1):
        #print(sudoku[i])
        for j in range(column_no, col_end, 1):
             check_num = sudoku[i][j]
             #print(check_num)
             
             if check_num >0 and check_num in temp_list:
                return False
             
             temp_list.append(check_num)
        
    return True

if __name__ == "__main__":
    sudoku = [
            [9, 0, 0, 0, 8, 0, 3, 0, 0],
            [2, 0, 0, 2, 5, 0, 7, 0, 0],
            [0, 2, 0, 3, 0, 0, 0, 0, 4],
            [2, 9, 4, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 7, 3, 0, 5, 6, 0],
            [7, 0, 5, 0, 6, 0, 4, 0, 0],
            [0, 0, 7, 8, 0, 3, 9, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 2]
            ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))