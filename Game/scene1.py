from scene import Scene
from game import HorizontalSlidingIn
from renderer import RenderManager
import pygame, defaults, json
from pacman import Pacman
from enemy import Enemy
from berry import Berry
from random import randint
from math import floor, ceil

vel_add = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
path = "maps/main_map"

with open(path) as file:
    data = json.load(file)
    if isinstance(data, list):
        TILES = data


class Scene1(Scene):
    def __init__(self, main_surface):
        super().__init__(main_surface)
        self.surface = main_surface
        self.render_manager = RenderManager(main_surface)

        self.pacman = Pacman(main_surface, x=14, y=13)
        self.life = 3

        self.enemy1 = Enemy(main_surface, x=4, y=2, vel=randint(1, 4))
        self.enemy2 = Enemy(main_surface, x=25, y=2, vel=randint(1, 4))
        self.enemy3 = Enemy(main_surface, x=4, y=23, vel=randint(1, 4))
        self.enemy4 = Enemy(main_surface, x=25, y=23, vel=randint(1, 4))
        self.enemies = [self.enemy1, self.enemy2, self.enemy3, self.enemy4]
        self.render_manager.add(self.pacman, self.enemy1, self.enemy2, self.enemy3, self.enemy4)

        self.collected_berry = 0
        self.berries = []
        self.MOVABLE_TILES = 0
        for x in range(defaults.H_TILES):
            for y in range(defaults.V_TILES):
                if TILES[x][y] == 1:
                    self.MOVABLE_TILES += 1
                    new_berry = Berry(main_surface, x=x, y=y)
                    self.render_manager.add(new_berry)
                    self.berries.append(new_berry)

        HorizontalSlidingIn(self, 40)

    def process_input(self, events, pressed_keys, mouse_pos):
        if (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]) and TILES[floor(self.pacman.transform.x)][floor(self.pacman.transform.y - 1)] == 1:
            self.pacman.velocity = 1
        if (pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]) and TILES[floor(self.pacman.transform.x + 1)][floor(self.pacman.transform.y)] == 1:
            self.pacman.velocity = 2
        if (pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]) and TILES[floor(self.pacman.transform.x)][floor(self.pacman.transform.y + 1)] == 1:
            self.pacman.velocity = 3
        if (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]) and TILES[floor(self.pacman.transform.x - 1)][floor(self.pacman.transform.y)] == 1:
            self.pacman.velocity = 4

    def check_if_died(self):
        for enemy in self.enemies:
            if floor(self.pacman.transform.x) == floor(enemy.transform.x) and \
                    floor(self.pacman.transform.y) == floor(enemy.transform.y):
                self.life -= 1
                if self.life > 0:
                    self.render_manager.remove(self.pacman)
                    self.pacman = Pacman(self.surface, x=14, y=13)
                    self.render_manager.add(self.pacman)
                else:
                    print("You Died!")


    def eat_berry(self):
        for berry in self.berries:
            if not berry.is_taken:
                if berry.transform.x == floor(self.pacman.transform.x) and berry.transform.y == floor(self.pacman.transform.y):
                    self.collected_berry += 1
                    berry.is_taken = True
                elif berry.transform.x == ceil(self.pacman.transform.x) and berry.transform.y == ceil(self.pacman.transform.y):
                    self.collected_berry += 1
                    berry.is_taken = True

    def check_if_won(self):
        if self.MOVABLE_TILES == self.collected_berry:
            print("You Won!")

    def update(self):
        self.pacman.move(TILES)
        for enemy in self.enemies:
            enemy.move(TILES)
        self.check_if_died()
        self.eat_berry()
        self.check_if_won()

    def render(self):
        """
        pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
        for x in range(defaults.H_TILES):
            pos[0] += defaults.TILE_WIDTH
            for y in range(defaults.V_TILES):
                pygame.draw.rect(self.surface, (255,255,255), pos, 1)
                pos[1] += defaults.TILE_WIDTH
            pos[1] = 0
        """
        pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
        for x in range(defaults.H_TILES):
            pos[0] += defaults.TILE_WIDTH
            for y in range(defaults.V_TILES):
                tile = TILES[x][y]
                color = (0, 0, 0)
                if tile == 1:
                    color = defaults.ACTIVE_COLOR
                elif tile == 2:
                    color = defaults.OBSTACLE_COLOR
                elif tile == 3:
                    color = defaults.INACTIVE_COLOR
                pygame.draw.rect(self.surface, color, pos)
                pos[1] += defaults.TILE_WIDTH
            pos[1] = 0

        pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
        for x in range(defaults.H_TILES):
            pos[0] += defaults.TILE_WIDTH
            for y in range(defaults.V_TILES):
                pygame.draw.rect(self.surface, (255, 255, 255), pos, 1)
                pos[1] += defaults.TILE_WIDTH
            pos[1] = 0

        self.render_manager.render()
