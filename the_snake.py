from random import choice, randint

import pygame

SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480
GRID_SIZE: int = 20
GRID_WIDTH: int = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT: int = SCREEN_HEIGHT // GRID_SIZE

UP: tuple[int, int] = (0, -1)
DOWN: tuple[int, int] = (0, 1)
LEFT: tuple[int, int] = (-1, 0)
RIGHT: tuple[int, int] = (1, 0)

BOARD_BACKGROUND_COLOR: tuple[int, int, int] = (0, 0, 0)
BORDER_COLOR: tuple[int, int, int] = (93, 216, 228)
APPLE_COLOR: tuple[int, int, int] = (255, 0, 0)
SNAKE_COLOR: tuple[int, int, int] = (0, 255, 0)
GRID_COLOR: tuple[int, int, int] = (28, 28, 28)

SPEED: int = 20


class GameObject:
    """Базовый объект игры."""

    def __init__(self) -> None:
        """Задаёт начальные параметры объекта."""
        self.position: tuple[int, int] = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
        )
        # Цвет по умолчанию нужен для совместимости с типизацией mypy.
        # Подклассы задают собственные цвета через параметры конструктора.
        self.body_color: tuple[int, int, int] = (0, 0, 0)

    def draw(self, screen: pygame.Surface) -> None:
        """Отображает объект на игровом поле."""


class Snake(GameObject):
    """Представляет объект змейки."""

    def __init__(
        self,
        body_color: tuple[int, int, int] = SNAKE_COLOR,
    ) -> None:
        super().__init__()
        self.reset()
        self.direction: tuple[int, int] = RIGHT
        self.body_color: tuple[int, int, int] = body_color

    def reset(self) -> None:
        """Возвращает змейку в начальное состояние."""
        self.length: int = 1
        self.positions: list[tuple[int, int]] = [self.position]
        self.direction = choice([RIGHT, LEFT, UP, DOWN])
        self.last: tuple[int, int] | None = None

    def get_head_position(self) -> tuple[int, int]:
        """Возвращает позицию головы."""
        return self.positions[0]

    def move(self) -> None:
        """Определяет клетку, где будет голова змейки."""
        self.last = None

        x, y = self.get_head_position()
        direction_x, direction_y = self.direction

        x_pos = (x + direction_x * GRID_SIZE) % SCREEN_WIDTH
        y_pos = (y + direction_y * GRID_SIZE) % SCREEN_HEIGHT

        self.positions.insert(0, (x_pos, y_pos))

        if len(self.positions) > self.length:
            self.last = self.positions.pop()

    def draw(self, screen: pygame.Surface) -> None:
        """Отрисовывает змейку."""
        for position in self.positions:
            rect = pygame.Rect(
                position,
                (GRID_SIZE, GRID_SIZE),
            )
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        if self.last:
            last_rect = pygame.Rect(
                self.last,
                (GRID_SIZE, GRID_SIZE),
            )
            pygame.draw.rect(
                screen,
                BOARD_BACKGROUND_COLOR,
                last_rect,
            )
            draw_cell_border(screen, self.last)

    def update_direction(
        self,
        new_direction: tuple[int, int],
    ) -> None:
        """Обновляет направление движения змейки."""
        self.direction = new_direction


class Apple(GameObject):
    """Представляет объект яблока."""

    def __init__(
        self,
        body_color: tuple[int, int, int] = APPLE_COLOR,
    ) -> None:
        super().__init__()
        self.body_color = body_color

    def randomize_position(
        self,
        occupied_positions: list[tuple[int, int]],
    ) -> None:
        """Определяет случайную позицию яблока."""
        while True:
            random_cell_x = randint(0, GRID_WIDTH - 1)
            random_cell_y = randint(0, GRID_HEIGHT - 1)

            new_position = (
                random_cell_x * GRID_SIZE,
                random_cell_y * GRID_SIZE,
            )

            if new_position not in occupied_positions:
                self.position = new_position
                break

    def draw(self, screen: pygame.Surface) -> None:
        """Отрисовывает яблоко."""
        rect = pygame.Rect(
            self.position,
            (GRID_SIZE, GRID_SIZE),
        )
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


def check_self_collision(snake: Snake) -> bool:
    """Проверяет столкновение головы змейки с туловищем."""
    head_position = snake.get_head_position()
    return head_position in snake.positions[1:]


def check_apple_collision(
    snake: Snake,
    apple: Apple,
) -> bool:
    """Проверяет столкновение головы змейки с яблоком."""
    head_position = snake.get_head_position()
    return apple.position == head_position


screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT),
    0,
    32,
)

pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()


def draw_grid(screen: pygame.Surface) -> None:
    """Рисует сетку."""
    for y in range(0, SCREEN_HEIGHT + GRID_SIZE, GRID_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, y),
            (SCREEN_WIDTH, y),
            2,
        )

    for x in range(0, SCREEN_WIDTH + GRID_SIZE, GRID_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (x, 0),
            (x, SCREEN_HEIGHT),
            2,
        )


def draw_cell_border(
    screen: pygame.Surface,
    position: tuple[int, int],
) -> None:
    """Восстанавливает границу клетки после движения змейки."""
    pygame.draw.rect(
        screen,
        GRID_COLOR,
        pygame.Rect(
            position,
            (GRID_SIZE, GRID_SIZE),
        ),
        1,
    )


def handle_keys(game_object: Snake) -> bool:
    """Управляет змейкой с клавиатуры."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.update_direction(UP)

            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.update_direction(DOWN)

            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.update_direction(LEFT)

            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.update_direction(RIGHT)

            elif event.key == pygame.K_ESCAPE:
                return False

    return True


def main() -> None:
    """Точка входа в игру."""
    pygame.init()

    snake = Snake()
    apple = Apple()
    apple.randomize_position(snake.positions)

    screen.fill(BOARD_BACKGROUND_COLOR)
    draw_grid(screen)

    apple.draw(screen)
    snake.draw(screen)

    pygame.display.update()

    running = True

    while running:
        running = handle_keys(snake)

        snake.move()

        if check_apple_collision(snake, apple):
            snake.length += 1
            apple.randomize_position(snake.positions)

        if check_self_collision(snake):
            snake.reset()
            apple.randomize_position(snake.positions)

            screen.fill(BOARD_BACKGROUND_COLOR)
            draw_grid(screen)

        apple.draw(screen)
        snake.draw(screen)

        pygame.display.update()

        clock.tick(SPEED)


if __name__ == '__main__':
    main()
