import pygame


class Ball(pygame.sprite.Sprite):
    """ Для обработки групп спрайтов"""
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        # изображение спрайта(ссылка на Surface)
        # его загружаем из файла
        self.image = pygame.image.load(filename).convert_alpha()
        # его размер и местоположение
        # располагаем для падения посередине координаты x,
        # а по y будет равно 0
        self.rect = self.image.get_rect(center=(x, 0))

