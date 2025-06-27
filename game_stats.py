class GameStats:
    """
    A class to store game statistics.
    """
    
    def __init__(self, ai_game):
        """Intialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """
        Intialize statistics that may change during the game.
        """
        self.ships_left = self.settings.ship_limit