'''
let color = '';
...
color = 'red'; -> let color = 'red';
# инициализировать лучше при объявлении

let arraySize -> const arraySize
# тут переменная нужна только для хранения размера

let array -> const arrayOfBooks
# массив не будет меняться, будет меняться его содержимое

def __init__(self, path):
    self.path = path
    self.mode = 'w'
# инициализация всех полей в конструкторе

fd.close() -> fd = null
# закончили работу с файлом

for (var i ...) -> for (let i ...)
# после блока for переменная i нам не нужна

connection.fetch();
connection = null;
# ресурсы под соединение больше не нужны

let price = 23.99;
...
price = -1;
# недопустимое значение для цены в конце работы с ней

console.assert(price > 0);
# добавляем в код инвариант на проверку цены

email = '}{[]';
# недопустимое значение для строки с email-ом

console.assert(!email.includes('[]'));
# добавляем в код инвариант на проверку email

counter = 0
while True:
    counter += 1
# счетчики должны быть рядом с циклом

acc = 0
while True:
    acc += counter * 2
    total = acc
# не забываем обнулять аккумулятор

let acc = 0;
for (let i = 0; ...)
# всегда инициализируем счетчик в заголовке цикла

console.assert(acc == 0);
# добавляем в код инвариант на аккумулятор

'''