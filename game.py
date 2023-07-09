import pygame

from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:
    def _init_(self):

        self.width = 800
        self.height = 800
        self.white_colour = (255,255,255) 

        self.game_window = pygame.display.set_mode((self.width,self.height))

        self.clock = pygame.time.Clock()

        self.background = GameObject (0,0, self.width, self.height, 'assets/background.png')
        self.treasure = GameObject(320,30,50,50, 'assets/treasure.png')
        self.player = Player (320,450,50,50, 'assets/player.png', 10)
        self.enemy = Enemy (100.390,50,50, 'assets/enemy.png', 10)
        
    def draw_objects(self):
        
        self.game_window.fill(self.white_colour)
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        self.game_window.blit(self.enemy.image, (self.enemy.x, self.enemy.y))
        
        pygame.display.update()

    def run_game_loop(self):
        while True:
        
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
                        
            self.player.move(player_direction, self.height)
            self.enemy.move(self.width)

                    
            self.draw_objects()
            
            self.clock.tick(60)
        
        