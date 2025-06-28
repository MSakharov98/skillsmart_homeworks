# 1. Полное скрытие (name mangling / псевдо-private)

class Base:
    def __real_method(self):
        print("Base.__real_method")

    def access_private(self):
        self.__real_method()  # работает внутри класса

b = Base()
b.access_private()
# b.__real_method()  # AttributeError
# но можно добраться так: b._Base__real_method()  # не рекомендуется

# 2. Частичное скрытие (protected по соглашению)
class Base:
    def _semi_private_method(self):
        print("Base._semi_private_method")

class Child(Base):
    def use_parent_method(self):
        self._semi_private_method()  # ✅ по соглашению допускается

Child().use_parent_method()
_method() — это соглашение, означающее: "не трогай снаружи, если ты не потомок".

# 3. Скрытие через перекрытие (overriding)

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # перекрывает метод родителя
        print("Hello from Child")

obj = Child()
obj.greet()  # Hello from Child

# 4. Скрытие через делегирование/обёртку (composition)

class Core:
    def secret_logic(self):
        print("Doing something internal")

class Wrapper:
    def __init__(self):
        self._core = Core()  # спрятали Core внутрь

    def exposed_method(self):
        print("Wrapper calls core method:")
        self._core.secret_logic()

w = Wrapper()
w.exposed_method()
# w._core.secret_logic()  # можно, но считается скрытым доступом