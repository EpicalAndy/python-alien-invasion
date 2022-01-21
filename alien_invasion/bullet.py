import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, alien_invasion_instance):
        """ Класс управления стрельбой """
        super().__init__()

        self.screen = alien_invasion_instance.screen
        self.settings = alien_invasion_instance.settings
        self.color = self.settings.bullet_color

        # Создание снаряда
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                       self.settings.bullet_height)
        self.bullet_rect.midtop = alien_invasion_instance.ship.ship_rect.midtop

        # Позиция снаряда
        self.y = float(self.bullet_rect.y)

    def update(self):
        """ Перемещение снаряда """
        self.y -= self.settings.bullet_speed
        self.bullet_rect.y = self.y

    def draw_bullet(self):
        """ Отрисовка снаряда """
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)

