class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game settings"""
        # Screen Settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (31,62,90)
        
        # Ship settings
        self.ship_limit = 3
        
        #Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3 # Limit on the bullets
        
        # Aliens settings
        self.fleet_drop_speed = 10
        
        # How quickly the game sppeds up
        self.speedup_scale = 1.1
        
        # How quickk will the alien point values increase
        self.score_scale = 1.5
        
        self.intialize_dynamic_settings()
        
    def intialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet_direction of 1 represents right ; -1 represents left
        self.fleet_direction = 1
        
        # Scoring settings
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(f"New Alien Points: {self.alien_points}")