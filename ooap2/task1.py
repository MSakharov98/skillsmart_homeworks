# Базовый класс для музыкальных инструментов
class MusicInstrument:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def play(self):
        # Базовый метод, который будет переопределен в дочерних классах
        return "Играет музыкальный инструмент"

    def get_info(self):
        return f"Инструмент: {self.brand}, Цена: {self.price} руб."


# Наследование: Guitar является (is-a) MusicInstrument
class Guitar(MusicInstrument):
    def __init__(self, brand, price, strings_count):
        # Вызов конструктора родительского класса
        super().__init__(brand, price)
        # Добавление специфичного для гитары атрибута
        self.strings_count = strings_count

    # Переопределение метода родительского класса - пример полиморфизма
    def play(self):
        return "Бренчание струн гитары"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Количество струн: {self.strings_count}"


# Еще один пример наследования: Piano является (is-a) MusicInstrument
class Piano(MusicInstrument):
    def __init__(self, brand, price, keys_count):
        super().__init__(brand, price)
        self.keys_count = keys_count

    # Еще одно переопределение метода - другая форма того же метода (полиморфизм)
    def play(self):
        return "Звук пианино"


# Класс, демонстрирующий композицию
class MusicStore:
    def __init__(self, name):
        self.name = name
        # Композиция: магазин содержит (has-a) список инструментов
        self.instruments = []

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    # Метод, демонстрирующий полиморфизм через использование одного интерфейса
    # для разных объектов в иерархии наследования
    def play_all_instruments(self):
        sounds = []
        for instrument in self.instruments:
            # Вызов метода play() будет обращаться к соответствующей реализации
            # в зависимости от конкретного типа инструмента - это полиморфизм
            sounds.append(instrument.play())
        return sounds


# Пример использования
if __name__ == "__main__":
    # Создание экземпляров разных классов
    guitar = Guitar("Fender", 25000, 6)
    piano = Piano("Yamaha", 150000, 88)

    # Создание магазина (композиция)
    store = MusicStore("Мелодия")
    store.add_instrument(guitar)
    store.add_instrument(piano)

    # Демонстрация полиморфизма
    print("Информация о гитаре:", guitar.get_info())
    print("Информация о пианино:", piano.get_info())

    # Полиморфное поведение - один интерфейс, разные реализации
    print("\nЗвуки всех инструментов в магазине:")
    for sound in store.play_all_instruments():
        print(sound)