import pygame
from .score_manager import load_scores


def main_menu(screen):
    name = ""
    selected = 0

    scores = load_scores()

    menu_items = [
        "Начать игру",
        "Выход",
    ]

    font = pygame.font.Font(None, 50)

    while True:
        screen.fill((0, 0, 0))

        # Заголовок
        title = font.render("ЗМЕЙКА", True, (255, 255, 255))
        screen.blit(title, (250, 80))

        # Поле имени
        name_text = font.render(f"Имя: {name}", True, (255, 255, 255))
        screen.blit(name_text, (100, 170))

        # Пункты меню
        for index, item in enumerate(menu_items):
            color = (255, 255, 0) if index == selected else (255, 255, 255)

            menu_text = font.render(item, True, color)

            screen.blit(menu_text, (100, 280 + index * 60))

        for event in pygame.event.get():

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

                # Выбор пункта
                elif event.key == pygame.K_RETURN:

                    if selected == 0 and name:
                        return name

                    elif selected == 1:
                        pygame.quit()
                        raise SystemExit

        pygame.display.update()
