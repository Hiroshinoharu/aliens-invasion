import sys
from time import sleep

import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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
        
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        # Intialise the ship 
        self.ship = Ship(self)
        #Intialise the bullet
        self.bullets = pygame.sprite.Group()
        # Intialise the aliens
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        # Start Alein invasion in an active state
        self.game_running = False
        
        # Make a play button
        self.play_button = Button(self, "Play")
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._spawn_alien(current_x, current_y)
                current_x += (2 * alien_width)
            
            # Finshed a Row; resets x values and increments y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _spawn_alien(self, alien_position_x, alien_position_y):
        new_alien = Alien(self)
        new_alien.x = alien_position_x
        new_alien.rect.x = alien_position_x
        new_alien.rect.y = alien_position_y
        self.aliens.add(new_alien)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            
            if self.game_running:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            
            self.clock.tick(60)
            
    def _update_aliens(self):
        """Update the position of the aliens."""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        #   Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
        
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet down and change the direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        self.bullets.update()
            
            # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Checks for any bullets that have hit an alien.
        # If so, get rid of the bullet and the alien.
        collisions  = pygame.sprite.groupcollide(self.bullets, self.aliens,True,True)
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # Increase Levels
            self.stats.level += 1
            self.sb.prep_level()
            
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_running:
            # Reset Game settings
            self.settings.intialize_dynamic_settings()
            
            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            
            # Start the game.
            self.game_running = True
    
    def _update_screen(self):
        """Update the screen with the current game state."""
        self.screen.fill(self.settings.bg_color)
        
        # Run a loop for the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()
        
        # Draw the aliens
        self.aliens.draw(self.screen)
        
        # Draw the score information.
        self.sb.show_score()
        
        # Draw the play button if the game is inactive.
        if not self.game_running:
            self.play_button.draw_button()
        
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
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
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left and update the scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            # Get rid of any reamianing bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            
            # Pause.
            sleep(0.5)
        else:
            self.game_running = False
            pygame.mouse.set_visible(True)  # Show the mouse cursor
    
    def _check_aliens_bottom(self):
        """
        Check if any aliens have reached the bottom of the screen.
        """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

# Run the game if this file is executed directly
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()