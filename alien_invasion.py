import sys
import pygame
from ship import Ship
from settings import Settings

class AlienInvasion:
    """
    This class manages the game resources and behavior.
    """
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        # Set up some constants
        self.clock = pygame.time.Clock() # Sets up a clock to control the frame rate, limiting the game loop to 60 FPS in the run_game method
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # Set the screen size
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")  # Set the window title
        
        # Intialise the ship 
        self.ship = Ship(self)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Move the ship based on user input
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Check for key releases
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _update_screen(self):
        """Update the screen with the current game state."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()
        
    def _check_keydown_events(self,event):
        """Check for key presses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self,event):
        """Check for key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

# Run the game if this file is executed directly
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()