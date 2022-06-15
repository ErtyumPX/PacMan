import pygame, defaults
from transform import Transform


class Berry(pygame.sprite.Sprite):
    def __init__(self, surface, x:int = 0, y:int = 0):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.transform = Transform(x=x, y=y)

    def update(self):
        x = int(self.transform.x * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2)
        y = int(self.transform.y * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2)
        r = 2
        pygame.draw.circle(self.surface, defaults.BERRY_COLOR, (x, y), r)
