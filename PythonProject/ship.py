import pygame

class Ship():
    """Класс для управления кораблем"""

    def __init__(self,ai_game):
        """Инициализация корабля и задает начал.позицию"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings

        #Загрузка изображения корабля и получает прямоугольник.
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края
        self.rect.midbottom=self.screen_rect.midbottom

        #Сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


        #Флаг перемещения
        self.moving_right=False
        self.moving_left = False
        self.moving_top= False
        self.moving_bottom=False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -= self.settings.ship_speed
        self.rect.x=self.x

        if self.moving_top and self.rect.top>0:
            self.y -= self.settings.ship_speed
        if self.moving_bottom and self.rect.bottom<self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y=self.y

    def blitme(self):
        """Рисует корабль в тек.позиции"""
        self.screen.blit(self.image, self.rect)