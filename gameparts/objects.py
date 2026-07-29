from random import randint

import pygame

from gameparts import constants


class GameObject:
    """Родительский класс объектов игры."""

    def __init__(self):
        self.position = (
            constants.SCREEN_WIDTH // 2,
            constants.SCREEN_HEIGHT // 2,
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
        self.direction = constants.RIGHT
        self.next_direction = None
        self.last = None
        self.body_color = constants.SNAKE_COLOR

    def reset(self):
        """Возвращает змейку в начальное состояние."""
        self.length = 1
        self.positions = [self.position]
        self.direction = constants.RIGHT
        self.next_direction = None
        self.last = None

    def get_head_position(self):
        """Определяет позицию головы"""
        return self.positions[0]

    def move(self):
        """Определяет клетку, где будет голова змейки."""
        self.last = None

        head = self.get_head_position()
        x_pos = (
            head[0] + self.direction[0] * constants.GRID_SIZE
        ) % constants.SCREEN_WIDTH
        y_pos = (
            head[1] + self.direction[1] * constants.GRID_SIZE
        ) % constants.SCREEN_HEIGHT

        self.positions.insert(0, (x_pos, y_pos))

        if len(self.positions) > self.length:
            self.last = self.positions.pop()

    def draw(self, screen):
        """Отрисовка змейки."""
        for position in self.positions:
            rect = pygame.Rect(
                position, (constants.GRID_SIZE, constants.GRID_SIZE)
            )
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, constants.BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(
            self.positions[0],
            (constants.GRID_SIZE, constants.GRID_SIZE),
        )
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, constants.BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(
                self.last, (constants.GRID_SIZE, constants.GRID_SIZE)
            )
            pygame.draw.rect(
                screen, constants.BOARD_BACKGROUND_COLOR, last_rect
            )

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None


class Apple(GameObject):
    """Класс яблока."""

    def __init__(self):
        super().__init__()
        self.body_color = constants.APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        """Определения позиции яблока."""
        random_cell_x = randint(0, constants.GRID_WIDTH - 1)
        position_x = random_cell_x * constants.GRID_SIZE

        random_cell_y = randint(0, constants.GRID_HEIGHT - 1)
        position_y = random_cell_y * constants.GRID_SIZE

        self.position = (position_x, position_y)

    def draw(self, screen):
        """Отрисовка яблока."""
        rect = pygame.Rect(
            self.position, (constants.GRID_SIZE, constants.GRID_SIZE)
        )
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, constants.BORDER_COLOR, rect, 1)
