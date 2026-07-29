from gameparts import GameObject, Apple, Snake
from gameparts import constants


def check_self_collision(snake):
    head_position = snake.get_head_position()
    if head_position in snake.positions[1:]:
        return True

    return False


def check_apple_collision(snake, apple):
    head_position = snake.get_head_position()
    if apple.position == head_position:
        return True

    return False
