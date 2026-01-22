class Settings():
    """Класс для хранения настроек игры"""
    def __init__(self):
        """Инициализация настрек игры"""
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(50,50,100)

        #Настройка корабля
        self.ship_speed= 3
        self.ship_limit = 3

        #Параметры снаряда
        self.bullet_speed=2.5
        self.bullet_width=10
        self.bullet_height=20
        self.bullet_color=(60,60,60)

        #Ограничение выстрелов
        self.bullets_allowed=3

        #Настройка пришельцев
        self.alien_speed=2
        self.fleet_drop_speed = 10
        #fleet_direction = 1 движение вправо a -1 - влево
        self.fleet_direction = 1