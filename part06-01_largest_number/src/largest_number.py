# write your solution here
def largest():
    largest = 0
    with open("numbers.txt") as my_file:
        for num in my_file:
            number = int(num)
            if number > largest:
                largest=number
    return largest

#print(largest())
