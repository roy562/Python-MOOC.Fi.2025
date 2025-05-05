# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week:int, correct_numbers:list):
        self.__week = week
        self.__correct_numbers = correct_numbers
    
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.__correct_numbers])

    def hits_in_place(self, numbers:list):
        return [number if number in self.__correct_numbers else -1 for number in numbers]


def main():
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))

#main()