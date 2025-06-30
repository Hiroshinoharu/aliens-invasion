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

# Bullet Class Overview – Alien Invasion (Pygame)

This document explains the purpose and structure of the `Bullet` class in the Alien Invasion game, focusing on how it integrates with Pygame's sprite system and interacts with the ship.

---

## Purpose

The `Bullet` class represents projectiles fired by the player's ship. It inherits from `pygame.sprite.Sprite`, allowing bullets to be managed in groups and updated collectively.

---

## Key Concepts

### 1. Inheriting from Sprite

- The class inherits from `pygame.sprite.Sprite`.
- This enables grouping and batch operations on bullets (e.g., updating, drawing, collision detection).

### 2. Initialization

- The `__init__()` method requires the current instance of `AlienInvasion`.
- `super()` is used to properly initialize the Sprite base class.
- Attributes are set for:
  - `screen`
  - `settings`
  - `color`

---

## Bullet Rect Creation

### ❶ Creating the Rect

- Since the bullet is not image-based, a `pygame.Rect()` is created manually.
- Initialized at `(0, 0)` with width and height from `self.settings`.
- The rect is then repositioned based on the ship’s current location.

### ❷ Aligning with the Ship

- The bullet’s `midtop` is set to match the ship’s `midtop`.
- This ensures bullets appear to fire from the top center of the ship.

---

## Movement and Precision

### ❸ Using Float for Y-Coordinate

- The bullet’s vertical position (`y`) is stored as a float.
- This allows for smoother and more precise movement, especially at higher speeds.

---

---

## Goal

To draw a fleet of aliens across the top of the screen, adding aliens until there’s no space left for a new alien. This process is repeated as long as there is enough vertical space to add a new row.

---

## Creating a Row of Aliens

To generate a full row of aliens, we first create a single alien to access its width. We then place an alien on the left side of the screen and keep adding aliens until we run out of space.

---

## Calculating Spacing

1. **Alien Width**: We get the alien’s width from the first alien created.
2. **Initial Position**: Define a variable `current_x` to refer to the horizontal position of the next alien. Initially set to one alien width to offset the first alien from the left edge.

---

## Loop Logic for Placing Aliens

1. **While Loop**: Continue adding aliens while there’s enough room to place one.
2. **Condition**: Compare `current_x` to a maximum value to determine if there’s room for another alien.
3. **Creating Aliens**:
   - Create an alien at the correct position.
   - Define the horizontal position of the next alien.
4. **Positioning**:
   - Set the precise horizontal position to the current value of `current_x`.
   - Position the alien’s rect at this x-value.
   - Add the new alien to the group `self.aliens`.
5. **Increment**: Increment `current_x` by two alien widths to move past the alien just added and leave space between aliens.