class Settings():
    """Класс для хранения настроек игры"""
    def __init__(self):
        """Инициализация статистических настроек игры"""
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(50,50,100)

        #Настройка корабля
        self.ship_speed= 3
        self.ship_limit = 3

        #Параметры снаряда
        self.bullet_speed=2.5
        self.bullet_width=100
        self.bullet_height=200
        self.bullet_color=(60,60,60)

        #Ограничение выстрелов
        self.bullets_allowed=3

        #Настройка пришельцев
        self.alien_speed=2
        self.fleet_drop_speed = 10
        #fleet_direction = 1 движение вправо a -1 - влево
        self.fleet_direction = 1

        #Темп ускорения
        self.speedup_scale=1.1
        #Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        #fleet_direction 1 вправо -1 влево
        self.fleet_direction = 1

        #Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)