# Задание 1.1

'''
1) В работе медиааналитика использую сервисы под названием "Медиалогия" и "Brand Analytics". 
Суть данных программ заключается в анализе постов, брендов и личностей в социальных сетях, а также различных параметров.
В качестве класса, предположительно, разработчики могут использовать публикацию в соцмедиа. 
'''

class Post_in_VKontakte():
    likes = 0 #количество лайков
    reposts = 0 # количество репостов
    comments = 0 #количество комментариев
    audience = 0 #аудитория поста
    er = 0 #уровень вовлеченности поста

# Далее мы сможем задать публикацию как объект и внести его данные
post_about_roads = Post_in_VKontakte()
post_about_roads.likes = 155
post_about_roads.reposts = 23
post_about_roads.comments = 12
post_about_roads.audience = 1457

# И с помощью этих данных мы можем рассчитать уровень вовлеченности поста
post_about_roads.er = (post_about_roads.likes + post_about_roads.reposts 
      + post_about_roads.comments) / post_about_roads.audience * 100

'''
2) Еще один пример программы, которые использую ежедневно – FatSecret. 
В силу активных занятий спортом нужно следить за рационом питания и записывать съеденное,
так можно понять, сколько употребляю белков, жиров и углеводов. Пример класса – блюдо 
со своими питательными характеристиками.
'''

class dish():
    proteins = 0
    fats = 0 
    carbohydrates = 0
    calories = 0

# Объектом будет компонент блюда - котлета.
cutlet = dish()

# Задаем объекту - котлете питательные характеристики.
cutlet.proteins = 12
cutlet.fats = 20
cutlet.carbohydrates = 25
cutlet.calories = 123

# Задание 1.2

'''
Для выполнения задания выбрал классы, связанные с устройством компьютера
и его техническими характеристиками, а также устройствами ввода и вывода
'''

# Характеристики компьютера
class Computer():
    model = 'MacBook Pro'
    processor = 'M1 Pro'
    memory = 0
    storage = 0
    graphics = 14
    operating_system = 'MacOS'
    price = 0

#Пусть даже используется ноутбук, к нему можно подключить монитор
class Monitor():
    size = 0
    panel_type = 'IPS'
    resolution = '1920x1080'
    refresh_rate = 144
    inputs = ['HDMI', 'USB-C']
    price = 0

# Для удобства и повышения скорости печати подключим клавиатуру
class Keyboard():
    keyboard_type = 'mechanical'
    layout = 'RU'
    backlighting = True
    macros = ['Macro-1', 'Macro-2']
    interface = 'USB'
    multimedia_keys = True
    price = 0

# Создадим объект mac_book_pro_16 класса Computer()
mac_book_pro_16 = Computer()
mac_book_pro_16.memory = 16
mac_book_pro_16.graphics = 14
mac_book_pro_16.storage = 512
mac_book_pro_16.price = 175000
print(mac_book_pro_16)

# Создадим объект msi класса Monitor()
msi = Monitor()
msi.refresh_rate = 144
msi.size = 21
msi.price = 15000
print(msi)

# Создадим объект keychron класса Keyboard()
keychron = Keyboard()
keychron.price = 12000
keychron.backlighting = True
keychron.interface = ['USB', 'USB-C']
keychron.macros = 'Macro-1'
print(keychron)







