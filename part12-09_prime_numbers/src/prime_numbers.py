# Write your solution here
def get_next_prime_number(x:int):
    
    while True:
        prime_found=True
        for i in range(2, x):
            if x%i == 0:
                prime_found = False

        if prime_found == False:
            x+=1
        else:
            break
    return x    
        



def prime_numbers():
    x = 2
    
    while True:
        yield x
        x = get_next_prime_number(x+1)
        #print("Next prime number is: ", x)

def test():
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))

#test()