import pygame
import random as rand
import settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Explosion import Explosion
from Boss import Boss

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders OOP V2")
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

explosion_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
level = 1
def create_lvl(level):
    if level > 5:
        enemy = Boss(150, 25)
        enemy_group.add(enemy)
    else:
        x = 75
        y = 25
        for i in range(level):
            for j in range(level*2):
                enemy = Enemy(x,y)
                x += 50
                enemy_group.add(enemy)
            y += 50
            x = 75
create_lvl(level)



running = True
while running:
    clock.tick(settings.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.cooldown == 0:
                    bullet = Bullet(player.rect.left +5 ,player.rect.top +40 ,"Player")
                    player_bullet_group.add(bullet)
                    bullet = Bullet(player.rect.right -5 ,player.rect.top +40,"Player")
                    player_bullet_group.add(bullet)
                    player.cooldown = pygame.time.get_ticks()

    current_time = pygame.time.get_ticks()
    for enemy in enemy_group:
        if current_time - enemy.last_shooting_time >= enemy.shooting_cooldown:
            bullet = Bullet(enemy.rect.left +5 ,enemy.rect.bottom +40)
            enemy_bullet_group.add(bullet)
            enemy.last_shooting_time = current_time
            enemy.shooting_cooldown = rand.randint(1000, 5000)

    if pygame.sprite.groupcollide(player_group, enemy_bullet_group, True, True, collided = pygame.sprite.collide_mask):
        print("Player hit!")
        running = False
    
    collided_enemies = pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, True, collided = pygame.sprite.collide_mask)
    for enemy in collided_enemies:
        if enemy.hp > 1:
            enemy.hp -=1
            print("Enemy hit! HP left:", enemy.hp)
        else:
            explosion = Explosion(enemy.rect.centerx, enemy.rect.centery)
            explosion_group.add(explosion)
            enemy.kill()
            print("Enemy shotted down")
        if len(enemy_group) == 0:
            level += 1
            create_lvl(level)
        if pygame.sprite.groupcollide(enemy_group, player_group, False, True, collided = pygame.sprite.collide_mask):
            print("Player hit by enemy!")  
            running = False          
                

                    




    screen.fill(settings.BG_COLOR)
    player_group.update()
    player_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    enemy_bullet_group.update() 
    enemy_bullet_group.draw(screen)
    explosion_group.draw(screen)
    explosion_group.update()
    pygame.display.flip()
pygame.quit()


