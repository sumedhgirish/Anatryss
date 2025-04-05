from typing import override, Self

class Vector2:
    def __init__(self, x :float, y :float):
        self.x :float = x
        self.y :float = y

    @override
    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"

    def __add__(self, other :Self):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other :Self):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other :float):
        return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other :float):
        return self * other

class Vector3:
    def __init__(self, x :float, y :float, z :float):
        self.x :float = x
        self.y :float = y
        self.z :float = z

