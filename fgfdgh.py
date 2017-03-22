import pygame

import random

from pygame.locals import*


class Player(pygame.sprite.Sprite):
    
    def__init__(self):
        
        super(Player,self,).__init__()
        
        self.image.load("Untitled-3").convert()
        
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()





        def update(self, pressed_keys):
            
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -1)
                
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 1)
                
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-1, 0)
                
            if pessed_keys[K_RIGHT]:
                self.rect.move_ip(1, 0)






                

            if self.rect < 0:
                self.rect.left = 0

            if self.rect.right > 800:
                self.rect.right = 800

            if self.rect.top < 0:
                self.rect.top = 0

            if self.rect.bottom >600:
                self.rect.bottom = 600


class Opponent(pygame.sprite.Sprite)
