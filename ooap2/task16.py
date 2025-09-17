# Полиморфный вызов метода

class Animal:
    def speak(self):
        print("Some animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def make_animal_speak(animal: Animal):
    # Полиморфный вызов: вызывается метод в зависимости от фактического типа объекта
    animal.speak()

make_animal_speak(Dog())  # Bark!
make_animal_speak(Cat())  # Meow!

# Ковариантный вызов метода

from typing import TypeVar, Generic

# Базовый класс
class Animal:
    def speak(self):
        return "Animal sound"

# Подкласс
class Dog(Animal):
    def speak(self):
        return "Bark!"

# Тип с ковариантностью
T_co = TypeVar('T_co', bound=Animal, covariant=True)

class AnimalProvider(Generic[T_co]):
    def get_animal(self) -> T_co:
        raise NotImplementedError()

class DogProvider(AnimalProvider[Dog]):
    def get_animal(self) -> Dog:
        return Dog()
