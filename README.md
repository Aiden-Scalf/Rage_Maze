# Rage Maze
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/Aiden-Scalf/Rage_Maze/badge)](https://scorecard.dev/viewer/?uri=github.com/Aiden-Scalf/Rage_Maze)

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/YOUR_ID/badge)](https://www.bestpractices.dev/projects/16244)

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
## Installation
1. Install Python 3.x
2. Install dependencies: `pip install pygame`
3. Clone the repo: `git clone https://github.com/Aiden-Scalf/Rage_Maze.git`

## How to Run
`python main.py`

## How to Play
Guide the cursor through the maze to the goal without touching the walls.
Touching a wall sends you back to the start.

## Controls and Interface
**Input:** trackpad/mouse movement controls the cursor. Press ESC to quit.
**Output:** a game window shows the maze, your cursor, and the current
attempt count. A message appears when you reach the goal.
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

## Running Tests
  `pip install pytest` then run `pytest` from the repo root.
  Linting: `pip install flake8` then `flake8 . --max-line-length=120`.
