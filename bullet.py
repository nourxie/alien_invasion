import pygame
from pygame.sprite import Sprite
from settings import Settings
class Bullet(Sprite):
    """class managing bullets fired from the ship"""
    def __init__(self, ri_game):
        """create bullet object at ship's current position"""
        super().__init__()
        self.screen = ri_game.screen
        self.settings = Settings()
        self.color = self.settings.bullet_color
        # create a bullet rect at 0,0 and set correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ri_game.ship.rect.midtop

        # store bullet position as a float
        self.y = float(self.rect.y)
    def draw_bullet(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y