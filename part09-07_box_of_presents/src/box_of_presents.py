# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name:str, weight:float):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
        
class Box:
    def __init__(self):
        self.weight = 0
        self.presents = []
    
    def add_present(self, present:Present):
        self.presents.append(present)
        self.weight+= present.weight

    def total_weight(self):
        return self.weight

def main():
    book = Present("ABC Book", 2)

    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present:", book)

def main1():
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())

#main()
#main1()