import pygame, defaults
from transform import Transform


class SuperBerry(pygame.sprite.Sprite):
    def __init__(self, surface, x:int = 0, y:int = 0):
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.transform = Transform(x=x, y=y)
        self.is_taken = False

    def update(self):
        if not self.is_taken:
            x = int(self.transform.x * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2)
            y = int(self.transform.y * defaults.TILE_WIDTH + defaults.TILE_WIDTH / 2)
            r = 5
            pygame.draw.circle(self.surface, 0, (x, y), r + 1)
            pygame.draw.circle(self.surface, defaults.SUPER_BERRY_COLOR, (x, y), r)
