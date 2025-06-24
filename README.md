# 🛸 Alien Invasion Game (Pygame)

This project is a simple 2D game built using Python and Pygame. The game window displays a blank screen and sets the foundation for adding interactive elements like a spaceship and aliens.

## 🚀 Game Structure

### Initialization

- **Modules Used**:  
  - `pygame`: for game graphics and event handling  
  - `sys`: to exit the game cleanly

- **Game Class**: `AlienInvasion`
  - `__init__()`:
    - Initializes Pygame with `pygame.init()`
    - Sets up the game window using `pygame.display.set_mode((1200, 800))`
    - Stores the window surface in `self.screen` for drawing game elements

### Game Loop

- **Method**: `run_game()`
  - Contains a `while` loop that keeps the game running
  - Inside it, a `for` loop (event loop) listens for user input using `pygame.event.get()`
  - If a `QUIT` event is detected (e.g., closing the window), the game exits using `sys.exit()`

### Screen Updates

- `pygame.display.flip()` refreshes the screen on each loop iteration
- This creates smooth animations by redrawing the screen with updated game elements

### Running the Game

At the bottom of the file:

```python
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

## 🚢 Adding the Player's Ship

To display the player's ship in the game, we load an image and draw it using Pygame's `blit()` method.

### 🖼️ Image Setup
- Use a freely licensed image (e.g., from [OpenGamert).
- Preferred format: `.bmp` (loads easily in Pygame).
- Save the image (e.g., `ship.bmp`) in an `images/` folder inside your project directory.

### 🧱 Ship Class Overview

- **Initialization**:
  - The `Ship` class takes a reference to the main `AlienInvasion` instance.
  - Accesses the game screen via `self.screen` and its rectangle via `self.screen_rect`.

- **Loading the Image**:
  - Uses `pygame.image.load()` to load the ship image.
  - Stores the image surface in `self.image`.
  - Gets the image's rectangle with `self.rect = self.image.get_rect()`.

- **Positioning**:
  - The ship is positioned at the bottom center of the screen using:
    ```python
    self.rect.midbottom = self.screen_rect.midbottom

- **Drawing the Ship**:
  - The `blitme()` method draws the ship on the screen at its current position:
    ```python
    self.screen.blit(self.image, self.rect)
    ```

### 📐 Coordinate System Note
- The origin `(0, 0)` is at the top-left of the screen.
- Coordinates increase to the right (x) and downward (y).
- On a 1200×800 screen, the bottom-right corner is `(1200, 800)`.

### 🧠 Why Rectangles?
- Pygame treats all elements as rectangles for efficiency.
- This simplifies positioning and collision detection.

---

## Features

- **Consistent Frame Rate**: Ensures the game runs at the same speed on different systems using Pygame's clock.
- **Custom Background Color**: Sets a light gray background using RGB values.
- **Centralized Settings**: All game settings are stored in a separate `Settings` class for easy management and scalability.

---

## Project Structure

- `alien_invasion.py`: Main game loop and logic.
- `settings.py`: Stores all configurable game settings.

---

## Frame Rate Control

To maintain a consistent frame rate across systems, the game uses Pygame’s `Clock` class. The `tick()` method is called once per loop iteration to limit the frame rate (e.g., 60 FPS). This helps ensure smooth and consistent gameplay regardless of system performance.

---

## Background Color

The game screen is filled with a custom background color using RGB values. For example, `(230, 230, 230)` produces a light gray color. This color is applied during each iteration of the game loop to refresh the screen.

---

## Settings Class

All game settings such as screen dimensions and background color are stored in a dedicated `Settings` class in `settings.py`. This modular approach makes it easier to manage and update settings as the game evolves.

---

## Getting Started

1. Install Pygame using pip.
2. Run the `alien_invasion.py` file to start the game.
3. Modify values in `settings.py` to customize the game’s appearance and behavior.

---
