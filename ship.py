import pygame

class Ship:
    """
    A class to represent a ship in the game.
    """
    
    def __init__(self, ai_game):
        """
        Initialize the ship and set its starting position.

        Args:
            ai_game (AlienInvasion): The game instance.
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('assets/blueship.bmp')
        self.rect = self.image.get_rect()
        
        # Start a new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)