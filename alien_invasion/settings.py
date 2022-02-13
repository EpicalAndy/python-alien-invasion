class Settings():
    """ Класс для хранения настроек игры """
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (70, 130, 180)

        # Параметры корабля игрока
        self.ship_speed = 1
        self.ship_limit = 3

        # Параметры стрельбы
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.max_bullets_on_screen = 3

        # Параметры пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # 1 - движение направло; -1 - налево
        self.fleet_direction = 1

        # Темп игры
        self.speedup_scale = 1

        # Прирост стоимости уничтожения пришельцев
        self.score_scale = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_facrot = 1

        # fleet_direction = 1 - движение вправло, -1 влево
        self.fleet_direction = 1
        # Вес очков
        self.alien_point = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_facrot *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
