import pygame.font


class Button:
    def __init__(self, alien_invasion_game, message):
        """ Инициализация кнопки """
        self.screen = alien_invasion_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение свойств и размеров
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.test_color = (255, 255, 255)

        self.font = pygame.font.SysFont(None, 48)

        # Построение кнопки и выравнивание по центру
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_message(message)

    def _prep_message(self, message):
        """ Отрисовывет текст в прямоугольнике """
        self.msg_image = self.font.render(message, True, self.test_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


