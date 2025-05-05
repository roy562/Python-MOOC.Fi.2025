# Write your solution here
def greatest_number(n1, n2, n3):
    greatest = 0
    if n1>=n2:
        greatest = n1
    else:
        greatest = n2

    if greatest<n3:
        greatest = n3
    
    return greatest

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(0, 0, 0)
    print(greatest)