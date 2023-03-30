import sys

import pygame

from alien import Alien
from bullet import Bullet
from stars import Star


def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        # Создание новой пули и включение ее в bullets
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def ultimate_1(game_settings, screen, ship, bullets):
    bullet_up = Bullet(game_settings, screen, ship, direction="up", bullet_width=3, bullet_height=15)
    bullet_right = Bullet(game_settings, screen, ship, direction="right", bullet_width=15, bullet_height=3)
    bullet_down = Bullet(game_settings, screen, ship, direction="down", bullet_width=3, bullet_height=15)
    bullet_left = Bullet(game_settings, screen, ship, direction="left", bullet_width=15, bullet_height=3)
    bullets.add(bullet_up, bullet_right, bullet_down, bullet_left)


def check_keydown_events(event, game_settings, screen, ship, bullets, bullets_ult):
    """Реагирует на нажатия клавиш"""
    if event.key == pygame.K_d:
        ship.moving_right = True
    if event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_w:
        ship.moving_top = True
    if event.key == pygame.K_s:
        ship.moving_bottom = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    if event.key == pygame.K_TAB:
        ultimate_1(game_settings, screen, ship, bullets_ult)
    elif event.key == pygame.K_g:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_w:
        ship.moving_top = False
    if event.key == pygame.K_s:
        ship.moving_bottom = False


def check_events(game_settings, screen, ship, bullets, bullets_ult):
    """Обраюатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets, bullets_ult)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, aliens, bullets, bullets_ult, stars):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets_ult.sprites():
        bullet.draw_bullet()
    ship.blitme()
    stars.draw(screen)
    aliens.draw(screen)
    pygame.display.flip()


def update_any_bullets(bullets, game_settings):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or bullet.rect.top >= game_settings.screen_height or bullet.rect.left >= game_settings.screen_width or bullet.rect.right <= 0:
            bullets.remove(bullet)


def get_number_aliens_col(game_settings, alien_width):
    """Находит число пришельцев в строке"""
    available_space_col = game_settings.screen_width - 2 * alien_width
    number_aliens_col = int(available_space_col / (2 * alien_width))
    return number_aliens_col


def create_alien(game_settings, screen, aliens, alien_number_col, row_number):
    """Создает пришельца"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number_col
    alien.rect.x = alien.x
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.y = alien.y
    aliens.add(alien)


def create_star(game_settings, screen, stars, col_number, row_number):
    star = Star(game_settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = star_width + 2 * star_width * col_number
    star.rect.x = star.x
    star.y = star_height + 2 * star_height * row_number
    star.rect.y = star.y
    stars.add(star)


def get_number_rows(game_settings, ship_height, alien_height):
    """Находит число пришельцев в столбце"""
    available_space_row = game_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_row / (2 * alien_height))
    return number_rows


def create_fleet(game_settings, screen, ship, aliens):
    """Создает флот пришельцов"""
    alien = Alien(game_settings, screen)

    number_aliens_col = get_number_aliens_col(game_settings, alien.rect.width)
    number_aliens_row = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_aliens_row):
        for alien_number in range(number_aliens_col):
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def create_sky_with_stars(game_settings, screen, stars):
    star = Star(game_settings, screen)
    number_col = int(game_settings.screen_width / (2 * star.rect.height))
    number_row = int(game_settings.screen_height / (2 * star.rect.height))
    for row in range(number_row):
        for col in range(number_col):
            create_star(game_settings, screen, stars, col, row)
