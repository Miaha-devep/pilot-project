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
    bullets = Group()
    bullets_ult = Group()
    ship = Ship(game_settings, screen)
    aliens = Group()
    stars = Group()
    game_functions.create_fleet(game_settings, screen, ship, aliens)
    game_functions.create_sky_with_stars(game_settings, screen, stars)
    """Отслеживание событий клавиатуры и мыши"""
    while True:
        game_functions.check_events(game_settings, screen, ship, bullets, bullets_ult)
        ship.update()
        bullets.update()
        bullets_ult.update()
        game_functions.update_any_bullets(bullets, game_settings)
        game_functions.update_any_bullets(bullets_ult, game_settings)
        game_functions.update_screen(game_settings, screen, ship, aliens, bullets, bullets_ult, stars)


run_game()
