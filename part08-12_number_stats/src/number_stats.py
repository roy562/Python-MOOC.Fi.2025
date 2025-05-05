# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.numbers+=1
        self.sum+=number

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        return self.sum
    
    def average(self):
        if self.numbers == 0:
            return 0
        return self.sum/self.numbers

def main():
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())

def main2():
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())

def main3():
    stats = NumberStats()

    print("Please type in integer numbers:")
    while True:
        int_number = int(input())

        if int_number == -1:
            break

        stats.add_number(int_number)
    
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())

def main4():
    all_stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()
    
    print("Please type in integer numbers:")
    while True:
        int_number = int(input())

        if int_number == -1:
            break

        all_stats.add_number(int_number)

        if int_number%2 == 0:
            even_stats.add_number(int_number)
        else:
            odd_stats.add_number(int_number)
    
    print("Sum of numbers:", all_stats.get_sum())
    print("Mean of numbers:", all_stats.average())
    print("Sum of even numbers:", even_stats.get_sum())
    print("Sum of odd numbers:", odd_stats.get_sum())



#main()
#main2()
#main3()
main4()