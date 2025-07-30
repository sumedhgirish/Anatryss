from decimal import DivisionByZero
from typing import override, Self
import math

class Vector2:
    def __init__(self, x :float, y :float) -> None:
        self.x :float = x
        self.y :float = y

    @override
    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"

    @override
    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other :Self):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other :Self):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other :float):
        return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other :float):
        return self * other

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def as_tuple(self):
        return (self.x, self.y)

class Vector3:
    def __init__(self, x :float, y :float, z :float) -> None:
        self.x :float = x
        self.y :float = y
        self.z :float = z

