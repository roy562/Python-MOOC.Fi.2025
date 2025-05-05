# Write your solution here
def read_input(prompt:str, lb:int, ub:int):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            number = -1
    
        if number >= lb and number <=ub:
            break
        else:
           print(f"You must type in an integer between {lb} and {ub}")

    return number

#number = read_input("Please type in a number: ", 5, 10)
#print("You typed in:", number)