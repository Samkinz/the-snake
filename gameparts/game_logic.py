def check_self_collision(snake):
    head_position = snake.get_head_position()
    return head_position in snake.positions[1:]


def check_apple_collision(snake, apple):
    head_position = snake.get_head_position()
    return apple.position == head_position
