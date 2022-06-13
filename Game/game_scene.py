from scene import Scene
from game import HorizontalSlidingIn, HorizontalSlidingOut
from renderer import RenderManager
import pygame, defaults, json
from pacman import Pacman
from enemy import Enemy
from berry import Berry
from super_berry import SuperBerry
from random import randint
from math import floor, ceil

vel_add = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}

class GameScene(Scene):
    def __init__(self, main_surface:pygame.Surface, map_path:str="maps/rectangle"):
        super().__init__(main_surface)

        self.TILES = None
        self.create_map(map_path)

        self.surface = main_surface
        self.render_manager = RenderManager(main_surface)
           
        self.enemies = []

        self.collected_berry = 0
        self.berries = []
        self.super_berries = []
        self.berry_amount = 0

        self.spawn_position = None

        for x in range(defaults.H_TILES):
            for y in range(defaults.V_TILES):

                if self.TILES[x][y] == 1:
                    self.berry_amount += 1
                    new_berry = Berry(main_surface, x=x, y=y)
                    self.render_manager.add(new_berry, layer=1)
                    self.berries.append(new_berry)

                elif self.TILES[x][y] == -1:
                    self.berry_amount += 1
                    new_super_berry = SuperBerry(main_surface, x=x, y=y)
                    self.super_berries.append(new_super_berry)
                    self.render_manager.add(new_super_berry, layer=1)
                    self.TILES[x][y] = 1

                elif self.TILES[x][y] == -2:
                    new_enemy = Enemy(main_surface, x=x, y=y, vel=randint(1, 4))
                    self.enemies.append(new_enemy)
                    self.render_manager.add(new_enemy, layer=3)
                    self.TILES[x][y] = 1


                elif self.TILES[x][y] == 0:
                    self.pacman = Pacman(main_surface, x=x, y=y, life=1)
                    self.render_manager.add(self.pacman,layer=2)
                    self.spawn_position = [x, y]
                    self.TILES[x][y] = 1

        HorizontalSlidingIn(self, 60)

    def create_map(self, path:str):
        with open(path) as file:
            data = json.load(file)
            if isinstance(data, list):
                self.TILES = data

    def process_input(self, events, pressed_keys, mouse_pos):
        if (pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]) and self.TILES[floor(self.pacman.transform.x)][floor(self.pacman.transform.y - 1)] == 1:
            self.pacman.velocity = 1
        if (pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]) and self.TILES[floor(self.pacman.transform.x + 1)][floor(self.pacman.transform.y)] == 1:
            self.pacman.velocity = 2
        if (pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]) and self.TILES[floor(self.pacman.transform.x)][floor(self.pacman.transform.y + 1)] == 1:
            self.pacman.velocity = 3
        if (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]) and self.TILES[floor(self.pacman.transform.x - 1)][floor(self.pacman.transform.y)] == 1:
            self.pacman.velocity = 4

    def check_if_died(self):
        for enemy in self.enemies:
            if floor(self.pacman.transform.x) == floor(enemy.transform.x) and \
                    floor(self.pacman.transform.y) == floor(enemy.transform.y):
                self.pacman.life -= 1
                print(self.pacman.life)
                if self.pacman.life > 0:
                    self.render_manager.remove(self.pacman)
                    self.pacman = Pacman(self.surface, x=self.spawn_position[0], y=self.spawn_position[1], life=self.pacman.life)
                    self.render_manager.add(self.pacman)
                else:
                    print("You Died!")
                    HorizontalSlidingOut(self, 60)
                    self.next_scene = GameScene(self.surface)

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
        if self.berry_amount == self.collected_berry:
            print("You Won!")

    def update(self):
        self.pacman.move(self.TILES)
        for enemy in self.enemies:
            enemy.move(self.TILES)
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
                tile = self.TILES[x][y]
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
