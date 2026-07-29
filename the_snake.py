import pygame
from gameparts import constants
from gameparts import GameObject, Apple, Snake
from gameparts.field_rendering import draw_grid
from gameparts.key_processing import handle_keys
from gameparts.game_logic import check_apple_collision, check_self_collision

# Настройка игрового окна:
screen = pygame.display.set_mode(
    (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), 0, 32
)

# Заголовок окна игрового поля:
pygame.display.set_caption("Змейка")

# Настройка времени:
clock = pygame.time.Clock()


def main():
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

        screen.fill(constants.BOARD_BACKGROUND_COLOR)
        draw_grid(screen)

        apple.draw(screen)
        snake.draw(screen)

        # Функция обработки действий пользователя

        pygame.display.update()

        clock.tick(constants.SPEED)


if __name__ == "__main__":
    main()


# Метод обновления направления после нажатия на кнопку
# def update_direction(self):
#     if self.next_direction:
#         self.direction = self.next_direction
#         self.next_direction = None
