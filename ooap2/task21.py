# 1. Наследование реализации
# Подкласс просто использует уже реализованное поведение родителя как есть, без переопределения.

class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class Service(Logger):  # Наследуем реализацию log()
    def run(self):
        self.log("Service started")

s = Service()
s.run()

# Здесь класс Service наследует реализацию метода log() от Logger и использует его без изменений.

# 2. Льготное наследование
# Подкласс получает привилегированный доступ к защищённым членам (_protected) родительского класса, которые не предназначены для внешнего использования.

class Counter:
    def __init__(self):
        self._count = 0  # защищённое поле

    def _increment(self):  # защищённый метод
        self._count += 1

class PrivilegedCounter(Counter):  # Льготный доступ
    def count_three_times(self):
        self._increment()
        self._increment()
        self._increment()
        return self._count

pc = PrivilegedCounter()
print(pc.count_three_times())  # 3