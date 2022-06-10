import pygame

class RenderManager:
	def __init__(self, surface:pygame.Surface, background_color=None):
		self.surface = surface
		self.background_color = background_color
		self.objects = []

	def add(self, *args):
		for obj in args:
			self.objects.append(obj)

	def remove(self, *args):
		for obj in args:
			try:
				self.objects.remove(obj)
			except Exception as exp:
				print(exp)

	def reset(self):
		self.objects = []

	def render(self):
		if self.background_color is not None:
			self.surface.fill(self.background_color)
		for x in self.objects:
			x.update()
