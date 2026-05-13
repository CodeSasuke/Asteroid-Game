# Asteroid Game

A simple Pygame asteroid game prototype in development.

## Current Progress

- Basic Pygame window, game loop, and clock are implemented in `main.py`.
- `Player` sprite is implemented in `player.py` using `CircleShape`.
- Sprite groups are created for update/draw handling: `updatable`, `drawable`, and `asteroids`.
- `AsteroidField` is defined in `asteroidfield.py` and handles asteroid spawning.
- `Asteroid` is defined in `asteroid.py` and moves using velocity.
- Debug logging is available through `logger.py`.

## Known Issues / To Fix

- `main.py` currently references `AsteroidField` but does not import it.
- `asteroid.py` contains an invalid self-import: `from asteroid import Asteroid`.
- `Player.containers` and related Pygame sprite-group auto-add logic use `# type: ignore` to suppress type checker warnings.
- Asteroid rendering and collision/game state logic still need completion.

## Next Steps

- Fix imports for `AsteroidField` and `Asteroid`.
- Ensure asteroids are added to the correct sprite groups.
- Add player controls, collisions, and game over handling.
- Improve game visuals and scoring.

## Run

```bash
source .venv/bin/activate
uv run main.py
```
