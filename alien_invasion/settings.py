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

