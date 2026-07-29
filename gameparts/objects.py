import pygame
from gameparts import constants
from random import randint


class GameObject:
    """Родительский класс объектов игры"""

    def __init__(self):
        self.position = (constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)

    def draw(self, screen):
        pass


class Snake(GameObject):

    def __init__(self):
        super().__init__()
        self.length = 1
        self.positions: list[tuple[int, int]] = [self.position]
        self.direction = constants.RIGHT
        self.next_direction = None
        self.last = None
        self.body_color = constants.SNAKE_COLOR

    def get_head_position(self):
        return self.positions[0]

    def move(self):
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
        for position in self.positions:
            rect = pygame.Rect(position, (constants.GRID_SIZE, constants.GRID_SIZE))
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
            pygame.draw.rect(screen, constants.BOARD_BACKGROUND_COLOR, last_rect)

    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None


class Apple(GameObject):
    def __init__(self):
        super().__init__()
        self.body_color = constants.APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        random_cell_x = randint(0, constants.GRID_WIDTH - 1)
        position_x = random_cell_x * constants.GRID_SIZE

        random_cell_y = randint(0, constants.GRID_HEIGHT - 1)
        position_y = random_cell_y * constants.GRID_SIZE

        self.position = (position_x, position_y)

        return None

    def draw(self, screen):
        rect = pygame.Rect(self.position, (constants.GRID_SIZE, constants.GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, constants.BORDER_COLOR, rect, 1)
