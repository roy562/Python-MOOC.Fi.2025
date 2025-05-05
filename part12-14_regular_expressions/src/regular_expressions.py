# Write your solution here
import re

def is_dotw(my_string: str):
    return True if re.search('Mon|Tue|Wed|Thu|Fri|Sat|Sun', my_string) else False

def all_vowels(my_string: str):
    if re.search('[b-df-hj-np-tv-z]',my_string):
        return False
    else:
        return True

def time_of_day(my_string: str):
    if re.search('([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', my_string):
        return True
    else:
        return False

def test1():
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

#test1()

def test2():
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

#test2()

def test3():
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))

#test3()