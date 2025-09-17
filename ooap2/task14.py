class General:
    def __add__(self, other):
        raise NotImplementedError("Subclasses must implement addition")

    def __str__(self):
        return f"<General instance>"

class Number(General):
    def __init__(self, value: float):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

from typing import List, Optional, TypeVar, Generic

T = TypeVar('T', bound=General)

class Vector(General, Generic[T]):
    def __init__(self, elements: List[T]):
        self.elements = elements

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.elements) != len(other.elements):
            return None  # или можно вернуть специальный Void-класс

        result = []
        for a, b in zip(self.elements, other.elements):
            sum_value = a + b
            if sum_value is None:
                return None  # если одно из сложений не сработало
            result.append(sum_value)
        return Vector(result)

    def __str__(self):
        return "[" + ", ".join(str(e) for e in self.elements) + "]"

v1 = Vector([Number(1), Number(2), Number(3)])
v2 = Vector([Number(10), Number(20), Number(30)])
v3 = v1 + v2  # Vector([Number(11), Number(22), Number(33)])
print(v3)     # [11.0, 22.0, 33.0]

inner1 = Vector([Number(1), Number(2)])
inner2 = Vector([Number(10), Number(20)])
outer1 = Vector([inner1])
outer2 = Vector([inner2])
nested_sum = outer1 + outer2
print(nested_sum)  # [[11.0, 22.0]]

class Void(General):
    def __str__(self):
        return "Void"

# И использовать: return Void() вместо None
