import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, image, x, y, *groups):
        super().__init__(*groups)
        
        self.image = pygame.image.load(image)
        
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y


class Hero(Obj):
    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)
        
        self.vel = 4
        self.grav = 1
        
    def update(self):
        self.gravity()
    
    def gravity(self):
        self.vel += self.grav
        self.rect[1] += self.vel
        
        if self.vel >= 10:
            self.vel = 10
    
    def colisions(self, group, kill):
        
        col = pygame.sprite.spritecollide(self, group, kill)
        
        if col:
            self.rect.bottom = col[0].rect.top