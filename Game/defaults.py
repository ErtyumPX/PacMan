import pygame

FRAME_RATE = 120

WINDOW_NAME = "Pacman"

SIZE = 600, 500
TILE_WIDTH = 20
H_TILES = int(SIZE[0]/TILE_WIDTH)
V_TILES = int(SIZE[1]/TILE_WIDTH)

ACTIVE_COLOR = (255, 120, 120)
OBSTACLE_COLOR = (0, 120, 255)
INACTIVE_COLOR = (160, 160, 160)

BERRY_COLOR = (0, 0, 0)
SUPER_BERRY_COLOR = (204, 0, 255)
ENEMY_COLOR = (0, 0, 0)
PACMAN_COLOR = (255, 255, 0)

CURSOR = pygame.cursors.tri_left

PACMAN_IMAGE = None
ENEMY_IMAGE = None
BLANK_WHITE_IMAGE = pygame.image.load("data/white.jpg")
BLANK_BLACK_IMAGE = pygame.image.load("data/black.jpg")

#MAPS
MAP_ONE = "maps/rectangle"

BLACK_HIGHLIGHT_COLOR = (0, 0, 0, 60)
