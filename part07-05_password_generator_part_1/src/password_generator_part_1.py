# Write your solution here
def generate_password(size:int):
    from string import ascii_lowercase
    from random import sample

    return "".join(sample(ascii_lowercase,size))

def main():
    for i in range(10):
        print(generate_password(8))

#main()