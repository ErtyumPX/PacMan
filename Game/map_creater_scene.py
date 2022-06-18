from game import FadeIn, FadeOut, CirclerIn
from scene import Scene
from renderer import RenderManager
from ui_elements import TextButton, InputBox, Text, ProcessElements, UpdateElements
import tkinter as tk
from tkinter import filedialog
import pygame, defaults, json

tk.Tk().withdraw()


class MapCreaterScene(Scene):
    def __init__(self, main_surface):
        super().__init__(main_surface)
        self.surface = main_surface
        self.render_manager = RenderManager(main_surface, background_color=(255, 102, 102))

        self.TILES = []
        self.main_pacman_position = None

        self.clear_tiles()

        self.tile_change_status = None

        self.open_button = TextButton(main_surface, x=650, y=40, width=100, height=24, text="Open Map", font_size=12, func=self.open_map)
        self.clear_button = TextButton(main_surface, x=650, y=70, width=100, height=24, text="Clear Map", font_size=12, func=self.clear_tiles)
        self.save_button = TextButton(main_surface, x=650, y=140, width=100, height=24, text="Save Map", font_size=12, func=self.save_map)
        self.go_back_button = TextButton(main_surface, x=650, y=400, width=100, height=24, text="Back", font_size=12, func=self.go_back)
        
        self.name_input = InputBox(main_surface, x=650, y=170, width=100, height=24, default_text="File name...")
        
        self.BUTTONS = [self.clear_button, self.save_button, self.open_button, self.go_back_button]
        self.INPUT_BOXES = [self.name_input, ]
        self.TEXTS = []




       	CirclerIn(self, 20)

    def clear_tiles(self):
	    self.TILES.clear()
	    for _ in range(defaults.H_TILES):
	        column = [2 for _ in range(defaults.V_TILES)]
	        self.TILES.append(column)
	    self.main_pacman_position = None
	    print("Cleared")

    def save_map(self):
	    try:
	        with open(defaults.MAPS_PATH.format(self.name_input.text.replace(" ", "_")), "w") as json_file:
	            json.dump(self.TILES, json_file)
	            print("Saved")
	    except Exception as exp:
	        print(exp)


    def open_map(self):
	    path = filedialog.askopenfilename()
	    try:
	        with open(path) as file:
	            data = json.load(file)
	            if isinstance(data, list):
	                self.TILES = data
	        print(f"Opened {path}")
	        self.name_input.text = path.split("/")[-1]
	    except Exception as exp:
	        print(exp)

    def go_back(self):
	    FadeOut(self, 40)
	    self.next_scene = defaults.MenuScene(self.surface)

    def process_input(self, events, pressed_keys, mouse_pos):

	    mouse_tile_x = mouse_pos[0] // defaults.TILE_WIDTH
	    mouse_tile_y = mouse_pos[1] // defaults.TILE_WIDTH

	    for event in events:
	        if event.type == pygame.MOUSEBUTTONDOWN:
	            if event.button == 1:
	                self.tile_change_status = 1
	            elif event.button == 3:
	                self.tile_change_status = 2
	            elif event.button == 2:
	                self.tile_change_status = 3

	        elif event.type == pygame.MOUSEBUTTONUP:
	            self.tile_change_status = None

	        elif event.type == pygame.KEYDOWN:
	            if -1 < mouse_tile_x < defaults.H_TILES and -1 < mouse_tile_y < defaults.V_TILES:
	                tile_position = [mouse_tile_x * defaults.TILE_WIDTH + defaults.TILE_WIDTH/2, mouse_tile_y * defaults.TILE_WIDTH + defaults.TILE_WIDTH/2]

	                if event.key == pygame.K_SPACE:
	                    if self.main_pacman_position == None:
	                        self.TILES[mouse_tile_x][mouse_tile_y] = 0
	                        self.main_pacman_position = [mouse_tile_x, mouse_tile_y]
	                    elif mouse_tile_x == self.main_pacman_position[0] and mouse_tile_y == self.main_pacman_position[1]:
	                            self.TILES[mouse_tile_x][mouse_tile_y] = 1
	                            self.main_pacman_position = None
	                    else:
	                        self.TILES[self.main_pacman_position[0]][self.main_pacman_position[1]] = 1
	                        self.TILES[mouse_tile_x][mouse_tile_y] = 0
	                        self.main_pacman_position = [mouse_tile_x, mouse_tile_y]
	                
	                elif event.key == pygame.K_f:
	                    if self.TILES[mouse_tile_x][mouse_tile_y] == -1:
	                        self.TILES[mouse_tile_x][mouse_tile_y] = 1
	                    else:
	                        self.TILES[mouse_tile_x][mouse_tile_y] = -1
	                        if self.main_pacman_position != None:
	                            if mouse_tile_x == self.main_pacman_position[0] and mouse_tile_y == self.main_pacman_position[1]:
	                                    self.main_pacman_position = None

	                elif event.key == pygame.K_e:
	                    if self.TILES[mouse_tile_x][mouse_tile_y] == -2:
	                        self.TILES[mouse_tile_x][mouse_tile_y] = 1
	                    else:
	                        self.TILES[mouse_tile_x][mouse_tile_y] = -2
	                        if self.main_pacman_position != None:
	                            if mouse_tile_x == self.main_pacman_position[0] and mouse_tile_y == self.main_pacman_position[1]:
	                                    self.main_pacman_position = None


	        elif event.type == pygame.KEYUP:
	            self.tile_change_status = None


	    if -1 < mouse_tile_x < defaults.H_TILES and -1 < mouse_tile_y < defaults.V_TILES:
	        if self.tile_change_status == 1:
	            self.TILES[mouse_tile_x][mouse_tile_y] = 1
	        elif self.tile_change_status == 2:
	            self.TILES[mouse_tile_x][mouse_tile_y] = 2
	        elif self.tile_change_status == 3:
	            self.TILES[mouse_tile_x][mouse_tile_y] = 3


	    pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
	    for x in range(defaults.H_TILES):
	        pos[0] += defaults.TILE_WIDTH
	        for y in range(defaults.V_TILES):
	            tile = self.TILES[x][y]
	            color = (0, 0, 0)
	            if tile == 1 or tile == 0 or tile == -1 or tile == -2: color = defaults.ACTIVE_COLOR
	            elif tile == 2: color = defaults.OBSTACLE_COLOR
	            elif tile == 3: color = defaults.INACTIVE_COLOR
	            pygame.draw.rect(self.surface, color, pos)

	            pos_middle = [pos[0] + defaults.TILE_WIDTH / 2, pos[1] + defaults.TILE_WIDTH / 2]
	            if tile == -1:
	                pygame.draw.circle(self.surface, 0, pos_middle, 6)
	                pygame.draw.circle(self.surface, defaults.SUPER_BERRY_COLOR, pos_middle, 5)
	            elif tile == -2:
	                pygame.draw.circle(self.surface, defaults.ENEMY_COLOR, pos_middle, 7)
	            elif tile == 0:
	                pygame.draw.circle(self.surface, (255, 255, 0), pos_middle, 7)

	            pos[1] += defaults.TILE_WIDTH
	        pos[1] = 0

	    pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
	    for x in range(defaults.H_TILES):
	        pos[0] += defaults.TILE_WIDTH
	        for y in range(defaults.V_TILES):
	            pygame.draw.rect(self.surface, (255, 255, 255), pos, 1)
	            pos[1] += defaults.TILE_WIDTH
	        pos[1] = 0

	    ProcessElements(events, pressed_keys, mouse_pos, self.BUTTONS, self.INPUT_BOXES, self.TEXTS)

    def update(self):
	    pass
    
    def render(self):
	    self.render_manager.render()

	    pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
	    for x in range(defaults.H_TILES):
	        pos[0] += defaults.TILE_WIDTH
	        for y in range(defaults.V_TILES):
	            tile = self.TILES[x][y]
	            color = (0, 0, 0)
	            if tile == 1 or tile == 0 or tile == -1 or tile == -2: color = defaults.ACTIVE_COLOR
	            elif tile == 2: color = defaults.OBSTACLE_COLOR
	            elif tile == 3: color = defaults.INACTIVE_COLOR
	            pygame.draw.rect(self.surface, color, pos)

	            pos_middle = [pos[0] + defaults.TILE_WIDTH / 2, pos[1] + defaults.TILE_WIDTH / 2]
	            if tile == -1:
	                pygame.draw.circle(self.surface, 0, pos_middle, 6)
	                pygame.draw.circle(self.surface, defaults.SUPER_BERRY_COLOR, pos_middle, 5)
	            elif tile == -2:
	                pygame.draw.circle(self.surface, defaults.ENEMY_COLOR, pos_middle, 7)
	            elif tile == 0:
	                pygame.draw.circle(self.surface, (255, 255, 0), pos_middle, 7)

	            pos[1] += defaults.TILE_WIDTH
	        pos[1] = 0

	    pos = [-defaults.TILE_WIDTH, 0, defaults.TILE_WIDTH, defaults.TILE_WIDTH]
	    for x in range(defaults.H_TILES):
	        pos[0] += defaults.TILE_WIDTH
	        for y in range(defaults.V_TILES):
	            pygame.draw.rect(self.surface, (255, 255, 255), pos, 1)
	            pos[1] += defaults.TILE_WIDTH
	        pos[1] = 0

	    UpdateElements(self.BUTTONS, self.INPUT_BOXES, self.TEXTS)
