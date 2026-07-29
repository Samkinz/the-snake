import pygame
from gameparts import constants
from gameparts import GameObject, Apple, Snake
from gameparts.field_rendering import draw_grid
from gameparts.key_processing import handle_keys
from gameparts.game_logic import (
    check_apple_collision,
    check_self_collision,
    spawn_apple,
)
from gameparts.score_manager import save_score, load_scores
from gameparts.main_menu import main_menu

# Настройка игрового окна:
screen = pygame.display.set_mode(
    (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), 0, 32
)

# Заголовок окна игрового поля:
pygame.display.set_caption("Змейка")

# Настройка времени:
clock = pygame.time.Clock()


def game(player_name):
    running = True

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
            spawn_apple(apple, snake)

        if check_self_collision(snake):
            save_score(player_name, snake.length)
            running = False

        screen.fill(constants.BOARD_BACKGROUND_COLOR)
        draw_grid(screen)

        apple.draw(screen)
        snake.draw(screen)

        pygame.display.update()
        clock.tick(constants.SPEED)


def main():
    pygame.init()

    while True:
        player_name = main_menu(screen)

        game(player_name)


if __name__ == "__main__":
    main()
