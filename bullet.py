import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями"""

    def __init__(self, game_settings, screen, ship, direction='up', bullet_width=3, bullet_height=15):
        super().__init__()
        self.screen = screen
        self.direction = direction
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        # Создание пули в начале координат и назначение нужной позиции
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Перемещает пулю по экрану"""
        if self.direction == "up":
            self.y -= self.speed_factor
        if self.direction == "right":
            self.x += self.speed_factor
        if self.direction == "down":
            self.y += self.speed_factor
        if self.direction == "left":
            self.x -= self.speed_factor
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        """Выводит пулю на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
