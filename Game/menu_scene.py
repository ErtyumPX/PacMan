from game import FadeIn, FadeOut, SquareOut, CirclerOut, HorizontalSlidingOut
from scene import Scene
from renderer import RenderManager
from ui_elements import TextButton, ProcessElements
import pygame, defaults



class MenuScene(Scene):
    def __init__(self, main_surface):
        super().__init__(main_surface)
        self.surface = main_surface
        self.render_manager = RenderManager(main_surface, background_color=(80, 80, 80))

        play_button = TextButton(main_surface, x=defaults.SIZE[0]/2-50, y=240, width=100, height=40, text="PLAY", func=self.play, color=(255,0,0))
        custom_maps_button = TextButton(main_surface, x=defaults.SIZE[0]/2-80, y=300, width=160, height=40, text="CUSTOM MAPS", func=self.custom_maps, color=(255,0,0))
        map_creater_button = TextButton(main_surface, x=defaults.SIZE[0]/2-85, y=360, width=170, height=40, text="MAP CREATER", func=self.go_to_map_creater, color=(255,0,0))
        self.BUTTONS = [play_button, custom_maps_button, map_creater_button]

        self.render_manager.add_all(self.BUTTONS)


        FadeIn(self, 40)


    def process_input(self, events, pressed_keys, mouse_pos):
        ProcessElements(events, pressed_keys, mouse_pos, self.BUTTONS)

    def play(self):
        CirclerOut(self, 30, pygame.mouse.get_pos())
        self.next_scene = defaults.LevelsScene(self.surface)

    def custom_maps(self):
        CirclerOut(self, 30, pygame.mouse.get_pos())
        self.next_scene = defaults.CustomMapScene(self.surface)

    def go_to_map_creater(self):
        CirclerOut(self, 30, pygame.mouse.get_pos())
        self.next_scene = defaults.MapCreaterScene(self.surface)
    
    def update(self):
        pass
    
    def render(self):
        self.render_manager.render()
