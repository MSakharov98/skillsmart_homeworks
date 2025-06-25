# Определения

# Ковариантность (covariance)** — это когда подтипы можно **использовать вместо** родительских типов.
# Контравариантность (contravariance)** — это когда родительские типы можно использовать **вместо подтипов**.

# Применяется к обобщённым типам (`Generic[T]`) — например, спискам, функциям, контейнерам.

# Примеры в Python с `typing`

from typing import TypeVar, Generic, List, Callable

# Базовые классы
class Animal:
    def speak(self):
        print("Some animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

# ----- КОВАРИАНТНОСТЬ -----

# T_co — ковариантный тип-параметр
T_co = TypeVar('T_co', covariant=True)

class ReadOnlyBox(Generic[T_co]):
    def __init__(self, value: T_co):
        self._value = value

    def get(self) -> T_co:
        return self._value

# Ковариантность позволяет: ReadOnlyBox[Dog] -> ReadOnlyBox[Animal]
dog_box = ReadOnlyBox(Dog())
animal_box: ReadOnlyBox[Animal] = dog_box  # OK, Dog -> Animal

# Контрвариантность

# T_contra — контравариантный тип-параметр
T_contra = TypeVar('T_contra', contravariant=True)

class Writer(Generic[T_contra]):
    def write(self, value: T_contra):
        print(f"Writing: {value}")

# Контравариантность позволяет: Writer[Animal] -> Writer[Dog]
animal_writer: Writer[Animal] = Writer()
dog_writer: Writer[Dog] = animal_writer  # OK, Animal <- Dog
```

---

## 🔍 Краткое объяснение

#| Параметр               | Пример                                     | Допустимо, если:        |
#| ---------------------- | ------------------------------------------ | ----------------------- |
#| Ковариантность         | `ReadOnlyBox[Dog]` → `ReadOnlyBox[Animal]` | Подтип вместо родителя  |
#| Контравариантность     | `Writer[Animal]` → `Writer[Dog]`           | Родитель вместо подтипа |
