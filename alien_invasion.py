import sys
import pygame

class AlienInvasion:
    """
    This class manages the game resources and behavior.
    """
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800)) # Set the screen size
        pygame.display.set_caption("Alien Invasion")  # Set the window title
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()