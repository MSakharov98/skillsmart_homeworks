# Пример иерархии:
# Класс Документ — базовый класс, содержащий метод подписать(пользователь).
# По умолчанию предусловие: любой зарегистрированный пользователь может подписывать.
# Постусловие: после подписания документ помечен как "подписан".
#
# Класс Контракт — подкласс Документа. Это юридически значимый документ.
# В нем переопределяется метод подписать, но с дополнительной проверкой:
# теперь только пользователи с ролью "юрист" могут подписывать.
#
# Почему нельзя усиливать предусловия:
# Если мы усилим предусловие (требовать "юрист" вместо "любой пользователь"), то:
#
# Код, который работает с объектами типа Документ, не ожидает таких ограничений.
#
# Он может передать обычного пользователя — это сработает с Документ, но сломается с Контрактом, нарушая принцип подстановки Лисков.
#
# Поведение станет менее общим, а значит — опасным для полиморфизма.
#
# Почему нельзя ослаблять постусловия:
# Предположим, что в Контракте метод подписать не помечает контракт как "подписан", а просто логирует действие.
#
# Код, который работает с Документами, может ожидать, что после вызова подписать() объект обязательно будет подписан.
#
# Если это не так — программа теряет корректность.
#
# Это нарушает контракт интерфейса, разрушающий согласованность поведения.
#
