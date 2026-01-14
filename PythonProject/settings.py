class Settings():
    """Класс для хранения настроек игры"""
    def __init__(self):
        """Инициализация настрек игры"""
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(50,50,100)

        #Настройка корабля
        self.ship_speed= 1.5

        #Параметры снаряда
        self.bullet_speed=1
        self.bullet_width=5
        self.bullet_height=20
        self.bullet_color=(60,60,60)

        #Ограничение выстрелов
        self.bullets_allowed=3