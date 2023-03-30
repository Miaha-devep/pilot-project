class Settings:
    """Класс для сохранения всех настроек игры"""

    def __init__(self, screen_width=1200, screen_height=800, bg_color=(230, 230, 230), ship_speed_factor=1.25,
                 bullet_speed_factor=0.75, bullet_color=(60, 60, 60),
                 bullets_allowed=2):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_color = bg_color
        self.ship_speed_factor = ship_speed_factor

        self.bullet_speed_factor = bullet_speed_factor
        self.bullet_color = bullet_color
        self.bullets_allowed = bullets_allowed
