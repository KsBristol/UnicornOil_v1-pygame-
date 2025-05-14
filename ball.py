import pygame


class Ball(pygame.sprite.Sprite):
    """ Для обработки групп спрайтов"""
    def __init__(self, x, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        # изображение спрайта(ссылка на передаваемую поверхность)
        self.image = surf
        # его размер и местоположение располагаем
        # для падения посередине координаты x, а по y будет равно 0
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, *args):
        """Движение пончика как только достигает низа окна,
        удаляется из группы
        в args передаем высоту рабочей зоны"""
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()

