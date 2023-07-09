import pygame

from gameObject import GameObject

class Enemy(GameObject):
    def _init_ (self, x, y, width, height, image_path, speed):
        super()._init_(x, y, width, height, image_path)
        
        self.speed = speed
        
    def move(self, max_width):
        if self.x  <= 0:
            self.speed = abs (self.speed)
        elif self.x >= max_width - self.width:
            self.speed = -self.speed
            
        self.x += self.speed