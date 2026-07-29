from gameparts import constants
import pygame


def draw_grid(screen):
    """Рисует сетку"""

    for y in range(0, 481, constants.GRID_SIZE):
        pygame.draw.line(
            screen, constants.GRID_COLOR, (0, y), (constants.SCREEN_WIDTH, y), 2
        )

    for x in range(0, 641, constants.GRID_SIZE):
        pygame.draw.line(
            screen, constants.GRID_COLOR, (x, 0), (x, constants.SCREEN_HEIGHT), 2
        )
