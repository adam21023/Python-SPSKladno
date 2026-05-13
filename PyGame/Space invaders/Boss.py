import pygame
from Enemy import Enemy
import settings
import random as rand

class Boss(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.BOSS_SCALE, self.image.get_height()*settings.BOSS_SCALE))
        self.hp = 20
    
    def _check_borders(self):
        # Boss bounces exactly at the screen edges
        if self.rect.right >= settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
            self.direction = -1
            self.rect.y += settings.ENEMY_DROP_SPEED * 2
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.direction = 1
            self.rect.y += settings.ENEMY_DROP_SPEED * 2

