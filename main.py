
# 5-m
class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        print("Shakl yuzasi aniqlanmagan")


class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def area(self):
        super().area()
        print("Yuza:", self.width * self.height)


r = Rectangle("To‘rtburchak", "Qizil", 5, 4)
r.area()

