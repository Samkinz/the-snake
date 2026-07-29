import pygame

from . import constants
from .score_manager import load_scores


def draw_title(screen, font):
    """Рисует заголовок игры."""
    title = font.render("ЗМЕЙКА", True, (255, 255, 255))
    screen.blit(title, (250, 80))


def draw_player_name(screen, font, name):
    """Рисует поле ввода имени."""
    name_text = font.render(f"Имя: {name}", True, (255, 255, 255))
    screen.blit(name_text, (100, 170))


def draw_menu_items(screen, font, menu_items, selected):
    """Рисует пункты меню."""
    for index, item in enumerate(menu_items):
        color = (255, 255, 0) if index == selected else (255, 255, 255)

        menu_text = font.render(item, True, color)
        screen.blit(menu_text, (100, 280 + index * 60))


def draw_scores(screen, font, scores):
    """Рисует таблицу результатов."""
    title = font.render("Результаты:", True, (255, 255, 255))
    screen.blit(title, (400, 170))

    for index, score in enumerate(scores):
        score_text = font.render(
            score.strip(),
            True,
            (255, 255, 255),
        )
        screen.blit(score_text, (400, 230 + index * 40))


def handle_menu_event(event, name, selected, menu_items):
    """Обрабатывает события главного меню."""
    if event.type == pygame.QUIT:
        pygame.quit()
        raise SystemExit

    if event.type == pygame.KEYDOWN:

        # Ввод имени
        if event.key == pygame.K_BACKSPACE:
            name = name[:-1]

        elif event.key not in (
            pygame.K_RETURN,
            pygame.K_UP,
            pygame.K_DOWN,
        ):
            name += event.unicode

        # Навигация
        elif event.key == pygame.K_UP:
            selected = (selected - 1) % len(menu_items)

        elif event.key == pygame.K_DOWN:
            selected = (selected + 1) % len(menu_items)

        # Запуск игры
        elif event.key == pygame.K_RETURN:

            if selected == 0 and name:
                return name, selected, True

            elif selected == 1:
                pygame.quit()
                raise SystemExit

    return name, selected, False


def main_menu(screen):
    """Отображает главное меню игры."""
    name = ""
    selected = 0

    menu_items = [
        "Начать игру",
        "Выход",
    ]

    title_font = pygame.font.Font(
        None,
        constants.TITLE_FONT_SIZE,
    )

    menu_font = pygame.font.Font(
        None,
        constants.MENU_FONT_SIZE,
    )

    score_font = pygame.font.Font(
        None,
        constants.SCORE_FONT_SIZE,
    )

    while True:
        screen.fill(constants.BOARD_BACKGROUND_COLOR)

        scores = load_scores()

        draw_title(screen, title_font)
        draw_player_name(screen, menu_font, name)
        draw_menu_items(
            screen,
            menu_font,
            menu_items,
            selected,
        )
        draw_scores(screen, score_font, scores)

        for event in pygame.event.get():
            (
                name,
                selected,
                start_game,
            ) = handle_menu_event(
                event,
                name,
                selected,
                menu_items,
            )

            if start_game:
                return name

        pygame.display.update()
