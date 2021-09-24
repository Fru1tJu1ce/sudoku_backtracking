import pygame


class Timer:
    """Класс для создания таймера."""

    def __init__(self, su_settings, screen, time):
        """Инициализирует атрибуты таймера."""
        self.screen = screen
        self.time = time
        self.su_settings = su_settings
        self.screen_rect = screen.get_rect()

        # Назначение размеров и свойств таймера.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont("Times New Roman", 48)
        self.time_image = self.font.render('Time: 0', True, self.text_color,
                                           (255, 255, 255))
        self.time_image_rect = self.time_image.get_rect()
        self.time_image_rect.centerx = 820
        self.time_image_rect.centery = 64

    def update_time(self, new_time):
        """Обновляет время на таймере."""
        self.time_image = self.font.render('Time: ' + str(new_time), True,
                                           self.text_color,
                                           (255, 255, 255))

    def draw_timer(self):
        """Вывод изображения таймера."""
        self.screen.blit(self.time_image, self.time_image_rect)
