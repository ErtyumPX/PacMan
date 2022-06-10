import pygame, defaults, time
from transform import Transform
from animation import bySpeed
from math import floor

vel_add = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}

class Pacman(pygame.sprite.Sprite):
    def __init__(self, surface, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.transform = Transform(x=x, y=y)
        self.velocity = 0  # 0:stand, 1:up, 2:right, 3:down, 4:left
        self.image = defaults.PACMAN_IMAGE

        self.moving_speed = 8
        self.is_moving = False

    def after_function(self):
        self.is_moving = False

    def move(self, tiles):
        if not self.is_moving and self.velocity != 0:
            next_step = vel_add[self.velocity]
            if tiles[floor(self.transform.x + next_step[0])][floor(self.transform.y + next_step[1])] == 1:
                next_pos = (self.transform.x + next_step[0], self.transform.y + next_step[1])
                self.is_moving = True
                bySpeed(self.transform, next_pos, self.moving_speed, defaults.FRAME_RATE, self.after_function)


    def update(self):
        x = int(self.transform.x * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2)
        y = int(self.transform.y * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2)
        r = 7
        pygame.draw.circle(self.surface, (255, 255, 0), (x, y), r)
