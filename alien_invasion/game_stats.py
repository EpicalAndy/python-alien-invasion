class GameStats():
    """ Отслежживание статистики игрока"""
    def __init__(self, alien_invasion_game):
        self.settings = alien_invasion_game.settings
        self.reset_stats()
        # Признак завершённости игры
        self.game_active = False
        self.score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0

