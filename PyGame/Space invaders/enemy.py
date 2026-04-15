import pygame
import settings
import random as rand
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        alien_type = rand.randint(1, 5)
        self.image = pygame.image.load(settings.ENEMY_IMAGE_PATH.format(alien_type)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*settings.ENEMY_SCALE,self.image.get_height()*settings.ENEMY_SCALE))
        self.rect = self.image.get_rect(top = y, centerx= x) # center = (x,y)¨
        self.speed = settings.PLAYER_SPEED

       
if __name__ == "__main__":
    import main