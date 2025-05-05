# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, another:"Money"):
        return (self.__euros*100+self.__cents) == (another.__euros*100+another.__cents)

    def __ne__(self, another:"Money"):
        return (self.__euros*100+self.__cents) != (another.__euros*100+another.__cents)
    
    def __gt__(self, another:"Money"):
        return (self.__euros*100+self.__cents) > (another.__euros*100+another.__cents)

    def __lt__(self, another:"Money"):
        return (self.__euros*100+self.__cents) < (another.__euros*100+another.__cents)

    def __add__(self, another:"Money"):
        total = (self.__euros*100+self.__cents) + (another.__euros*100+another.__cents)
        return Money(total//100, total%100)

    def __sub__(self, another:"Money"):
        money1 = self.__euros*100+self.__cents
        money2 = another.__euros*100+another.__cents
        if money1 < money2:
            raise ValueError("a negative result is not allowed")
        else:
            diff = money1 - money2
        
        return Money(diff//100, diff%100)


def main():
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two __euros and five __cents

    print(e1)
    print(e2)

def main2():
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)

def main3():
    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

def main4():
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    #e5 = e2-e1

#main()
#main2()
#main3()
#main4()