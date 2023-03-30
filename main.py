import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group

game_settings = Settings()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(game_settings, screen)
    bullets = Group()
    bullets_ult = Group()

    """Отслеживание событий клавиатуры и мыши"""
    while True:
        game_functions.check_events(game_settings, screen, ship, bullets, bullets_ult)
        ship.update()
        bullets.update()
        bullets_ult.update()
        game_functions.update_bullets(bullets)
        game_functions.update_bullets_ult(game_settings, bullets_ult)
        game_functions.update_screen(game_settings, screen, ship, bullets, bullets_ult)
        print(len(bullets_ult))

run_game()
