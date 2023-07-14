import pygame
from pygame.sprite import Sprite
from settings import Settings
import random
class Alien(Sprite):
    """represents a single alien in the fleet"""
    def __init__(self, ri_game):
        """initialize the alien + its start position"""
        super().__init__()
        # initializing alien
        self.screen = ri_game.screen
        self.settings = Settings()
        # randomizing between rayan e and ryan b
        self.ryanb = pygame.image.load('ryanbalien.bmp')
        self.rayane = pygame.image.load('ryanealien.bmp')
        self.images = [self.rayane, self.ryanb]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
    
        # starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # horizontal position
        self.x = float(self.rect.x)

        

