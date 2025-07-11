import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    A class to represent a bullet fired from the ship.

    Args:
        Sprite (class): This is the sprite which is the base class for all the sprites in Pygame.
    """
    
    def __init__(self, ai_game):
        """
        Create a bullet object at the ship's current position.
        
        Args:
            ai_game (class):This is the class which contains all the game related variables and methods.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a float
        self.y = float(self.rect.y)
        
    def update(self):
        """ Move the bullet up the screen"""
        # Update the bullet's position based on the speed
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)