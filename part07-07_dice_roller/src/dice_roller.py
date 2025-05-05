# Write your solution here
from random import choice

def roll(die: str):
    choice_list = []
    if die == 'A':
        choice_list = [3, 3, 3, 3, 3, 6]
    elif die == 'B':
        choice_list = [2, 2, 2, 5, 5, 5]
    else:
        choice_list = [1, 4, 4, 4, 4, 4]

    return choice(choice_list)

def play(die1: str, die2: str, times: int):
    result_list = [0,0,0]
    for i in range(1, times+1):
        first_die = roll(die1)
        second_die = roll(die2)
        print(first_die, second_die)
        if first_die > second_die:
            result_list[0]+=1
        elif first_die < second_die:
            result_list[1]+=1
        else:
            result_list[2]+=1
    return result_list[0], result_list[1], result_list[2]

def main():
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()

    result = play("A", "C", 5)
    print(result)
    result = play("B", "B", 5)
    print(result)

#main()