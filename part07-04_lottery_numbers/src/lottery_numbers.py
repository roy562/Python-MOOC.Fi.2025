# Write your solution here

def lottery_numbers(amount: int, lower: int, upper: int):
    from random import sample
    
    return sorted(sample(range(lower, upper+1),amount))





def main():
    for number in lottery_numbers(7, 1, 40):
        print(number)

#main()