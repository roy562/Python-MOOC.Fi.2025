# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers:list):
    if len(numbers)%5 != 0 :
        numbers.append(numbers[-1]+1)
        add_numbers_to_list(numbers)

def test():
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)

#test()