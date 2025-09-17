# Базовый класс Any
class Any:
    def assign(self, other):
        # По умолчанию запрещаем присваивание
        if not isinstance(other, self.__class__):
            raise TypeError(f"Cannot assign: {type(other).__name__} is not {self.__class__.__name__}")
        # Заглушка для переопределения
        raise NotImplementedError("Assign not implemented in base class")

# Класс General, унаследованный от Any
class General(Any):
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def assign(self, other):
        # Проверим тип через базовый метод
        super().assign(other)
        # Выполним копирование состояния
        self.name = other.name
        self.value = other.value
