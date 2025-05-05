# Write your solution here
def hash_square(length):
    i=1
    while i<=length:
        j=1
        hash_string=""
        while j<=length:
            hash_string+="#"
            j+=1
        print(hash_string)
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)