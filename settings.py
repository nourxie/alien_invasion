class Settings:
    """storing settings for Ryan Invasion"""
    def __init__(self):
        """initialize game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_image = ("background_image_tt.bmp")
        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (57,255,20)
        self.bullets_allowed = 10 
        # alien settings
        self.alien_direction = 1 #-1 is left, 1 is right
        # initalize dynamic settings
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """settings that change as the game progresses"""
        # ship settings
        self.ship_speed = 4
        self.shiplives_limit = 2     
        # Bullet settings
        self.bullet_speed = 6.0
        # alien settings
        self.alien_y_drop = 5
        self.alien_speed = 0.7
        self.alien_amt = 5 # how far aliens are from the bottom of the sceen at start
   


