# Write your solution here
def spruce(size):
    print("a spruce!")
    largest_row_size = (size*2)-1
    last_row_same_as_first = ""
    i=1
    while i<=size:
        no_of_stars = (i*2)-1
        no_of_spaces = int((largest_row_size-no_of_stars)/2)
        if i==1:
            last_row_same_as_first = " " * no_of_spaces+"*" * no_of_stars+" " * no_of_spaces
            print(last_row_same_as_first)
        else:
            print(" " * no_of_spaces+"*" * no_of_stars+" " * no_of_spaces)
        i+=1
    print(last_row_same_as_first)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(6)