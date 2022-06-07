import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Center: ({self.x}, {self.y})"


class Circle(Point):
    def __init__(self, radius, x, y) -> None:
        super().__init__(x, y)
        self.radius = radius
        self.area = self.circle_area()

    def circle_area(self):
        return math.pi * self.radius * self.radius

    def __str__(self) -> str:
        return f"{super().__str__()}, Radius: {self.radius}"


class Cylinder(Circle):
    def __init__(self, height, radius, x, y) -> None:
        super().__init__(radius, x, y)
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius * self.radius

    def volume(self):
        return self.circle_area() * self.height

    def __str__(self) -> str:
        return f"{super().__str__()}, Surface Area: {self.surface_area()}, Volume: {self.volume()}"


c = Circle(10, 5, 10)
print(c.circle_area())
print(c.__str__())

cy = Cylinder(100, 50, 10, 50)
print(cy.surface_area())
print(cy.volume())
print(cy.__str__())

