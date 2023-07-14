from settings import Settings
class GameStats():
    """tracking statistics of alien invasion"""
    def __init__(self):
        """Initialize statistics."""
        self.ri_settings = Settings()
        self.reset_stats()
        # start the game inactive
        self.game_active = False
        # highscore shouldnt get reset
        self.high_score = self.load_highscore('highscore.txt')
    def reset_stats(self):
        """initialize statistics that get reset during game"""
        self.lives_left = self.ri_settings.shiplives_limit
        self.score = 0
        self.level = 1      
    def load_highscore(self, filename):
        try: 
            with open(filename, "r") as file:
                return int(file.read())
        except FileNotFoundError:
                print("file not ofound")
  
