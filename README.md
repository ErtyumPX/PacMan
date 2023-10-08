# PacMan
 
The good old PacMan game simulated with PyGame.

## License

This project is [MIT](https://github.com/ErtyumPX/SpaceInvaders/blob/main/LICENSE) licensed.

## Setup

The python script 'Game/main.py' is the launcher of the game. After you clone or download the repository, you can run that file.

Beware that used Python version of this project is [3.8.3](https://www.python.org/downloads/release/python-383) and the used Pygame version is [2.0.1](https://www.pygame.org/project/5409/7928).

## Images from the Game

### Game's Itself

<img src="https://github.com/ErtyumPX/PacMan/blob/main/Images/pacman_game.JPG" width=50% height=50%>

### Map Creater for the Game

<img src="https://github.com/ErtyumPX/PacMan/blob/main/Images/pacman_map_creater.JPG" width=50% height=50%>

### SuperBerry that Allowes You to Consume Enemies

<img src="https://github.com/ErtyumPX/PacMan/blob/main/Images/superberry.JPG" width=15% height=15%>


## Algorithms

### Pathfinding

For enemies, they check which square that they could move next is closer to the PacMan by pixels whenever they come to a turning point, and choosing the closest node with a 60 percent of chance. If our little Pacman is on superberry effect and able to consume them, the odds are turned.

### Engine

All the system created and used are also in this repository [PyGameEngine](https://github.com/ErtyumPX/PyGameEngine). It includes scene management system, various scene transitions, render manager, asyncronous character animations and also the UI Elemenets created from scrtach.
