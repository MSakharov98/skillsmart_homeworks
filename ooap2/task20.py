# 1. Наследование вариаций
# Подклассы реализуют один и тот же интерфейс, но по-разному. Используется, когда есть разные стратегии поведения.

class Payment:
    def pay(self, amount):
        raise NotImplementedError()

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using credit card.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in cash.")

def process_payment(p: Payment, amount: float):
    p.pay(amount)

process_payment(CardPayment(), 100)
process_payment(CashPayment(), 50)

 # Здесь CardPayment и CashPayment — вариации поведения одного и того же типа Payment.

# 2. Наследование с конкретизацией
# Подкласс расширяет поведение абстрактного класса, делая его конкретным. Абстрактный класс содержит частично реализованную логику.

class Report:
    def generate(self):
        data = self.get_data()
        print("Generating report with:", data)

    def get_data(self):
        raise NotImplementedError()

class SalesReport(Report):
    def get_data(self):
        return "sales data"

class InventoryReport(Report):
    def get_data(self):
        return "inventory data"

SalesReport().generate()
InventoryReport().generate()

# Здесь Report — шаблон поведения, а подклассы конкретизируют часть (данные).

# 3. Структурное наследование
# Подкласс наследует поля и методы для повторного использования кода, даже если не является логическим подтипом.

class Timestamped:
    def __init__(self):
        import datetime
        self.created_at = datetime.datetime.now()

    def get_timestamp(self):
        return self.created_at

class File(Timestamped):
    def __init__(self, name):
        super().__init__()
        self.name = name

f = File("document.txt")
print(f.name)
print(f.get_timestamp())