# 1. Класс Car и класс Engine
# Ошибочное рассуждение:
#
# «У автомобиля есть двигатель → значит, автомобиль — это двигатель → можно унаследовать Car от Engine.»
#
# Правильное рассуждение:
#
# Автомобиль содержит двигатель, но не является им. Это композиция, а не наследование.

class Engine:
    ...

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

# 2. Класс Library и класс Book
# Ошибочное рассуждение:
#
# «Библиотека содержит книги → значит, библиотека — это книга.»
#
# Правильное рассуждение:
#
# Библиотека состоит из книг, но не является книгой. Это тоже композиция.

class Book:
    ...

class Library:
    def __init__(self, books: list[Book]):
        self.books = books