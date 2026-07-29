"""Пакет игровых компонентов игры «Змейка»."""

from .objects import Apple, GameObject, Snake
from .score_manager import load_scores, save_score
from .main_menu import main_menu

__all__ = [
    "Apple",
    "GameObject",
    "Snake",
    "load_scores",
    "save_score",
    "main_menu",
]
