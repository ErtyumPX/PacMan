import pygame
import defaults
import json
import tkinter as tk
from tkinter import filedialog
from ui_elements import TextButton, InputBox, Text, ProcessElements, UpdateElements

pygame.init()
tk.Tk().withdraw()

SIZE = X, Y = 700, 500
UI_SIZE = UI_X, UI_Y = 100, 0
TILE_WIDTH = 20
H_TILES = int(SIZE[0]/TILE_WIDTH)
V_TILES = int(SIZE[1]/TILE_WIDTH)

maps_path = "maps/{0}"

pygame.display.set_caption("Map Creater")
surface = pygame.display.set_mode((SIZE[0]+UI_SIZE[0], SIZE[1]+UI_SIZE[1]))
clock = pygame.time.Clock()

# TILE STATUS:   1: ACTIVE, 2: BORDER, 3: INACTIVE
TILES = []
def clear_tiles():
    TILES.clear()
    for _ in range(H_TILES):
        column = [2 for _ in range(V_TILES)]
        TILES.append(column)
    global SUPER_BERRIES, main_pacman_position
    for super_berry in SUPER_BERRIES:
        del super_berry
    SUPER_BERRIES = []
    main_pacman_position = [-1, -1]
    print("Cleared")


def save_func():
    try:
        with open(maps_path.format(name_input.text), "w") as json_file:
            json.dump(TILES, json_file)
            print("Saved")
    except Exception as exp:
        print(exp)


def open_func():
    global TILES
    path = filedialog.askopenfilename()
    try:
        with open(path) as file:
            data = json.load(file)
            if isinstance(data, list):
                TILES = data
        print(f"Opened {path}")
    except Exception as exp:
        print(exp)

SUPER_BERRIES = []
main_pacman_position = [-1, -1]

clear_tiles()

tile_change_status = None

#button_image = pygame.transform.scale(pygame.image.load("data/white.jpg"), (60,20))
open_button = TextButton(surface, x=650, y=40, width=100, height=24, text="Open Map", font_size=12, func=open_func)
clear_button = TextButton(surface, x=650, y=70, width=100, height=24, text="Clear Map", font_size=12, func=clear_tiles)
save_button = TextButton(surface, x=650, y=140, width=100, height=24, text="Save Map", font_size=12, func=save_func)
name_input = InputBox(surface, x=650, y=170, width=100, height=24, default_text="File name...")
BUTTONS = [clear_button, save_button, open_button]
INPUT_BOXES = [name_input, ]
TEXTS = []




main = True
while main:
    clock.tick(120)
    surface.fill((255, 102, 102))
    EVENTS = pygame.event.get()
    PRESSED_KEYS = pygame.key.get_pressed()

    mouse_pos = pygame.mouse.get_pos()
    mouse_tile_x = mouse_pos[0] // TILE_WIDTH
    mouse_tile_y = mouse_pos[1] // TILE_WIDTH

    for event in EVENTS:
        if event.type == pygame.QUIT:
            main = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                tile_change_status = 1
            elif event.button == 3:
                tile_change_status = 2
            elif event.button == 2:
                tile_change_status = 3

        elif event.type == pygame.MOUSEBUTTONUP:
            tile_change_status = None

        elif event.type == pygame.KEYDOWN:
            if -1 < mouse_tile_x < H_TILES and -1 < mouse_tile_y < V_TILES:
                tile_position = [mouse_tile_x * TILE_WIDTH + TILE_WIDTH/2, mouse_tile_y * TILE_WIDTH + TILE_WIDTH/2]

                if event.key == pygame.K_SPACE:
                    if main_pacman_position == tile_position:
                        main_pacman_position = [-1, -1]
                    else:
                        TILES[mouse_tile_x][mouse_tile_y] = 0
                        main_pacman_position = tile_position 
                
                elif event.key == pygame.K_f:
                    if tile_position in SUPER_BERRIES:
                        SUPER_BERRIES.remove(tile_position)
                    else:
                        SUPER_BERRIES.append(tile_position)
                        TILES[mouse_tile_x][mouse_tile_y] = -1

        elif event.type == pygame.KEYUP:
            tile_change_status = None


    if -1 < mouse_tile_x < H_TILES and -1 < mouse_tile_y < V_TILES:
        if tile_change_status == 1:
            TILES[mouse_tile_x][mouse_tile_y] = 1
        elif tile_change_status == 2:
            TILES[mouse_tile_x][mouse_tile_y] = 2
        elif tile_change_status == 3:
            TILES[mouse_tile_x][mouse_tile_y] = 3


    pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
    for x in range(defaults.H_TILES):
        pos[0] += defaults.TILE_WIDTH
        for y in range(defaults.V_TILES):
            tile = TILES[x][y]
            color = (0, 0, 0)
            if tile == 1 or tile == 0 or tile == -1: color = defaults.ACTIVE_COLOR
            elif tile == 2: color = defaults.OBSTACLE_COLOR
            elif tile == 3: color = defaults.INACTIVE_COLOR
            pygame.draw.rect(surface, color, pos)
            pos[1] += defaults.TILE_WIDTH
        pos[1] = 0

    pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
    for x in range(defaults.H_TILES):
        pos[0] += defaults.TILE_WIDTH
        for y in range(defaults.V_TILES):
            pygame.draw.rect(surface, (255, 255, 255), pos, 1)
            pos[1] += defaults.TILE_WIDTH
        pos[1] = 0

    ProcessElements(EVENTS, PRESSED_KEYS, mouse_pos, BUTTONS, INPUT_BOXES, TEXTS)
    UpdateElements(BUTTONS, INPUT_BOXES, TEXTS)
    for berry_position in SUPER_BERRIES:
        pygame.draw.circle(surface, (0, 0, 0), berry_position, 5)
    pygame.draw.circle(surface, (255, 255, 0), main_pacman_position, 7)
    pygame.display.update()

pygame.quit()
