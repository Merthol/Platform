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
        
        self.rigth = False
        self.left = False
        self.jump = False
        
    def update(self):
        self.gravity()
        self.moviments()
    
    def gravity(self):
        self.vel += self.grav
        self.rect[1] += self.vel
        
        if self.vel >= 10:
            self.vel = 10
    
    def colisions(self, group, kill):
        col = pygame.sprite.spritecollide(self, group, kill)
        
        if col:
            self.rect.bottom = col[0].rect.top
    
    def events(self, events):
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_d:
                self.rigth = True
                print("Direita")
            elif events.key == pygame.K_a:
                self.left = True
                print("Esquerda")
            if events.key == pygame.K_SPACE:
                # self.jump = True
                self.vel *= -1
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_d:
                self.rigth = False
            elif events.key == pygame.K_a:
                self.left = False
            # if events.key == pygame.K_SPACE:
            #     self.jump = False
    
    def moviments(self):
        if self.rigth:
            self.rect[0] += 8
        elif self.left:
            self.rect[0] -= 8
