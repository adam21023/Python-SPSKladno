import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Balon na lajně")

# čára
line_y = 300
line_start = 100
line_end = 500

# načtení obrázku
balloon_img = pygame.image.load("balon.png").convert_alpha()
balloon_img = pygame.transform.scale(balloon_img, (80, 80))

width = balloon_img.get_width()
height = balloon_img.get_height()

# start
x = line_start + width // 2
speed = 4
direction = 1   # 1 = doprava, -1 = doleva
angle = 0

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # pohyb
    x += speed * direction

    # rotace podle směru
    angle -= speed * direction * 2

    # otočení na krajích
    if x >= line_end - width // 2:
        direction = -1
    if x <= line_start + width // 2:
        direction = 1

    screen.fill((30, 30, 30))

    # čára
    pygame.draw.line(screen, (255, 255, 255),
                     (line_start, line_y),
                     (line_end, line_y), 5)

    # rotace obrázku
    rotated_img = pygame.transform.rotate(balloon_img, angle)
    rect = rotated_img.get_rect(
        center=(x, line_y - height // 2)  # přesně na čáře
    )

    screen.blit(rotated_img, rect)

    pygame.display.flip()



