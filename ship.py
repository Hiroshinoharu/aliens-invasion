import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """
    A class to represent a ship in the game.
    """
    
    def __init__(self, ai_game):
        """
        Initialize the ship and set its starting position.

        Args:
            ai_game (AlienInvasion): The game instance.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('assets/blueship.bmp')
        self.rect = self.image.get_rect()
        
        # Start a new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """ Update the ship's position based on the movement flags."""
        # Update the ship's position based on the movement flags not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        # Update rect object from self.x and self.y.
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)