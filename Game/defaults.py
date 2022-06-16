import pygame

#All Scenes
from menu_scene import MenuScene
from game_scene import GameScene
from map_creater_scene import MapCreaterScene
from custom_map_scene import CustomMapScene
from levels_scene import LevelsScene

FRAME_RATE = 120

WINDOW_NAME = "PacMan"

SIZE = 800, 500
GAME_SIZE = 600, 500
TILE_WIDTH = 20
H_TILES = int(GAME_SIZE[0]/TILE_WIDTH)
V_TILES = int(GAME_SIZE[1]/TILE_WIDTH)

ACTIVE_COLOR = (255, 120, 120)
OBSTACLE_COLOR = (0, 120, 255)
INACTIVE_COLOR = (160, 160, 160)

BERRY_COLOR = (0, 0, 0)
SUPER_BERRY_COLOR = (204, 0, 255)

PACMAN_COLOR = (255, 255, 0)

ENEMY_COLOR = (0, 0, 0)
ENEMY_BLINKING_COLOR = (100, 100, 100)
ENEMY_VULNERABLE_COLOR = (200, 0, 200)

ENEMY_BLINK_TIME = 6

CURSOR = pygame.cursors.tri_left

PACMAN_IMAGE = None
ENEMY_IMAGE = None
BLANK_WHITE_IMAGE = pygame.image.load("data/white.jpg")
BLANK_BLACK_IMAGE = pygame.image.load("data/black.jpg")

MAPS_PATH = "custom_maps/{0}"
CUSTOM_MAPS_DIR = "custom_maps/*"
#MAPS
ALL_LEVELS_DIR = "maps/*"

BLACK_HIGHLIGHT_COLOR = (0, 0, 0, 60)
