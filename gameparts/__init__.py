"""Пакет игровых компонентов для игры «Змейка».

Содержит классы игровых объектов, игровые константы,
логику игры, обработку управления и работу с результатами.
"""

from .objects import Apple, Snake, GameObject  # noqa: F401

# Импорты для прохождения тестов
from .constants import (  # noqa: F401
    DOWN,
    GRID_HEIGHT,
    GRID_SIZE,
    GRID_WIDTH,
    LEFT,
    RIGHT,
    UP,
    BOARD_BACKGROUND_COLOR,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SPEED,
)
