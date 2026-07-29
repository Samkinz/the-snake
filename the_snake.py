from random import choice, randint

import pygame
from gameparts import GameObject
from gameparts import constants

# Настройка игрового окна:
screen = pygame.display.set_mode(
    (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), 0, 32
)

# Заголовок окна игрового поля:
pygame.display.set_caption("Змейка")

# Настройка времени:
clock = pygame.time.Clock()


def draw_grid():
    """Рисует сетку"""

    for y in range(0, 481, constants.GRID_SIZE):
        pygame.draw.line(
            screen, constants.GRID_COLOR, (0, y), (constants.SCREEN_WIDTH, y), 2
        )

    for x in range(0, 641, constants.GRID_SIZE):
        pygame.draw.line(
            screen, constants.GRID_COLOR, (x, 0), (x, constants.SCREEN_HEIGHT), 2
        )

    # pygame.draw.line(surface, color, start_pos, end_pos, width)


# Тут опишите все классы игры.
...


def main():
    # Инициализация PyGame:
    pygame.init()
    draw_grid()
    pygame.display.update()
    running = True
    # Тут нужно создать экземпляры классов.
    ...
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(constants.SPEED)

    # Тут опишите основную логику игры.
    # ...


if __name__ == "__main__":
    main()


# Метод draw класса Apple
# def draw(self):
#     rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, self.body_color, rect)
#     pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

# # Метод draw класса Snake
# def draw(self):
#     for position in self.positions[:-1]:
#         rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
#         pygame.draw.rect(screen, self.body_color, rect)
#         pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

#     # Отрисовка головы змейки
#     head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
#     pygame.draw.rect(screen, self.body_color, head_rect)
#     pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

#     # Затирание последнего сегмента
#     if self.last:
#         last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
#         pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

# Функция обработки действий пользователя
# def handle_keys(game_object):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and game_object.direction != DOWN:
#                 game_object.next_direction = UP
#             elif event.key == pygame.K_DOWN and game_object.direction != UP:
#                 game_object.next_direction = DOWN
#             elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
#                 game_object.next_direction = LEFT
#             elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
#                 game_object.next_direction = RIGHT

# Метод обновления направления после нажатия на кнопку
# def update_direction(self):
#     if self.next_direction:
#         self.direction = self.next_direction
#         self.next_direction = None
