import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def scale_area(self, total_area):
        """Scale the rectangle to have a given area while maintaining the fixed ratio."""
        fixed_ratio = self.width / self.height
        new_width = math.sqrt(total_area * fixed_ratio)
        new_height = total_area / new_width
        return new_width, new_height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total_area = self.get_square() + other.get_square()
            # Use a fixed ratio for the new rectangle
            new_width, new_height = self.scale_area(total_area)
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            total_area = self.get_square() * n
            # Use a fixed ratio for the new rectangle
            new_width, new_height = self.scale_area(total_area)
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, "Test1"
assert r2.get_square() == 18, "Test2"

r3 = r1 + r2
assert r3.get_square() == 26, "Test3"

r4 = r1 * 4
assert r4.get_square() == 32, "Test4"

assert Rectangle(3, 6) == Rectangle(2, 9), "Test5"
