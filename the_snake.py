from random import randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Цвет сетки
GRID_COLOR = (28, 28, 28)

# Скорость движения змейки:
SPEED = 20


# Функции проверки солкновения со змейкой / яблоком.
def check_self_collision(snake):
    """Проверка на столкновение головы змейки с туловищем."""
    head_position = snake.get_head_position()
    return head_position in snake.positions[1:]


def check_apple_collision(snake, apple):
    """Проверка на столкновение головы змейки с яблоком."""
    head_position = snake.get_head_position()
    return apple.position == head_position


# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


class GameObject:
    """Родительский класс объектов игры."""

    def __init__(self):
        self.position = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
        )
        self.body_color = None

    def draw(self, screen):
        """Метод отображения в родительском классе"""
        pass


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self) -> None:
        super().__init__()
        self.length = 1
        self.positions: list[tuple[int, int]] = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None
        self.body_color = SNAKE_COLOR

    def reset(self):
        """Возвращает змейку в начальное состояние."""
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def get_head_position(self):
        """Определяет позицию головы"""
        return self.positions[0]

    def move(self):
        """Определяет клетку, где будет голова змейки."""
        self.last = None

        head = self.get_head_position()
        x_pos = (head[0] + self.direction[0] * GRID_SIZE) % SCREEN_WIDTH
        y_pos = (head[1] + self.direction[1] * GRID_SIZE) % SCREEN_HEIGHT

        self.positions.insert(0, (x_pos, y_pos))

        if len(self.positions) > self.length:
            self.last = self.positions.pop()

    def draw(self, screen):
        """Отрисовка змейки."""
        for position in self.positions:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(
            self.positions[0],
            (GRID_SIZE, GRID_SIZE),
        )
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None


class Apple(GameObject):
    """Класс яблока."""

    def __init__(self):
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        """Определения позиции яблока."""
        random_cell_x = randint(0, GRID_WIDTH - 1)
        position_x = random_cell_x * GRID_SIZE

        random_cell_y = randint(0, GRID_HEIGHT - 1)
        position_y = random_cell_y * GRID_SIZE

        self.position = (position_x, position_y)

    def draw(self, screen):
        """Отрисовка яблока."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


# Рисование игрового поля


def draw_grid(screen):
    """Рисует сетку"""
    for y in range(0, 481, GRID_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, y),
            (SCREEN_WIDTH, y),
            2,
        )

    for x in range(0, 641, GRID_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (x, 0),
            (x, SCREEN_HEIGHT),
            2,
        )


# Логика нажатия на клавиши
def handle_keys(event, game_object):
    """Управление змейкой стрелками клавиатуры"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and game_object.direction != DOWN:
            game_object.next_direction = UP
        elif event.key == pygame.K_DOWN and game_object.direction != UP:
            game_object.next_direction = DOWN
        elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
            game_object.next_direction = LEFT
        elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
            game_object.next_direction = RIGHT


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
