# Rage Maze

> *Without resistance, there is no growth.*

Rage Maze is a small Pygame maze game built to test your patience. Guide **Weenie** through a tight maze to reach the **Ketchup**, but one touch of a wall sends you right back to the start. Loud noises play the whole time, and the goal does not make it easy.

Nowadays it's tempting to quit the moment something gets slightly difficult, or to look for a shortcut. Rage Maze is a love project about doing the opposite: pushing through frustration instead of giving up.

<!-- Add a screenshot or GIF here, e.g. ![Gameplay](screenshot.png) -->

## How It Works

- **Controls:** Move Weenie with your laptop's **trackpad / mouse**.
- **Walls:** Touching a wall (checked with the player's hitbox rect) resets Weenie *and* Ketchup to their starting positions.
- **The goal runs away:** When Weenie gets close to Ketchup, Ketchup **teleports**. This happens **three times**.
- **Winning:** Once Weenie finally collides with Ketchup, movement is locked and the screen reads **"took you long enough."**
- **Audio:** Using `pygame.mixer`, the phrase "loud noises!" loops constantly, and every reset plays "sucks to suck."

## Getting Started

### Requirements

- Python 3
- [Pygame](https://www.pygame.org/)

### Install

```bash
git clone https://github.com/Aiden-Scalf/Rage_Maze.git
cd Rage_Maze
pip install pygame
```

### Run

```bash
python ragemaze_update.py
```

Run it from inside the project folder so the game can find its images, sounds, and maze file. You can also open the project in VS Code or PyCharm and run `ragemaze_update.py` from there.

## Project Structure

| File | Purpose |
| --- | --- |
| `ragemaze_update.py` | Main game script |
| `mazetiles` | Maze layout: a grid of `0`s and `1`s read from a text file |
| `Walls.png` | Wall tile image |
| `Glizzy 40x40.png` | Player sprite (Weenie) |
| `Ketchup 50x50.png` | Goal sprite |
| `Rage Game Background.png` | Background image |
| `loud_noises.wav` | Looping background audio |
| `restart.wav` | Sound played on reset |

## How the Maze Is Built

The maze is stored as a large grid of zeros and ones in the `mazetiles` file. Each cell becomes either open space or a wall tile when the game loads, so you can edit the file to design your own (even meaner) maze.

## Contributing

Ideas welcome: new mazes, more sound effects, difficulty settings, or a timer. Open an issue or submit a pull request.

## Author

Made by [Aiden-Scalf](https://github.com/Aiden-Scalf).
