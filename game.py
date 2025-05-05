from obj import *
import pygame


class Game:
    
    def __init__(self):
        
        self.all_sprites = pygame.sprite.Group() # Grupo contendo todos os sprites a serem desenhados na tela
        self.plataforms = pygame.sprite.Group() # Grupo contendo todos os sprites que são plataformas
        self.crystals = pygame.sprite.Group() # Grupo contendo todos os sprites que são cristais
        self.enemys = pygame.sprite.Group() # Grupo contendo todos os sprites que são inimigos
        
        self.bg = Obj("assets/bg.png", 0, 0, self.all_sprites)
        
        self.tree1 = Obj("assets/tree1.png", 80, 250, self.all_sprites)
        self.tree2 = Obj("assets/tree2.png", 450, 250, self.all_sprites)
        self.tree3 = Obj("assets/tree1.png", 1060, 250, self.all_sprites)
        
        self.plat1 = Obj("assets/plat1.png", 50, 550, self.all_sprites, self.plataforms)
        self.plat2 = Obj("assets/plat3.png", 430, 550, self.all_sprites, self.plataforms)
        self.plat3 = Obj("assets/plat2.png", 1080, 550, self.all_sprites, self.plataforms)
        
        self.crystal1 = Obj("assets/crystal.png", 520, 400, self.all_sprites, self.crystals)
        self.crystal2 = Obj("assets/crystal.png", 870, 400, self.all_sprites, self.crystals)
        self.crystal3 = Obj("assets/crystal.png", 1160, 400, self.all_sprites, self.crystals)
        
        self.enemy1 = Obj("assets/enemy0.png", 520, 501, self.all_sprites)
        
        self.player = Hero("assets/idle0.png", 100, 450, self.all_sprites)
        
        self.hud = Obj("assets/hud.png", 50, 50, self.all_sprites)
        
    def draw(self, window):
        self.all_sprites.draw(window)
    
    def update(self):
        self.all_sprites.update()
        self.player.colisions(self.plataforms, False)
