import pygame

from gameparts.constants import BOARD_BACKGROUND_COLOR
from gameparts.constants import SCREEN_HEIGHT
from gameparts.constants import SCREEN_WIDTH
from gameparts.constants import SPEED

from gameparts.field_rendering import draw_grid
from gameparts.game_logic import check_apple_collision
from gameparts.game_logic import check_self_collision
from gameparts.key_processing import handle_keys

from gameparts.objects import Apple
from gameparts.objects import Snake
from gameparts.objects import GameObject  # noqa: F401

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


def main():
    """Точка входа в игру"""
    running = True
    pygame.init()
    draw_grid(screen)
    pygame.display.update()

    snake = Snake()
    apple = Apple()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_keys(event, snake)

        snake.update_direction()
        snake.move()

        if check_apple_collision(snake, apple):
            snake.length += 1
            apple.randomize_position()

        if check_self_collision(snake):
            running = False

        screen.fill(BOARD_BACKGROUND_COLOR)
        draw_grid(screen)

        apple.draw(screen)
        snake.draw(screen)

        # Функция обработки действий пользователя

        pygame.display.update()

        clock.tick(SPEED)


if __name__ == '__main__':
    main()
