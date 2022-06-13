from game import FadeIn, FadeOut
from scene import Scene
from renderer import RenderManager
from ui_elements import TextButton, ProcessElements
import pygame, defaults

#next scenes
from game_scene import GameScene



class Menu(Scene):
    def __init__(self, main_surface):
        super().__init__(main_surface)
        self.surface = main_surface
        self.render_manager = RenderManager(main_surface, background_color=(80, 80, 80))

        play_button = TextButton(main_surface, x=defaults.SIZE[0]/2-50, y=300, width=100, height=40, text="PLAY", func=self.play,color=(255,0,0))
        self.render_manager.add(play_button)
        self.BUTTONS = [play_button,]

        FadeIn(self, 40)


    def process_input(self, events, pressed_keys, mouse_pos):
        ProcessElements(events, pressed_keys, mouse_pos, self.BUTTONS)

    def play(self):
        FadeOut(self, 40)
        self.next_scene = GameScene(self.surface)
    
    def update(self):
        pass
    
    def render(self):
        self.render_manager.render()
