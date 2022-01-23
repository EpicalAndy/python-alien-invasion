import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """ Корневой класс игры """

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update_ship_position()
            self.bullets.update()
            self._update_aliens()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _update_screen(self):
        """ Заливка экрана цветом """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Отрисовка последнего состояния экрана
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        self.remove_bullets()
        # Проверка попаданий по пришельцам. Bool параметры отвечают за удаления объектов
        # с экрана соответственно
        self._execute_alien_built_collisions()

    def _update_aliens(self):
        """ Лбновление позиций всех пришельцев """
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """ Создание флота """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        two_alien_width = 2 * alien_width
        available_space_x = self.settings.screen_width - two_alien_width
        number_aliens_x = available_space_x // two_alien_width
        # Определение количества рядов
        ship_height = self.ship.ship_rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - 2 * ship_height
        number_rows = available_space_y // (2 * alien_height)
        print(f'Ships params: {number_rows}')
        # Создание кораблей пришельцев
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        two_alien_width = 2 * alien_width
        alien.x = alien.rect.width + two_alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """ Реакция на достижения края экрана пришельцем """
        for alien in self.aliens:
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """ Опускает флот и меняет его направление """
        for alien in self.aliens:
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Создание нового снаряда с добавлением его в группу """
        if len(self.bullets) <= self.settings.max_bullets_on_screen:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _execute_alien_built_collisions(self):
        """ Обработка коллиций пуль и пришельцев """
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # Восстанавливает уничтоженный флот
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def remove_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
