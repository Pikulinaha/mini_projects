import pygame.font
from  pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Класс для вывода игровой информации """

    def __init__(self,ai_game):
        """Инициализирует атрибуты для подсчета очков"""
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.prep_ships()


        #Настройка шрифта для вывода счета
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48 )
        #Подготовка исходного изображения
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):
        """Преобразовывает текущий счет в графическое изображение"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Вывод счета в правой части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счет на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Преобразует рекордный счет в график изображение"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True , self.text_color,self.settings.bg_color)

        #Выравнивание по центру
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Проверяет, появился ли новый рекорд."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
        self.prep_high_score()
    def prep_ships(self):
        """Сообщает сколько кораблей осталось у игрока"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
                ship= Ship(self.ai_game)
                ship.rect.x = 10 + ship_number * ship.rect.width
                ship.rect.y = 10
                self.ships.add(ship)
