# Write your solution here

def print_sudoku(sudoku: list):
    for r in range(len(sudoku)):
        for c in range(len(sudoku[r])):
            if sudoku[r][c] > 0:
                print(sudoku[r][c], end=" ")
            else:
                print("_", end=" ")

            if c in (2,5):
                print(" ", end="")
        print()
        if r in (2,5):
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = [item[:] for item in sudoku]
    new_list[row_no][column_no] = number
    return new_list

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)