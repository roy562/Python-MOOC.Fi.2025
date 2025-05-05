# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side:int):
        super().__init__(side, side)

    def __str__(self):
        return f"square {self.width}x{self.height}"


def main():
    rectangle = Rectangle(2, 3)
    print(rectangle)
    print("area:", rectangle.area())

    square = Square(4)
    print(square)
    print("area:", square.area())

#main()