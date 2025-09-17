# Родительский класс — общее поведение для всех животных
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} издает звук.")

# Класс Dog — расширяет функциональность
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # используем конструктор родителя
        self.breed = breed

    def bark(self):
        print(f"{self.name} лает: Гав-гав!")

# Класс Bird — специализирует поведение родителя
class Bird(Animal):
    def speak(self):  # переопределяем метод speak
        print(f"{self.name} поет: Чирик-чирик!")

# Примеры использования:

dog = Dog("Барсик", "Лабрадор")
dog.speak()  # поведение унаследовано от Animal
dog.bark()   # расширение — новый метод bark

bird = Bird("Кеша")
bird.speak()  # специализация — переопределили speak
