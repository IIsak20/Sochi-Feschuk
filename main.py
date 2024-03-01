import pygame
pygame.init()

# Устанавливаем размеры окна
width, height = 1920, 1080
win = pygame.display.set_mode((width, height))

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)

# Загрузка изображений
pygame.image.load_extended = True
phon_image = pygame.transform.scale(pygame.image.load('sprites/phon.png'), (3408, 1080))

# Разделение изображения пополам вертикально
pokoi_image = pygame.image.load('sprites/gg/pokoi.png')
pokoi_rect = pokoi_image.get_rect(topleft=(500, 500))
show_character_animation = False

# Создание анимации персонажа вправо
pravo_image = pygame.image.load('sprites/gg/pravo.png')
pravo_rect = pravo_image.get_rect(topleft=(0, 0))
pravo_images = [pravo_image.subsurface((0, 0, pravo_rect.width // 2, pravo_rect.height)),
                pravo_image.subsurface((pravo_rect.width // 2, 0, pravo_rect.width // 2, pravo_rect.height))]
pravo_index = 0

# Создание анимации персонажа влево
vlevo_image = pygame.image.load('sprites/gg/vlevo.png')
vlevo_rect = vlevo_image.get_rect(topleft=(0, 0))
vlevo_images = [vlevo_image.subsurface((0, 0, vlevo_rect.width // 2, vlevo_rect.height)),
                vlevo_image.subsurface((vlevo_rect.width // 2, 0, vlevo_rect.width // 2, vlevo_rect.height))]
vlevo_index = 0

# Создание анимации персонажа вверх
vverh_image = pygame.image.load('sprites/gg/vverh.png')
vverh_rect = vverh_image.get_rect(topleft=(0, 0))
vverh_images = [vverh_image.subsurface((0, 0, vverh_rect.width, vverh_rect.height // 4)),
                vverh_image.subsurface((0, vverh_rect.height // 4, vverh_rect.width, vverh_rect.height // 4)),
                vverh_image.subsurface((0, vverh_rect.height // 2, vverh_rect.width, vverh_rect.height // 4)),
                vverh_image.subsurface((0, 3 * vverh_rect.height // 4, vverh_rect.width, vverh_rect.height // 4))]
vverh_index = 0

# Создание анимации персонажа вниз
vniz_image = pygame.image.load('sprites/gg/vniz.png')
vniz_rect = vniz_image.get_rect(topleft=(0, 0))
vniz_images = [vniz_image.subsurface((0, 0, vniz_rect.width, vniz_rect.height // 4)),
               vniz_image.subsurface((0, vniz_rect.height // 4, vniz_rect.width, vniz_rect.height // 4)),
               vniz_image.subsurface((0, vniz_rect.height // 2, vniz_rect.width, vniz_rect.height // 4)),
               vniz_image.subsurface((0, 3 * vniz_rect.height // 4, vniz_rect.width, vniz_rect.height // 4))]
vniz_index = 0

# Начальные координаты персонажа
character_pos = [1000, 500]

# Создание группы спрайтов
all_sprites = pygame.sprite.Group()

# Добавление спрайтов в группу all_sprites
exit_button_sprite = pygame.sprite.Sprite()
exit_button_sprite.image = pygame.image.load("sprites/screen/exit.png")
exit_button_sprite.rect = exit_button_sprite.image.get_rect(topleft=(760, 600))
all_sprites.add(exit_button_sprite)

play_button_sprite = pygame.sprite.Sprite()
play_button_sprite.image = pygame.image.load("sprites/screen/play.png")
play_button_sprite.rect = play_button_sprite.image.get_rect(topleft=(760, 400))
all_sprites.add(play_button_sprite)

# Главный цикл игры
run = True
show_phon = False
show_character_animation = False
clock = pygame.time.Clock()

speed = 5

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            show_character_animation = False
            if play_button_sprite.rect.collidepoint(mouse_pos):
                show_phon = True
                show_character_animation = True
            if exit_button_sprite.rect.collidepoint(mouse_pos):
                show_character_animation = False
                pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        character_pos[1] -= speed
        show_character_animation = True
        character_index = vverh_index
        vverh_index = (vverh_index + 1) % len(vverh_images)
    elif keys[pygame.K_s]:
        character_pos[1] += speed
        show_character_animation = True
        character_index = vniz_index
        vniz_index = (vniz_index + 1) % len(vniz_images)
    elif keys[pygame.K_d]:
        character_pos[0] += speed
        show_character_animation = True
        character_index = pravo_index
        pravo_index = (pravo_index + 1) % len(pravo_images)
    elif keys[pygame.K_a]:
        character_pos[0] -= speed
        show_character_animation = True
        character_index = vlevo_index
        vlevo_index = (vlevo_index + 1) % len(vlevo_images)
    else:
        show_character_animation = False

    win.fill(white)
    win.blit(pygame.image.load("sprites/screen/screen.png"), (0, 0))

    all_sprites.draw(win)

    if show_phon:
        win.blit(phon_image, (0, 0))

    if show_character_animation:
        if keys[pygame.K_w]:
            win.blit(vverh_images[vverh_index], character_pos)
        elif keys[pygame.K_s]:
            win.blit(vniz_images[vniz_index], character_pos)
        elif keys[pygame.K_d]:
            win.blit(pravo_images[pravo_index], character_pos)
        elif keys[pygame.K_a]:
            win.blit(vlevo_images[vlevo_index], character_pos)
    else:
        win.blit(pokoi_image, character_pos)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
