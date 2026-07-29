import pygame

from .score_manager import load_scores
from . import constants


def main_menu(screen):
    name = ""
    selected = 0

    menu_items = [
        "Начать игру",
        "Выход",
    ]

    title_font = pygame.font.Font(None, constants.TITLE_FONT_SIZE)
    menu_font = pygame.font.Font(None, constants.MENU_FONT_SIZE)
    score_font = pygame.font.Font(None, constants.SCORE_FONT_SIZE)

    while True:
        screen.fill(constants.BOARD_BACKGROUND_COLOR)

        scores = load_scores()

        # Заголовок
        title = title_font.render("ЗМЕЙКА", True, (255, 255, 255))
        screen.blit(title, (250, 80))

        # Ввод имени
        name_text = menu_font.render(f"Введите имя: {name}", True, (255, 255, 255))
        screen.blit(name_text, (100, 170))

        # Пункты меню
        for index, item in enumerate(menu_items):
            color = (255, 255, 0) if index == selected else (255, 255, 255)
            menu_text = menu_font.render(item, True, color)
            screen.blit(menu_text, (100, 280 + index * 60))

        # Таблица результатов
        scores_title = menu_font.render("Результаты:", True, (255, 255, 255))
        screen.blit(scores_title, (400, 170))

        for index, score in enumerate(scores):
            score_text = score_font.render(score.strip(), True, (255, 255, 255))
            screen.blit(score_text, (400, 230 + index * 35))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                # Удаление символа
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                # Ввод имени
                elif event.key not in (
                    pygame.K_RETURN,
                    pygame.K_UP,
                    pygame.K_DOWN,
                ):
                    name += event.unicode
                # Навигация вверх
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_items)

                # Навигация вниз
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_items)

                # Выбор пункта
                elif event.key == pygame.K_RETURN:

                    if selected == 0 and name:
                        return name

                    elif selected == 1:
                        pygame.quit()
                        raise SystemExit

        pygame.display.update()
