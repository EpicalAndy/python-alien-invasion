class GameStats():
    """ Отслежживание статистики игрока"""
    def __init__(self, alien_invasion_game):
        self.settings = alien_invasion_game.settings
        self.reset_stats()
        # Признак завершённости игры
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
