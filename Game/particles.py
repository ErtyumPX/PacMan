import pygame, random
from time import time

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos:list, velocity:list, gravity:float, creation_time:float):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.velocity = velocity
        self.gravity = gravity
        self.creation_time = creation_time

    def move(self):
        self.velocity[1] += self.gravity
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]


class CircleParticle(pygame.sprite.Sprite):
    def __init__(self, surface:pygame.Surface, pos:list, max_particle:int, color:tuple = (255,255,255), life_time:int = 3, gravity:float = 0.1):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.pos = pos
        self.max_particle = max_particle
        self.color = color
        self.life_time = life_time
        self.gravity = gravity

        self.particle_list = [Particle(self.pos, [random.random(), random.random()], gravity, time()) for _ in range(max_particle)]

    def update(self):
        for part in self.particle_list:
            pygame.draw.circle(self.surface, self.color, (int(part.pos[0]), int(part.pos[1])), 2*(time()-part.creation_time)/self.life_time)
            if time() - part.creation_time >= self.life_time:
                self.particle_list.remove(part)
                self.particle_list.append(Particle(self.pos, [random.random(), random.random()], self.gravity, time()))
            else:
                part.move()

