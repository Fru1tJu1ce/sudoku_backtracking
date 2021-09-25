import pygame
import time

from settings import Settings
from field import SudokuField
from timer import Timer
import sudoku_functions as sf
from button import Button


def run_sudoku():
    """Инициализирует pygame и запускает визуализацию."""
    # Инициализация pygame, размера экрана и названия окна
    pygame.init()
    su_settings = Settings()
    screen = pygame.display.set_mode((su_settings.screen_width,
                                      su_settings.screen_height))
    pygame.display.set_caption("Sudoku backtracking solver")

    # Заливаем задний фон белым цветом
    screen.fill(su_settings.screen_color)

    # Создаем экземпляр поля
    field = SudokuField(screen)

    # Создаем экземпляр кнопки
    button = Button(screen, 'Solve!')
    button.draw_button()

    # Сетап таймера
    timer = Timer(su_settings, screen)
    timer.draw_timer()

    # Вывод поля и известных значений судоку
    field.blitme()
    sf.draw_values(screen, su_settings)

    while True:
        sf.check_events(button, su_settings)
        if su_settings.solving_active:
            timer.time = time.time()
            sf.solve(screen, su_settings, field, timer, button)
            su_settings.solving_active = False
        pygame.display.flip()


if __name__ == '__main__':
    run_sudoku()
