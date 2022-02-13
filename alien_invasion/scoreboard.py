import pygame.font


class Scoreboard():
    """ Вывод игровой статистики """

    def __init__(self, alien_invasion_game):
        self.screen = alien_invasion_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = alien_invasion_game.settings
        self.stats = alien_invasion_game.stats
        self.score_image = None
        self.score_rect = None

        # Настройка шрифтов для вывода счёта
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Исходное изображение
        self.prepare_score()

    def prepare_score(self):
        """ Отрисовка счёта на экаран """
        rounded_score = round(self.stats.score, 0)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ Вывод счёта на экран """
        self.screen.blit(self.score_image, self.score_rect)
