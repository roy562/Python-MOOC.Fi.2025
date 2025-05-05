# Write your solution here:
class Item:
    def __init__(self, name:str, weight:float):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self, max_weight:int):
        self.__max_weight = max_weight
        self.__items = []
    
    def __get_suitcase_weight(self):
        return sum([item.weight() for item in self.__items])

    def __str__(self):
        total_items = len(self.__items)
        total_weight = self.__get_suitcase_weight()
        suitcase_str = f"{total_items} "
        if total_items == 1:
            suitcase_str+="item "
        else:
            suitcase_str+="items "

        suitcase_str+=f"({total_weight} kg)"
        return suitcase_str
    
    def add_item(self,item:"Item"):
        total_weight = self.__get_suitcase_weight()
        if total_weight+item.weight() <= self.__max_weight:
            self.__items.append(item)
    
    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return self.__get_suitcase_weight()
    
    def heaviest_item(self):
        heaviest = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest

class CargoHold:
    def __init__(self, cargo_max:int):
        self.__cargo_max = cargo_max
        self.__suitcases = []
    
    def __get_cargo_weight(self):
        return sum([suitcase.weight() for suitcase in self.__suitcases])

    def __str__(self):
        suitcases_count = len(self.__suitcases)
        cargo_weight = self.__get_cargo_weight()

        cargo_str = f"{suitcases_count} "
        if suitcases_count == 1:
            cargo_str+="suitcase"
        else:
            cargo_str+="suitcases"

        cargo_str+=f", space for {self.__cargo_max-cargo_weight} kg"
        return cargo_str
    
    def add_suitcase(self, suitcase:"Suitcase"):
        cargo_weight = self.__get_cargo_weight()
        if cargo_weight+suitcase.weight() <= self.__cargo_max:
            self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

def main1():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    print("Book:", book)
    print("Phone:", phone)

    book.weight = 10
    print("Book:", book)

def main2():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)

def main4():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")

def main5():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

def main6():
    cargo_hold = CargoHold(1000)
    print(cargo_hold)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)

def main7():
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()

#main4()
#main1()
#main2()
#main5()
#main6()
#main7()