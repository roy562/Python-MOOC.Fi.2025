# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day:int, month:int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year 

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def __totaldays(self):
        return (self.__year*360+self.__month*30+self.__day)
    
    def __daysToSimpleDate(self, days:int):
        #newDate = SimpleDate(0,0,0)
        year = days//360
        month = (days - year*360)//30
        day = days - year*360 - month*30
        return SimpleDate(day,month,year)

    def __eq__(self, other:"SimpleDate"):
        return self.__totaldays() == other.__totaldays()

    def __ne__(self, other:"SimpleDate"):
        return self.__totaldays() != other.__totaldays()

    def __lt__(self, other:"SimpleDate"):
       return self.__totaldays() < other.__totaldays()

    def __gt__(self, other:"SimpleDate"):
        return self.__totaldays() > other.__totaldays()
        
    def __add__(self, days_to_add:int):
        days = self.__totaldays()+days_to_add
        return self.__daysToSimpleDate(days)

    def __sub__(self, other:"SimpleDate"):
        return abs(self.__totaldays() - other.__totaldays())


def main1():
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)

def main2():
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)

def main3():
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)

#main1()
#main2()
#main3()