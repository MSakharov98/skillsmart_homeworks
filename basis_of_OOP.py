# В задании реализуем две несложные иерархии классов на основе окружающих предметов

# 1) Создаем класс Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand # марка 
        self.model = model # модель
        self.fuel = 0 # уровень топлива в баке

# Создадим метод запуска двигателя автомобиля
    def start_engine(self):
        print(f'The {self.brand} {self.model} engine is starting')
    
# Создадим метод дозаправки автомобиля
    def refuel(self, fuel_amount):
        self.fuel += fuel_amount
        print(f'Refueled the {self.brand} {self.model} with {fuel_amount} liters of fuel')
        
# Создадим метод управления автомобилем
    def drive(self):
        print(f'The {self.brand} {self.model} is driving')

# Создаем дочерний класс Car
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors # Количество дверей

# Добавим метод открывания дверей
    def open_doors(self):
        print(f'Opening {self.num_doors} doors of the {self.brand} {self.model}')

# Добавим метод воспроизведения музыки
    def play_music(self):
        print(f'Playing music in the {self.brand} {self.model}')

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
    def __init__(self, brand, model, num_gears):
        super().__init__(brand, model)
        self.num_gears = num_gears # количество передач

# Создадим метод езды на велосипеде
    def pedal(self):
        print(f'Pedaling the {self.brand} {self.model}')

# Создадим метод звонка для оповещения пешеходов
    def ring_bell(self):
        print(f'Ring the bell of the {self.brand} {self.model}')

# Создадим объект класса Bicycle
bicycle = Bicycle('Giant', 'Defy', 18)

# Начинаем движение на велосипеде "запускаем двигатель"
bicycle.start_engine()

# Едем, жмем на педали
bicycle.pedal()

# Оповещаем прохожих звонком о приближении
bicycle.ring_bell()

