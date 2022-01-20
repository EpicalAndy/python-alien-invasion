import pygame

class Ship:
    """ Класс корабля игорька """
    def __init__(self, alien_invasion_instance):
        self.screen = alien_invasion_instance.screen
        self.screen_rect = alien_invasion_instance.screen.get_rect()
        self.settings = alien_invasion_instance.settings

        # Описание корабля
        self.image = pygame.image.load('images/hero.png')
        self.ship_rect = self.image.get_rect()

        # Корабль героя прикреплён к низу экрана
        self.ship_rect.midbottom = self.screen_rect.midbottom
        self.x = self.ship_rect.x
        # Флаги движения корабля
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Отрисовка корабля в текущей позиции
        self.screen.blit(self.image, self.ship_rect)

    def update_ship_position(self):
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.ship_rect.left > 0:
            self.x -= self.settings.ship_speed

        self.ship_rect.x = self.x

