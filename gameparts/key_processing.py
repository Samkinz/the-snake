import pygame

import gameparts.constants as constants


def handle_keys(event, game_object):
    """Управление змейкой стрелками клавиатуры"""
    if event.type == pygame.KEYDOWN:
        if (
            event.key == pygame.K_UP
            and game_object.direction != constants.DOWN
        ):
            game_object.next_direction = constants.UP
        elif (
            event.key == pygame.K_DOWN
            and game_object.direction != constants.UP
        ):
            game_object.next_direction = constants.DOWN
        elif (
            event.key == pygame.K_LEFT
            and game_object.direction != constants.RIGHT
        ):
            game_object.next_direction = constants.LEFT
        elif (
            event.key == pygame.K_RIGHT
            and game_object.direction != constants.LEFT
        ):
            game_object.next_direction = constants.RIGHT
