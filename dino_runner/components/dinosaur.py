import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5
    
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.jump_velocity = self.JUMP_VELOCITY
        self.step_index = 0
        self.running = True
        self.jumping = False
        self.ducking = False
    
    def update(self, user_imput):
        if self.running:
            self.run()       
        elif self.jumping:
            self.jump()
        elif self.ducking:
            self.duck()
        
        if user_imput[pygame.K_UP] and not self.jumping:
            self.jumping = True 
            self.running = False
            self.ducking = False
        elif user_imput[pygame.K_DOWN] and not self.jumping:
            self.jumping = False 
            self.running = False
            self.ducking = True
        elif not self.jumping:
            self.running = True
            
        if self.step_index >= 10:
            self.step_index = 0
    
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.step_index += 1
       
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_rect.y = self.Y_POS
            self.jumping = False
            self.jump_velocity = self.JUMP_VELOCITY    
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1 
         
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))