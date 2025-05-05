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
        
        self.max_vel = 15
        self.vel = self.max_vel
        self.grav = 1
        
        self.rigth = False
        self.left = False
        self.jump = False
        
        self.direction = False
        
        self.ticks = 0
        self.img_count = 0
        
        self.colections = 0
        
        self.lifes = 3
        
    def update(self):
        self.gravity()
        self.moviments()
    
    def gravity(self):
        self.vel += self.grav
        self.rect[1] += self.vel
        
        if self.vel >= self.max_vel:
            self.vel = self.max_vel
    
    def colisions(self, group, kill, name):
        col = pygame.sprite.spritecollide(self, group, kill)
        
        if col and name == "platform":
            self.rect.bottom = col[0].rect.top
        if col and name == "crystal":
            self.colections += 1
        if col and name == "enemy":
            if self.rect.bottom - 10 == col[0].rect.top:
                self.vel *= -1
                col[0].kill()
            else:
                self.rect[0] -= 30
                self.lifes -= 1
                col[0].kill()
    
    def events(self, events):
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_d:
                self.rigth = True
            elif events.key == pygame.K_a:
                self.left = True
            if events.key == pygame.K_SPACE and self.vel == self.max_vel:
                # self.vel *= -1
                self.jump = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_d:
                self.rigth = False
            elif events.key == pygame.K_a:
                self.left = False
    
    def moviments(self):
        if self.rigth:
            self.rect[0] += 8
            self.anim("walk", 4, 4)
            self.direction = False
        elif self.left:
            self.rect[0] -= 8
            self.anim("walk", 4, 4)
            self.direction = True
        else:
            self.anim("idle", 4, 4)
        if self.jump or self.vel < self.max_vel:
            self.anim("jump", 4, 0)
        if self.jump and self.vel == self.max_vel:
            self.vel *= -1
            self.jump = False
        self.image = pygame.transform.flip(self.image, self.direction, False)
    
    def anim(self, name, ticks, limit):
        self.ticks += 1
        if self.ticks >= ticks:
            self.ticks = 0
            self.img_count += 1
        if self.img_count >= limit:
            self.img_count = 0
        
        if limit == 0:
            self.image = pygame.image.load(f"assets/{name}.png")
        else:
            self.image = pygame.image.load(f"assets/{name}{self.img_count}.png")
