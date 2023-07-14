import pygame.font

class Scoreboard():
    """making and displaying a scoreboard"""
    def __init__(self, ri_game):
        self.screen = ri_game.screen
        self.screenrect = self.screen.get_rect()
        self.settings = ri_game.settings
        self.stats = ri_game.gamestats
        # font settings
        self.text_color = (255,255,255)
        self.font = pygame.font.Font("planetk.ttf", 35)
        self.bgcolor = (47,47,128)
        self.prep_score()
        self.prep_high_score()
    def prep_score(self):
        """turn score into image"""
        self.score_str = str(self.stats.score)
        self.score_image = self.font.render(self.score_str, True, self.text_color, self.bgcolor)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screenrect.right - 20
        self.score_rect.top = 20
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """turn high score into rendered image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "HIGH SCORE: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.bgcolor)
        # center high score at top of screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screenrect.centerx
        self.high_score_rect.top = self.score_rect.top
    def check_high_score(self):
        """check for new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score() 
    def showscore(self):
        """draw scores to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

