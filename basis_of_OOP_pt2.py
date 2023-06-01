# 4 Задание

# Для генерирования 500 случайных объектов из задания 4.2 импортирует модуль random
import random

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

'''
Создаем массив из 500 объектов, где будут случайно 
перемешаны 500 объектов двух дочерних классов, 
и в цикле, не зная где какой объект, вызываем метод make_sound()
'''

animals = [Dog() if random.randint(0, 1) == 0 else Cat() for _ in range(500)]

# Вызываем для каждого объекта метод make_sound()

for animal in animals:
    animal.make_sound()

'''
Такой вывод получился, так как из-за полиморфизма каждый объект в массиве
ведет себя согласно своему типу Cat или Dog. При этом родительский метод
был переопределен, а Python автоматически выбирал объекты и выводил результат
переопределенного типа. Для Dog – 'Woof! Woof!', для Cat – 'Meow! Meow!'
'''

# Задание 4.3

# Пример работы ad hoc полиморфизма

# Наглядным примером ad hoc полиморфмизма может быть вычисление площади различных фигур

# Создаем класс Rectangle
class Rectangle:
    # Для вычисления площади прямоугольника нам нужны его ширина и длина
    def __init__(self, width, length):
        self._width = width
        self._length = length

    # Задаем метод вычисления площади
    def area(self):
        return self._width * self._length

# Далее создаем класс Circle
class Circle:
    # Для вычисления площади круга нужен радиус
    def __init__(self, radius):
        self._radius = radius

    # Задаем метод вычисления площади
    def area(self):
        return 3.14 * self._radius * self._radius

# Далее зададим общую функцию для расчета площади фигуры на плоскости
# Она будет принимать параметр shape, определять форму фигуры и вычислять площадь
def calculate_area(shape):
    return shape.area()

# Проверим работу ad hoc полиморфизма
rectangle = Rectangle(3, 4)
circle = Circle(4)

area_of_rectangle = calculate_area(rectangle)
print(area_of_rectangle)
area_of_circle = calculate_area(circle)
print(area_of_circle)





