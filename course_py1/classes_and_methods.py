# В задании решил создавать новые классы по мотивам серии игр Warhammer 40000

# Создадим класс Space Marine
# Герой будет атаковать, использовать способность и получать урон
class SpaceMarine:
    def __init__(self, name, chapter):
        self.name = name
        self.chapter = chapter # название легиона космодесантника
        self.health = 100
        self.power_armor = True
    
    # Создаем метод атаки
    def attack(self):
        print(f'{self.name} атакует врага с помощью своего оружия!')

    # Создаем метод применения способности
    def use_ability(self):
        print(f'{self.name} использует свою уникальную способность')

    # Создаем метод получения урона космодесантником
    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            print(f'{self.name} отправился к праотцам')
        else:
            print(f'{self.name} получил {damage} единиц урона')

# Создаем класс Weapon. Он отражает оружие космодесантника
# Оружие может стрелять, перезаряжаться и получать апгрейд
class Weapon:
    def __init__(self, mark, weapon_type, damage):
        self.mark = mark
        self.weapon_type = weapon_type
        self.damage = damage

    # Создаем метод для стрельбы
    def shoot(self):
        print(f'{self.mark} открывает огонь по врагам Императора!')
    
    def reload(self):
        print(f'{self.mark} перезаряжается перед следующим залпом')

    def upgrade(self):
        print(f'{self.mark} проходит апгрейд для повышения эффектиности боя')
        
# Создадим космического десантника как объект класса SpaceMarine
ultramarine = SpaceMarine('Марней Август Калгар', 'Ультрамарины')

# Использование методов класса SpaceMarine
ultramarine.attack()
ultramarine.use_ability()

#Создадим оружие Марнея Августа Калгара
bolter = Weapon('Тяжелый болтер', 'Штурмовое оружие', 50)
    
# Использование методов класса Weapon
bolter.shoot()
bolter.reload()
bolter.upgrade()

# Убиваем нашего магистра ордена Ультрамаринов
ultramarine.take_damage(120)


