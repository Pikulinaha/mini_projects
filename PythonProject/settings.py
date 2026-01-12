class Settings():
    """Класс для хранения настроек игры"""
    def __init__(self):
        """Инициализация настрек игры"""
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(50,50,100)

        #Настройка корабля
        self.ship_speed= 1.5