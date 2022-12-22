import pygame, defaults, time
from transform import Transform
from random import randint, choice, random
from math import floor, sqrt
from animation import bySpeed
from copy import deepcopy

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
        self.the_closest_direction = None

        self.borning_time = time.time()
        self.new_born = True
        self.blink_time = defaults.ENEMY_BLINK_TIME
        self.blink_frequency = 0.5
        self.blink = False

        self.starting_point = (x, y)
        self.vulnerable_until = None
        

    def find_possible_ways(self, tiles):
        self.is_moving = False
        possible_choices = [1, 2, 3, 4]
        possible_choices.remove(self.velocity)
        #prevent them to turn back
        k = (self.velocity + 1) % 4 + 1
        possible_choices.remove(k)
        self.possible_choices = possible_choices

    def find_closest_way_to_the_pacman(self, pacman_position:tuple, inverted:bool=False) -> int:
        '''
        possibility -> The possibility of choosing the closest way to the pacman, out of 100

        inverted -> If a super berry has been eaten soon, the possibility computation will 
        be inverted, so the enemy will try to find the furthest position from the pacman
        '''
        the_closest_distance = None
        the_closest_direction = None
        if not inverted:
            for direction in self.possible_choices:
                next_position = (floor(self.transform.x + vel_add[direction][0]), floor(self.transform.y + vel_add[direction][1]))
                distance = sqrt( (pacman_position[0] - next_position[0])**2 + (pacman_position[1] - next_position[1])**2 )
                if not the_closest_distance:   
                    the_closest_distance = distance
                    the_closest_direction = direction
                else:
                    if distance < the_closest_distance:
                        the_closest_distance = distance
                        the_closest_direction = direction

        else: #if inverted
            for direction in self.possible_choices:
                next_position = (floor(self.transform.x + vel_add[direction][0]), floor(self.transform.y + vel_add[direction][1]))
                distance = sqrt( (pacman_position[0] - next_position[0])**2 + (pacman_position[1] - next_position[1])**2 )
                if not the_closest_distance:   
                    the_closest_distance = distance
                    the_closest_direction = direction
                else:
                    if distance > the_closest_distance:
                        the_closest_distance = distance
                        the_closest_direction = direction

        self.the_closest_direction = the_closest_direction


    def change_direction(self, tiles, pacman_position:tuple, possibility:float=40, inverted:bool=False):
        #direction = choice(self.possible_choices)
        self.find_closest_way_to_the_pacman(pacman_position, inverted=inverted)
        if random()*100 > possibility and len(self.possible_choices) != 1:
            current_possible_choices = deepcopy(self.possible_choices)
            current_possible_choices.remove(self.the_closest_direction)
            direction = choice(current_possible_choices)
        else:
            direction = self.the_closest_direction

        next_step = vel_add[direction]
        if tiles[floor(self.transform.x + next_step[0])][floor(self.transform.y + next_step[1])] == 1:
            self.velocity = direction

    def move(self, tiles, pacman_position:tuple, possibility:float=40, inverted:bool=False):
        if not self.is_moving and self.velocity != 0:
            self.change_direction(tiles, pacman_position, possibility=possibility, inverted=inverted)
            next_step = vel_add[self.velocity]
            
            if tiles[floor(self.transform.x + next_step[0])][floor(self.transform.y + next_step[1])] == 1:
                next_pos = (self.transform.x + next_step[0], self.transform.y + next_step[1])
                self.is_moving = True
                bySpeed(self.transform, next_pos, self.moving_speed, defaults.FRAME_RATE, self.find_possible_ways, args=(tiles,))


    def update(self):
        x = self.transform.x * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2
        y = self.transform.y * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2
        r = 7
        if self.new_born and self.blink:
            pygame.draw.circle(self.surface, defaults.ENEMY_BLINKING_COLOR, (x, y), r)
        elif self.vulnerable_until != None:
            pygame.draw.circle(self.surface, defaults.ENEMY_VULNERABLE_COLOR, (x, y), r)
        else:
            pygame.draw.circle(self.surface, defaults.ENEMY_COLOR, (x, y), r)
