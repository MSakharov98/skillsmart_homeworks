# Универсальный базовый класс
class Any(object):
    pass

# Класс General унаследован от Any
class General(Any):
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    # 1. Сравнение на равенство
    def __eq__(self, other):
        if not isinstance(other, General):
            return NotImplemented
        return self.name == other.name and self.value == other.value

    # 2. Хеширование (для использования в set и dict)
    def __hash__(self):
        return hash((self.name, self.value))

    # 3. Представление в виде строки
    def __str__(self):
        return f"General(name={self.name}, value={self.value})"

    # 4. Представление для отладки
    def __repr__(self):
        return f"General(name={self.name!r}, value={self.value!r})"

    # 5. Проверка на идентичность (используем стандарт is)
    def is_same_instance(self, other):
        return self is other

    # 6. Получение типа
    def get_type(self):
        return type(self)

    # 7. Клонирование (поверхностная копия)
    def clone(self):
        from copy import copy
        return copy(self)

a = General("test", 10)
b = General("test", 10)
c = a.clone()

print(a == b)             # True
print(hash(a))            # Хеш объекта
print(str(a))             # General(name=test, value=10)
print(repr(a))            # General(name='test', value=10)
print(a.is_same_instance(b))  # False
print(a.get_type())       # <class '__main__.General'>
print(c == a)             # True, clone равен
print(c is a)             # False, clone — новый объект
