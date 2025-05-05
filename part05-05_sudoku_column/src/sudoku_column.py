# Write your solution here
def column_correct(sudoku: list, column_no: int):
    temp_list = []
    for row in sudoku:
        col_num = row[column_no]
        
        if col_num >0 and col_num in temp_list:
                return False
        
        temp_list.append(col_num)
        
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

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))