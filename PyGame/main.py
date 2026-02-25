import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving rectangle with jump")

x = 200
y = 400   # začíná na zemi

width = 20
height = 20

vel = 5
jump_vel = 15
gravity = 1

is_jumping = False
y_velocity = 0

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Pohyb do stran
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    # Skok (mezerník)
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            y_velocity = -jump_vel

    # Gravitace
    if is_jumping:
        y += y_velocity
        y_velocity += gravity

        # Kontrola země
        if y >= 500 - height:
            y = 500 - height
            is_jumping = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
