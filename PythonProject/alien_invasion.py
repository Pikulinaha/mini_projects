import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализация игры и создание игровых ресурсов"""
        pygame.init()
        self.settings=Settings()

        self.screen = pygame.display.set_mode((1200,800))
        # self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width=self.screen.get_rect().width
        # self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        #Цвет фона
        self.bg_color=(50,50,100)

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()
            #Отображение событий клавиатуры и мыши
            pygame.display.flip()
            #Удаление старых снарядов
            for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))



    def _check_events(self):
        """Отслеживание событий клавиатуры и мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key ==pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение в группу Bullets"""
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullets=Bullet(self)
            self.bullets.add(new_bullets)



    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


if __name__ == "__main__":
    ai=AlienInvasion()
    ai.run_game()