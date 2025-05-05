# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls,my_list: list):
        max_freq_num = 0
        num_count = 0
        for num in my_list:
            if num == max_freq_num:
                continue
            else:
                if my_list.count(num) > num_count:
                    num_count = my_list.count(num)
                    max_freq_num = num
        return max_freq_num
    
    @classmethod
    def doubles(cls, my_list: list):
        result = []
        for num in my_list:
            if num in result:
                continue
            else:
                if my_list.count(num) >=2:
                    result.append(num)
        return len(result)

def main():
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

#main()