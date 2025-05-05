# Write your solution here
def row_correct(sudoku: list, row_no: int):
    temp_list = []
    for number in sudoku[row_no]:
        if number >0 and number in temp_list:
                return False
        temp_list.append(number)
    return True

def column_correct(sudoku: list, column_no: int):
    temp_list = []
    for row in sudoku:
        col_num = row[column_no]
        
        if col_num >0 and col_num in temp_list:
                return False
        
        temp_list.append(col_num)
        
    return True

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

def sudoku_grid_correct(sudoku: list):
    for r in range(len(sudoku)):
        if not row_correct(sudoku, r):
            return False
        for c in range(len(sudoku[r])):
            if not column_correct(sudoku, c):
                return False
            if (r%3 == 0) and (c%3 == 0):
                if not block_correct(sudoku, r, c):
                    return False
    return True
    


if __name__ == "__main__":
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
        ]

    print(sudoku_grid_correct(sudoku2))
