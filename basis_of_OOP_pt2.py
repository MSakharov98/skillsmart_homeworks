# 4 Задание

# 4.1 Реализация композиции для кода классов из урока № 4

# a) Для начала преобразуем класс Vehicle

# Создадим класс Engine для управления двигателем

class Engine:
    def start(self):
        print('Engine started')

    def stop(self):
        print('Engine stopped')

# Далее создадим класс Wheel для управления колесами

class Wheel:
    def rotate(self):
        print('Wheel is rotating')

# Преобразуем класс Vehicle

class Vehicle:
    # Добавим машине двигатель и четыре колеса

    def __init__(self):
        self._engine = Engine()
        self._wheels = [Wheel() for _ in range(4)]

    # Реализуем метод начала движения

    def start(self):
        self._engine.start()
        for wheel in self._wheels:
            wheel.rotate()

    # Реализуем метод остановки

    def stop(self):
        self._engine.stop()
        for wheel in self._wheels:
            wheel.rotate()

# Проверим работу новой композиции

car = Vehicle()
car.start()
print('\n')
car.stop()
print('\n')

# б) Далее преобразуем класс Fruit

class Fruit:
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def peel(self):
        print(f'Peeling the {self._color} {self._name}')

    def eat(self):
        print(f'Eating the {self._color} {self._name}')

# Фрукты можно положить в корзину

class Basket:
    def __init__(self):
        self._fruits = []

    # Складываем фрукты в корзину
    def add_fruit(self, fruit):
        self._fruits.append(fruit)

    # Съедаем все фрукты
    def eat_all(self):
        for fruit in self._fruits:
            fruit.peel()
            fruit.eat()
            print('\n')

# Тестируем композицию Fruit

apple = Fruit('Apple', 'Red')
apple2 = Fruit('Apple', 'Green')

# Создадим экземпляр класса Basket

basket = Basket()

# Добавляем туда наши фрукты

basket.add_fruit(apple)
basket.add_fruit(apple2)

# И все съедаем

basket.eat_all()

# 4.2 Переопределение методов в иерархии родительского класса и двух дочерних

# Создадим класс Animal

class Animal:

    # Пускай звери издают звуки
    def make_sound(self):
        print('Animal makes its sound!')

# Далее создадим дочерний класс Dog

class Dog(Animal):

    # Собака гавкает
    def make_sound(self):
        print('Woof! Woof!')

# Создадим еще один дочерний класс Cat

class Cat(Animal):
    # Кот мяукает
    def make_sound(self):
        print('Meow! Meow!')

# Продемонстрируем работы классов
animal = Animal()
animal.make_sound()

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()






