import pygame

class GameObject:
    
    def _init_(self, x, y, width, height, image_path):
        image = pygame.image.load(image_path)
        self.image - pygame.transform.scale(image, (width,height))
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height