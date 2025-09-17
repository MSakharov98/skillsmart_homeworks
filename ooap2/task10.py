from typing import final

class Base:
    @final
    def important_method(self):
        print("This method is final and cannot be overridden.")

class Derived(Base):
    # Попытка переопределить вызовет предупреждение в IDE или статическом анализаторе
    # но не ошибку во время выполнения!
    def important_method(self):  # ⚠ Это нарушение правила @final
        print("Overridden in Derived")  # ← IDE (например, PyCharm, mypy) покажет ошибку
