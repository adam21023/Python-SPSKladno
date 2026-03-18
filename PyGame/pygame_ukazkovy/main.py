import pygame
from Player import *
from Block import Block
from settings import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uhybani")
running = True
clock = pygame.time.Clock()
score = 0
score_font = pygame.font.SysFont("Arial", 30)
score_text = score_font.render(f"score:{score}", True, WHITE)
score_rect = score_text.get_rect(topleft=(10, 10))
hrac = Player(WIDTH // 2, HEIGHT)
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
blok = Block()
blok_group = pygame.sprite.Group()
blok_group.add(blok)
BLOCK_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(BLOCK_SPAWN, 2000)
        
        

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == BLOCK_SPAWN:
            blok_group.add(Block())
            score += 1
            score_text = score_font.render(f"Score: {score}", True, WHITE)
        if score >= highscore:
            highscore = score
            highscore_text = score_font.render
    
    hrac_group.update()
    hrac_group.draw(screen)
    blok_group.update()
    blok_group.draw(screen)

    


    if pygame.sprite.spritecollide(hrac, blok_group, True):
        print("KOLIZE!")
        pygame.time.delay(100)
        running = False
    
    screen.blit(score_text, score_rect)
    screen.blit(highscore_text, highscore_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()