import sys
import pygame
from bullet import Bullet


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


def update_screen(settings, screen, ship, bullets, bullets_ult):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets_ult.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_bullets_ult(game_settings, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or bullet.rect.top >= game_settings.screen_height or bullet.rect.left >= game_settings.screen_width or bullet.rect.right <= 0:
            bullets.remove(bullet)
