import pygame, defaults, time
from transform import Transform
from random import randint, choice
from math import floor
from animation import bySpeed

vel_add = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surface, x=0, y=0, vel=randint(1, 4)):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.transform = Transform(x=x, y=y)
        self.velocity = vel  # 0:stand, 1:up, 2:right, 3:down, 4:left
        self.image = defaults.ENEMY_IMAGE

        self.is_moving = False
        self.moving_speed = 7
        self.possible_choices = [1, 2, 3, 4]

    def after_function(self):
        self.is_moving = False
        self.find_possible_ways()

    def find_possible_ways(self):
        possible_choices = [1, 2, 3, 4]
        possible_choices.remove(self.velocity)
        k = (self.velocity + 1) % 4 + 1
        possible_choices.remove(k)
        self.possible_choices = possible_choices

    def change_direction(self, tiles):
        v = choice(self.possible_choices)
        next_step = vel_add[v]
        if tiles[floor(self.transform.x + next_step[0])][floor(self.transform.y + next_step[1])] == 1:
            self.velocity = v

    def move(self, tiles):
        if not self.is_moving and self.velocity != 0:
            self.change_direction(tiles)
            next_step = vel_add[self.velocity]
            
            if tiles[floor(self.transform.x + next_step[0])][floor(self.transform.y + next_step[1])] == 1:
                next_pos = (self.transform.x + next_step[0], self.transform.y + next_step[1])
                self.is_moving = True
                bySpeed(self.transform, next_pos, self.moving_speed, defaults.FRAME_RATE, self.after_function)


    def update(self):
        x = self.transform.x * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2
        y = self.transform.y * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2
        r = 7
        pygame.draw.circle(self.surface, (0, 0, 0), (x, y), r)
