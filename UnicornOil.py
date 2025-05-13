import pygame
from ball import Ball

pygame.init()

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

speed_ball = 1  # скорость перемещения клубники
# создание первой клубники
b1 = Ball(W//2, 'ponch.png')
b2 = Ball(W//3, 'ponch.png')
b3 = Ball(W//1.2, 'ponch.png')

# сориентируем квадрат(поверхность) единорога по центру внизу
unic_rect = unic_surf.get_rect(center=(300, 350))

# главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

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

    sc.blit(b1.image, b1.rect)  # отображаем клубнику и ее область
    sc.blit(b2.image, b2.rect)  # отображаем клубнику и ее область
    sc.blit(b3.image, b3.rect)  # отображаем клубнику и ее область

    pygame.display.update()

    clock.tick(FPS)

    # движение пончика
    # как только достигает низа кона, снова появляется сверху
    if b1.rect.y < H - 20:
        b1.rect.y += speed_ball
    else:
        b1.rect.y = 0

    if b2.rect.y < H - 20:
        b2.rect.y += speed_ball
    else:
        b2.rect.y = 0

    if b3.rect.y < H - 20:
        b3.rect.y += speed_ball
    else:
        b3.rect.y = 0
