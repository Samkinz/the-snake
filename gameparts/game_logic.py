from gameparts import constants


def check_self_collision(snake):
    """Проверка на столкновение головы с телом змейки"""
    head_position = snake.get_head_position()
    if head_position in snake.positions[1:]:
        return True

    return False


def check_apple_collision(snake, apple):
    """Проверка на столкновение головы с яблоком"""
    head_position = snake.get_head_position()
    if apple.position == head_position:
        return True

    return False


def spawn_apple(apple, snake):
    """Появление яблока. Проверка, что яблоко не касается тела змейки"""
    apple.randomize_position()

    while apple.position in snake.positions:
        apple.randomize_position()


def check_win(snake):
    """Проверка, что все поля заняты телом змейки. Игра завершается победой"""
    total_cells = constants.GRID_WIDTH * constants.GRID_HEIGHT

    if len(snake.positions) == total_cells:
        return True

    return False
