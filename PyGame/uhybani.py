import pygame
from settings import *
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()

from Player import *
player = Player(WIDTH//2,HEIGHT)
player_group = pygame.sprite.Group()
player_group.add(player)

while running:
    screen.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player_group.update()
    player_group.draw(screen)
    
    clock.tick(FPS)
    pygame.display.update()
