# Asteroid Game

A Pygame-based asteroid shooter game built as a learning project. The player controls a ship to destroy asteroids while managing lives and score.

## Current Progress

✅ **Completed:**
- Basic Pygame window, game loop, and clock implemented in `main.py`
- `Player` sprite with rotation and movement (WASD controls) in `player.py`
- `CircleShape` base class for physics-based objects in `circleshape.py`
- `Asteroid` sprite that moves with velocity in `asteroid.py`
- `AsteroidField` spawner that generates asteroids periodically in `asteroidfield.py`
- `Shot` projectile class with velocity in `shot.py`
- Sprite groups for organizing and updating game objects
- Debug logging system in `logger.py`
- Constants configuration in `constants.py`

## Known Issues / To Fix

- Missing imports: `AsteroidField` and `Asteroid` not imported in `main.py`
- `asteroid.py` has incorrect random import (should be `from random import uniform` or `import random`)
- `Shot` class needs `velocity` initialization in `__init__`
- Collision detection not yet implemented
- Game state management (win/loss conditions) not implemented
- Asteroid splitting logic incomplete in `split()` method
- Player shooting not wired to game loop

## Next Steps (Priority Order)

1. Fix imports and initialize missing attributes
2. Implement collision detection (player/asteroid, shot/asteroid)
3. Wire up player shooting (space key) to game loop
4. Complete asteroid splitting logic on collision
5. Add game over and win conditions

## Upcoming Features

- [ ] Add a scoring system
- [ ] Implement multiple lives and respawning
- [ ] Add an explosion effect for the asteroids
- [ ] Add acceleration to the player movement
- [ ] Make the objects wrap around the screen instead of disappearing
- [ ] Add a background image
- [ ] Create different weapon types
- [ ] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped

## Getting Started

### Requirements
- Python 3.8+
- Pygame
- UV (package manager)

### Installation

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies (if needed)
uv pip install pygame
```

### Run the Game

```bash
uv run main.py
```

### Controls

- **A** – Rotate left
- **D** – Rotate right
- **W** – Move forward
- **S** – Move backward
- **Space** – Shoot (not yet implemented)

## Project Structure

```
├── main.py              # Game loop and initialization
├── player.py            # Player ship sprite and controls
├── asteroid.py          # Asteroid sprite and splitting logic
├── asteroidfield.py     # Asteroid spawner
├── shot.py              # Projectile sprite
├── circleshape.py       # Base class for physics objects
├── constants.py         # Game configuration (screen size, speeds, etc.)
├── logger.py            # Debug logging system
├── pyproject.toml       # Project metadata and dependencies
└── README.md            # This file
```

## Development Notes

- Uses Pygame sprite groups for efficient updating and rendering
- `CircleShape` provides position, velocity, and collision radius base functionality
- All sprites are automatically added to groups using the `containers` class attribute pattern
