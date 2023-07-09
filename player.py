import pygame

from gameObject import GameObject

class Player(GameObject):
    def _init_ (self, x, y, width, height, image_path, speed):
        super()._init_(x, y, width, height, image_path)
        
        self.speed = speed
        
    def move(self, direction, max_height):
        if (self.y > max_height - self.height and direction > 0) or (self.y == 0 and direction < 0):
            return
        self.y += (direction * self.speed)