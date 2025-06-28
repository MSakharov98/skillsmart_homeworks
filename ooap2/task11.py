# Универсальный базовый класс
class Any:
    def describe(self):
        return "This is Any"

# General расширяет Any
class General(Any):
    def describe(self):
        return "This is General"

# Дополнительный базовый класс
class Printable:
    def print_info(self):
        print("I can be printed.")

# Класс None наследует сразу от General и Printable
class NoneType(General, Printable):
    def describe(self):
        return "This is None (bottom of hierarchy)"

# Полиморфная функция, принимающая любой объект-наследник Any
def process_entity(entity: Any):
    print("Description:", entity.describe())
    if isinstance(entity, Printable):
        entity.print_info()
