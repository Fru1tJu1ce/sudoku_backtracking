import pygame


class SudokuField:
    """Класс, представляющий поле судоку."""

    def __init__(self, screen):
        self.screen = screen

    def blitme(self):
        """Выводит сетку судоку на экран."""
        for k in range(10):
            if k % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), [0, 24 + 80 * k],
                                 [720, 24 + 80 * k], 3)
            else:
                pygame.draw.line(self.screen, (0, 0, 0), [0, 24 + 80 * k],
                                 [720, 24 + 80 * k])

        for k in range(10):
            if k % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), [80 * k, 24],
                                 [80 * k, 744], 3)
            else:
                pygame.draw.line(self.screen, (0, 0, 0), [80 * k, 24],
                                 [80 * k, 744])
