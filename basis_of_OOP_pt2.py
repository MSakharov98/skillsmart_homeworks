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
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]

    # Реализуем метод начала движения
    def start(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.rotate()

    # Реализуем метод остановки
    def stop(self):
        self.engine.stop()
        for wheel in self.wheels:
            wheel.rotate()

# Проверим работу новой композиции
car = Vehicle()
car.start()
car.stop()

# б) Далее преобразуем класс Fruit



