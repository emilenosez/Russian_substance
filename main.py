import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode([626, 391])
pygame.display.set_caption("Russian_substance")

menu = pygame.image.load('images/menu.png')

bg = pygame.image.load('images/bg.jpg')
bg2 = bg
bg_x = 0

bro_right_1 = pygame.image.load('images/bro/right/bro_1.png')
bro_right_2 = pygame.image.load('images/bro/right/bro_2.png')
bro_right_3 = pygame.image.load('images/bro/right/bro_3.png')
bro_right_4 = pygame.image.load('images/bro/right/bro_4.png')
bro_right = [bro_right_1, bro_right_2, bro_right_3, bro_right_4]
bro_right_i = 0


#координаты персонажа
bro_x = 10
bro_y = 280

#счетчик кадров прыжка
jump_frame_current = 0
jump_frame_total = 30

#меню
is_menu = False

run = True
while run:
    dt = clock.tick(60) / 1000
    if is_menu:
        screen.blit(menu, (0, 0))
    else:
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg2, (bg_x + 626, 0))
        bg_x = bg_x - 2
        if bg_x < -626:
            bg_x = 0

        screen.blit(bro_right[bro_right_i], (bro_x, bro_y))

        keys = pygame.key.get_pressed()
        #движение вверх, вниз и влево
        if keys[pygame.K_w]:
            bro_y -= 1
        if keys[pygame.K_s]:
            bro_y += 1
        if keys[pygame.K_a]:
            bro_x -= 1
        #движение вправо и смена кадров движения
        if keys[pygame.K_d]:
            bro_x += 1
            bro_right_i += 1
            if bro_right_i > 3:
                bro_right_i = 0
        else:
            bro_right_i = 0 #если движение закончилось, то персонаж останавливается

    #прыжок
        if jump_frame_current > jump_frame_total/2:
            bro_y -= 7
            jump_frame_current -= 1
        if jump_frame_current > 0 and jump_frame_current <= jump_frame_total/2:
            bro_y += 7
            jump_frame_current -= 1

    pygame.display.update()

    for event in pygame.event.get():
        #кнопка выхода
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

        if event.type == pygame.KEYDOWN:
            #прыжок
            if event.key == pygame.K_SPACE and jump_frame_current == 0:
                jump_frame_current = jump_frame_total
            #меню
            if event.key == pygame.K_e:
                is_menu = not is_menu
