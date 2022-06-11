import pygame

FRAME_RATE = 120

WINDOW_NAME = "Pacman"

SIZE = 600, 500
TILE_WIDTH = 20
H_TILES = int(SIZE[0]/TILE_WIDTH)
V_TILES = int(SIZE[1]/TILE_WIDTH)

ACTIVE_COLOR = (255, 90, 90)
OBSTACLE_COLOR = (0, 153, 255)
INACTIVE_COLOR = (160, 160, 160)

CURSOR = pygame.cursors.tri_left

PACMAN_IMAGE = None
ENEMY_IMAGE = None
BLANK_WHITE_IMAGE = pygame.image.load("data/white.jpg")
BLANK_BLACK_IMAGE = pygame.image.load("data/black.jpg")

BLACK_HIGHLIGHT_COLOR = (0,0,0,60)
