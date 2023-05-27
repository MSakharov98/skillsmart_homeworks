# В задании реализуем две несложные иерархии классов на основе окружающих предметов
# Сделаем все поля классов приватными, но так, чтобы они при этом еще и наследовались. 
# Используем одинарное нижнее подчеркивание _*

# 1) Создаем класс Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand # марка 
        self._model = model # модель
        self._fuel = 0 # уровень топлива в баке

# Создадим метод запуска двигателя автомобиля
    def start_engine(self):
        print(f'The {self._brand} {self._model} engine is starting')
    
# Создадим метод дозаправки автомобиля
    def refuel(self, fuel_amount):
        self._fuel += fuel_amount
        print(f'Refueled the {self._brand} {self._model} with {fuel_amount} liters of fuel')
        
# Создадим метод управления автомобилем
    def drive(self):
        print(f'The {self._brand} {self._model} is driving')

# Создаем дочерний класс Car
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self._num_doors = num_doors # Количество дверей

# Добавим метод открывания дверей
    def open_doors(self):
        print(f'Opening {self._num_doors} doors of the {self._brand} {self._model}')

# Добавим метод воспроизведения музыки
    def play_music(self):
        print(f'Playing music in the {self._brand} {self._model}')

# Пример работы методов класса Car

# Создаем объект car класса Car
car = Car('Toyota', 'Camry', 4)

# Включаем двигатель 
car.start_engine()

# Дозаправка
car.refuel(50)

# Открываем двери в машине
car.open_doors()

# Ведем машину
car.drive()

# Создадим еще один дочерний класс Bicycle
class Bicycle(Vehicle):
    def __init__(self, _brand, _model, num_gears):
        super().__init__(_brand, _model)
        self._num_gears = num_gears # количество передач

# Создадим метод езды на велосипеде
    def pedal(self):
        print(f'Pedaling the {self._brand} {self._model}')

# Создадим метод звонка для оповещения пешеходов
    def ring_bell(self):
        print(f'Ring the bell of the {self._brand} {self._model}')

# Создадим объект класса Bicycle
bicycle = Bicycle('Giant', 'Defy', 18)

# Начинаем движение на велосипеде "запускаем двигатель"
bicycle.start_engine()

# Едем, жмем на педали
bicycle.pedal()

# Оповещаем прохожих звонком о приближении
bicycle.ring_bell()

# Создадим класс Fruit
# Фрукты можно будет почистить и съесть
class Fruit:
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def peel(self):
        print(f'Peeling the {self._color} {self._name}')
    
    def eat(self):
        print(f'Eating the {self._color} {self._name}')

# Создадим дочерний класс Apple
# Яблоко можно будет запечь или сделать из него сидр
class Apple(Fruit):
    def __init__(self, _name, _color, variety):
        super().__init__(_name, _color)
        self._variety = variety # название сорта яблок
    
    def bake(self):
        print(f'Baking an {self._color} {self._variety}')
    
    def make_cider(self):
        print(f'Making cider from {self._variety} apples')
        
    
