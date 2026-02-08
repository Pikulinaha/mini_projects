class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self,ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        #Игра запускается в неактивном режиме
        self.game_active= False
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ship_left = self.settings.ship_limit
        self.score = 0