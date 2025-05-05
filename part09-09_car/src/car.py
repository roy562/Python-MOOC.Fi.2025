# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odm = 0

    def __str__(self):
        return f"Car: odometer reading {self.__odm} km, petrol remaining {self.__petrol} litres"
    
    def fill_up(self):
        self.__petrol = 60
    
    def drive(self, km:int):
        self.__odm+= min(km, self.__petrol)
        self.__petrol-=min(km,self.__petrol)

def main():
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)

#main()