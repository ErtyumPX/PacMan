import pygame
from game import *
import defaults, time

#SCENES
from menu_scene import MenuScene
from game_scene import GameScene

pygame.init()

pygame.mouse.set_cursor(*defaults.CURSOR)

size = rootX, rootY = defaults.SIZE

root = pygame.display.set_mode(size)
pygame.display.set_caption(defaults.WINDOW_NAME)

game = Game(MenuScene(root), defaults.FRAME_RATE)

game.run()
