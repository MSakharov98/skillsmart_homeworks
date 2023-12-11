'''
Задание 6

speed = s / int(input()) ->
    try speed = s / int(input()) except ZeroDivisionError ...
// проверяем деление на 0

volume / count -> volume // count
// для целых используем целочисленное деление

left + right -> Math.addExact(left, right);
// в Java можно проверять на переполнение

int a -> long a
// если вероятно переполнение, можно взять тип "шире", чтобы его избежать

(0.1 + 0.2) == 0.3 -> Math.abs((a-b)/b) < 0.00001
// Избегайте сравнений на равенство. Вариант справа лучше, но тоже не идеал.

(11000000.10 + 1.2) -> (1100000010 + 120) / 100
// арифметику можно выполнить через целочисленные значения

float mass -> double mass
// лучше использовать двойную точность

float currency -> BigDecimal currency
// для цен можно использовать тип понадежнее

status = "ok" -> status = STATUS_MESSAGE_OK
// убираем магические строки

color = "#f2df2d" -> BASE_COLOR = "#f2df2d"; color = BASE_COLOR;
// убираем магические строки

status = Localisation.getMessage('RU')
// Разработайте стратегию интернационализации/локализации текстовых сообщений

isLogined = User.getLogin() || User.getAccess(login, password)
if (isLogined && isMobile) ...
// улучшаем читабелность логическими переменными

'''