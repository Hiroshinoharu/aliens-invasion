import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    A class to represent an alien in the game.
    Args:
        Sprite (class): The class where it'll inherit all the traits in the alien
    """
    
    def __init__(self,ai_game):
        """
        Intialises the alien and sets its starting position.
        Args:
            ai_game (class): Class where all game behaviours are stored in as a class
        """
        super().__init__()
        self.screen = ai_game.screen
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('assets/ufo.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact horizonatal position
        self.x = float(self.rect.x)