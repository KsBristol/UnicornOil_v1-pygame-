import pygame
from ball import Ball
from random import randint

pygame.init()
# функция каждые 2000мс будет генерировать событие USEREVENT
pygame.time.set_timer(pygame.USEREVENT, 2000)

# устанавливаем размер игрового поля
W, H = 600, 400
sc = pygame.display.set_mode((W, H))
# Название в титуле
pygame.display.set_caption("UnicornOil")
# иконка на главном экране
pygame.display.set_icon(pygame.image.load("unicornOil_unic.bmp"))

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

sc.fill(WHITE)
pygame.display.update()

# вернет поверхность, на которой будет нарисовано это изображение
unic_surf = pygame.image.load("unicornOil_unic_v2.png").convert()
# указываем цвет, который необходимо сделать прозрачным
unic_surf.set_colorkey((255, 255, 255))
bg_surf = pygame.image.load("rainbow_fon.png").convert_alpha()
finish_surf = pygame.image.load("finish_obl.png").convert_alpha()

unic_left = unic_surf
# отражаем изображение относительно оси y,
# чтобы единорог смотрел в другую сторону
unic_right = pygame.transform.flip(unic_surf, True, False)

unic = unic_left
speed_unic = 4  # скорость перемещения единорога

# создание объектов пончиков и капель через единую группу
balls = pygame.sprite.Group()
# один раз загрузим картинки
balls_images = ['drop.png', 'ponch.png']
# формирование списка из поверхностей загруженного изображения
balls_surf = [pygame.image.load(path).convert_alpha() for path in balls_images]


def createBall(group):
    """Функция для создания нового объекта пончика или капли,
    со случайным выбором изображения и со случайной
    координатой по х"""
    indx = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], group)


# сориентируем квадрат(поверхность) единорога по центру внизу
unic_rect = unic_surf.get_rect(center=(300, 350))

# главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

    # get_pressed() - возвращает номера нажатых клавиш
    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:  # нажатие на кнопку налево
        unic = unic_left
        # убавляем скорость от координаты x
        unic_rect.x -= speed_unic
        # если координата становится < 0 мы приравниваем её 0,
        # чтобы единорог не выходил за пределы экрана
        if unic_rect.x < 0:
            unic_rect.x = 0
    elif bt[pygame.K_RIGHT]:  # нажатие на кнопку направо
        unic = unic_right
        # прибавляем скорость к координате x
        unic_rect.x += speed_unic
        # если мы достигаем правого края, то координата x приравнивается
        # правому краю, чтобы единорог не выходил за пределы экрана
        if unic_rect.x > W - unic_rect.height:
            unic_rect.x = W - unic_rect.height

    # перерисовываем после всех движений
    # очищаем чтобы не было следов
    # заполняя поле белым на каждой итерации цикла
    sc.fill(WHITE)  # цвет заливки
    sc.blit(bg_surf, (0, 0))  # радуга на заднем фоне
    sc.blit(finish_surf, (15, 0))  # финишное облачко
    sc.blit(unic, unic_rect)  # сам единорог и квадрат единорога

    balls.draw(sc)  # отображение всей группы объектов balls

    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)  # движение пончиков и капель
