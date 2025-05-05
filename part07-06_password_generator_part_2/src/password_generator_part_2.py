# Write your solution here
from string import ascii_lowercase, digits
from random import sample, choice, shuffle, randint

# Write your solution here
def generate_strong_password(size:int, numbers:bool, special:bool):
    special_pool = '!?=+-()#'
    all_pool = ascii_lowercase+digits+special_pool
    strong_password = []

    if numbers == True and special == True:
        strong_password = sample(all_pool,size-3)
        strong_password.append(choice(digits))
        strong_password.append(choice(special_pool))
        strong_password.append(choice(ascii_lowercase))
    elif numbers == True:
        strong_password = sample(ascii_lowercase+digits,size-2)
        strong_password.append(choice(digits))
        strong_password.append(choice(ascii_lowercase))
    elif special == True:
        strong_password = sample(ascii_lowercase+special_pool,size-2)
        strong_password.append(choice(special_pool))
        strong_password.append(choice(ascii_lowercase))
    else:
        strong_password = sample(ascii_lowercase, size)
    
    
    return "".join(strong_password)

def main():
    for i in range(10):
        print(generate_strong_password(8, True, True))

#main()