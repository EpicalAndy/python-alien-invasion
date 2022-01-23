import pygame
from pygame.sprite import Sprite

import settings


class Alien(Sprite):
    """ Класс пришельца """

    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen

        # Задаём изображение и rect
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()

        # Появление пришельца
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height

        # Сохранение горизонтальной позиции
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """ Проверка на дохожденик к краю """
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0


