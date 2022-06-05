# 16
import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __return_str__(self):
        return self.x, self.y


class Circle(Point):
    def __init__(self, x, y, radius, area) -> None:
        super().__init__(x, y)
        self.radius = radius
        self.area = 2 * math.pi * radius

    def __return_str__(self):
        pass


point = Point(1, 2)
print(point.__return_str__())
