from game import FadeIn, FadeOut
from scene import Scene
from renderer import RenderManager
from ui_elements import TextButton, ProcessElements, UpdateElements
import pygame, defaults
from glob import glob



class LevelsScene(Scene):
    def __init__(self, main_surface):
        super().__init__(main_surface)
        self.surface = main_surface
        self.render_manager = RenderManager(main_surface, background_color=(80, 80, 80))


        self.go_back_button = TextButton(main_surface, x=650, y=400, width=100, height=24, text="Back", font_size=12, func=self.go_back)
        self.BUTTONS = [self.go_back_button,]

        all_maps = glob(defaults.ALL_LEVELS_DIR)
        for i, map_path in enumerate(all_maps):
            name = map_path.split(defaults.PATH_SEPERATOR)[1]
            x = 120 * i + 80
            y = 100
            custom_map_button = TextButton(main_surface, x=x-50, y=y, width=100, height=60, text=f"{name}", font_size=12, func=self.open_game, args=[map_path,])
            self.BUTTONS.append(custom_map_button)

        FadeIn(self, 40)


    def process_input(self, events, pressed_keys, mouse_pos):
        ProcessElements(events, pressed_keys, mouse_pos, self.BUTTONS)

    def go_back(self):
        FadeOut(self, 40)
        self.next_scene = defaults.MenuScene(self.surface)

    def open_game(self, map_path):
        FadeOut(self, 40)
        self.next_scene = defaults.GameScene(self.surface, map_path=map_path)
    
    def update(self):
        pass
    
    def render(self):
        self.render_manager.render()
        UpdateElements(self.BUTTONS)
