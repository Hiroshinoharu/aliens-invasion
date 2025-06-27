class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game settings"""
        # Screen Settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (31,62,90)
        
        # Ship settings
        self.ship_speed = 2.0
        self.ship_limit = 3
        
        #Bullet Settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3 # Limit on the bullets
        
        # Aliens settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        
        # fleet_direction of 1 represents right ; -1 represents left
        self.fleet_direction = 1