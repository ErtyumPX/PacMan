import pygame
from game import *
import defaults

#SCENES
from menu_scene import Menu
from scene1 import Scene1

pygame.init()

pygame.mouse.set_cursor(*defaults.CURSOR)

size = rootX, rootY = defaults.SIZE

root = pygame.display.set_mode(size)
pygame.display.set_caption(defaults.WINDOW_NAME)

game = Game(Menu(root), defaults.FRAME_RATE)

game.run()
