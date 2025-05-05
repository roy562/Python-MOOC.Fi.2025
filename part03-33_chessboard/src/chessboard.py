# Write your solution here
def chessboard(length):
    rows = 1
   
    while rows <= length:
        last_char = ""
        printed_row=""
        if rows%2 == 1:
            last_char = '1'
        else:
            last_char = '0'

        printed_row+= last_char
        cols = 2

        while cols <=length:
            if last_char == '1':
                last_char = '0'
            else:
                last_char='1'

            printed_row+=last_char
            cols+=1
        
        print(printed_row)
        rows+=1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
