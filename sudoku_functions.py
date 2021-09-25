import sys
import time

import pygame


def check_events(button, su_settings):
    """Обрабатывает события нажатий клавиш."""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(button, su_settings, mouse_x, mouse_y)


def check_keydown_events(event):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_q:
        sys.exit()


def zero_search(sudoku):
    """Ищет нуль."""
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None


def check_rules(sudoku, value, i, j):
    """Функция, которая проверяет возможность подставления цифры."""
    # Проверка строки на наличие значения
    if value in sudoku[i]:
        return False

    # Проверка сегмента по 9 чисел
    if i <= 2 and j <= 2:
        for row in sudoku[0:3]:
            if value in row[:3]:
                return False
    elif i <= 2 and (j > 2 and j <= 5):
        for row in sudoku[0:3]:
            if value in row[3:6]:
                return False
    elif i <= 2 and j > 5:
        for row in sudoku[0:3]:
            if value in row[6:]:
                return False
    elif (i > 2 and i <= 5) and j <= 2:
        for row in sudoku[3:6]:
            if value in row[:3]:
                return False
    elif (i > 2 and i <= 5) and (j > 2 and j <= 5):
        for row in sudoku[3:6]:
            if value in row[3:6]:
                return False
    elif (i > 2 and i <= 5) and j > 5:
        for row in sudoku[3:6]:
            if value in row[6:]:
                return False
    elif i > 5 and j <= 2:
        for row in sudoku[6:]:
            if value in row[:3]:
                return False
    elif i > 5 and (j > 2 and j <= 5):
        for row in sudoku[6:]:
            if value in row[3:6]:
                return False
    elif i > 5 and j > 5:
        for row in sudoku[6:]:
            if value in row[6:]:
                return False

    # Проверка столбца на наличие значения
    for k in range(len(sudoku)):
        if value == sudoku[k][j]:
            return False
    return True


def solve(screen, su_settings, field, timer, button):
    """Ищет решение судоку."""
    check_events(button, su_settings)
    contents = zero_search(su_settings.sudoku)
    if not contents:
        return True
    i, j = contents
    value = 1

    # Проверяем подхождение value под правила игры
    while value <= 9:
        # Отрисовка проверяемого значения
        draw_value(value, screen, i, j)
        draw_timer(timer)
        pygame.display.flip()

        if check_rules(su_settings.sudoku, value, i, j):
            su_settings.sudoku[i][j] = value

            if solve(screen, su_settings, field, timer, button):
                return True
        value += 1

    draw_timer(timer)
    draw_value(value, screen, i, j)
    su_settings.sudoku[i][j] = 0

    return False


def draw_value(value, screen, i, j):
    """Выводит изображение цифры в указанном положении."""
    text_color = (30, 30, 30)
    white = (255, 255, 255)
    font = pygame.font.SysFont(None, 44)

    if value != 10:
        sudoku_value_img = font.render(str(value), True, text_color,
                                       (255, 255, 255))
    else:
        sudoku_value_img = font.render(str(value), True, white,
                                       (255, 255, 255))
    value_rect = sudoku_value_img.get_rect()
    value_rect.centerx = 40 + 80 * j
    value_rect.centery = 64 + 80 * i

    screen.blit(sudoku_value_img, value_rect)


def draw_values(screen, su_settings):
    """Рисует поле судоку и известные значения."""
    for i in range(9):
        for j in range(9):
            if su_settings.sudoku[i][j] != 0:
                draw_value(su_settings.sudoku[i][j], screen, i, j)
                pygame.display.flip()


def draw_timer(timer):
    """Обновляет таймер."""
    new_time = int(time.time() - timer.time)
    timer.update_time(new_time)
    timer.draw_timer()


def check_play_button(button, su_settings, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play."""
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        su_settings.solving_active = True
