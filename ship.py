import pygame
from settings import Settings
class SimbaShip:
    """"class managing the ship"""
    def __init__(self, ri_game):
        """initializing the ship + its starting position"""
        self.screen = ri_game.screen
        self.screen_rect = ri_game.screen.get_rect()
        # ship settings
        self.settings = Settings()
        self.speed = self.settings.ship_speed
        # load ship and get its rect
        self.image = pygame.image.load('ship_simba.bmp')
        self.rect = self.image.get_rect()
        # start the ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom
        # movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """update ship position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.speed 
    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        