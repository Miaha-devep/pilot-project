import pygame


class Ship:

    def __init__(self, game_settings, screen):
        """Инициализирует корабль и его начальную позицию"""
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center_horizontal = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Обновляет позицию корабля"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_horizontal += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_horizontal -= self.game_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.center_vertical += self.game_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.center_vertical -= self.game_settings.ship_speed_factor

        self.rect.centerx = self.center_horizontal
        self.rect.centery = self.center_vertical

    def blitme(self):
        """Рисует корабль"""
        self.screen.blit(self.image, self.rect)
