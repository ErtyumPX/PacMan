import pygame
from scene import Scene

class Game:
    def __init__(self, first_scene:Scene, frame_rate:int):
        assert isinstance(first_scene, Scene)
        self.active_scene = first_scene
        self.frame_rate = frame_rate
        self.clock = pygame.time.Clock()

        self.last_function = lambda: print("End of the game.")

    def run(self): 
        while self.active_scene is not None:
            # Get user input
            pressed_keys = pygame.key.get_pressed()
            filtered_events = []
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.active_scene.terminate()
                    HorizontalSlidingOut(self.active_scene, 40)
                else:
                    filtered_events.append(event)

            # Manage scene
            self.active_scene.process_input(filtered_events, pressed_keys, mouse_pos)
            self.active_scene.update()
            if self.active_scene == self.active_scene.next_scene:
                self.active_scene.render()
            else:
                self.active_scene = self.active_scene.next_scene

            # Update and tick
            pygame.display.flip()
            self.clock.tick(self.frame_rate)

        # Call last function before shutting down the window
        self.last_function()





def FadeIn(scene:Scene, fq:int, alpha=255):
    fade_surface = pygame.Surface((scene.surface.get_width(), scene.surface.get_height()), pygame.SRCALPHA, 32)
    while alpha > 10:
        scene.render()
        fade_surface.fill((0,0,0,alpha))
        scene.surface.blit(fade_surface, (0,0))
        pygame.display.flip()
        alpha -= fq
        pygame.time.wait(10)
    pygame.event.clear()


def FadeOut(scene:Scene, fq:int, alpha=0):
    fade_surface = pygame.Surface((scene.surface.get_width(), scene.surface.get_height()), pygame.SRCALPHA, 32)
    while alpha < 245:
        scene.render()    
        fade_surface.fill((0,0,0,alpha))
        scene.surface.blit(fade_surface, (0,0))
        pygame.display.flip()
        alpha += fq
        pygame.time.wait(10)
    pygame.event.clear()


def HorizontalSlidingIn(scene:Scene, speed:int): #speed = 30 : default
    size = scene.surface.get_size()
    block = pygame.Surface((size[0]/2+50, size[1]))
    right_block_pos_x = -50
    left_block_pos_x = size[0]/2
    while right_block_pos_x > -size[0]/2-50:
        scene.render()
        scene.surface.blit(block, (right_block_pos_x, 0))
        scene.surface.blit(block, (left_block_pos_x, 0))
        right_block_pos_x -= speed
        left_block_pos_x += speed
        speed **= 0.95
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.event.clear()


def HorizontalSlidingOut(scene:Scene, speed:int):
    size = scene.surface.get_size()
    block = pygame.Surface((size[0]/2+50, size[1]))
    right_block_pos_x = -size[0]/2-50
    left_block_pos_x = size[0]
    while right_block_pos_x < 0:
        scene.render()
        scene.surface.blit(block, (right_block_pos_x, 0))
        scene.surface.blit(block, (left_block_pos_x, 0))
        right_block_pos_x += speed
        left_block_pos_x -= speed
        speed **= 0.95
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.event.clear()

def CirclerOut(scene:Scene , speed:int):
    return


def CircleCut(size:list, mouse:list):
    return
