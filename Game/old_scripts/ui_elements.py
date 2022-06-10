import pygame

empty_function = lambda: 0

def ButtonCollide(card, mouse):
	#x = card.x + card.upper_surface[0]
	#y = card.y + card.upper_surface[1]
	x = card.x
	y = card.y
	return x < mouse[0] < x + card.image.get_width() and y < mouse[1] < y + card.image.get_height()

def InputBoxCollide(box, mouse):
	return box.textRect[0] < mouse[0] < box.textRect[0] + box.textRect[2] and box.textRect[1] < mouse[1] < box.textRect[1] + box.textRect[3]


class InterfaceElement:
	def __init__(self, status):
		self.status = status # 0: visible/interactable   1: visible/uninteractable  2: invisible

	def change_status(self, new_status):
		if -1 < new_status < 3:
			self.status = new_status
		else:
			raise Exception("Improper status")


class Button(pygame.sprite.Sprite, InterfaceElement):
	def __init__(self, surface, image, x, y, func=empty_function, args=(), kwargs={}, upper_surface=(0,0), selected_change=(0,0), highlight_color = None, highlight_offset = (0, 0), status=0):
		pygame.sprite.Sprite.__init__(self)
		InterfaceElement.__init__(self, status)
		self.surface = surface
		self.image = image

		self.x, self.y = x, y
		self.upper_surface = upper_surface
		self.selected_change = selected_change
		self.selected = False
		self.clicked = False

		self.func = func
		self.args = args
		self.kwargs = kwargs

		self.highlight_color = highlight_color
		self.highlight_offset = highlight_offset
		if highlight_color:
			image_size = image.get_size()
			self.effect = pygame.Surface((image_size[0]+highlight_offset[0], image_size[1]+highlight_offset[1]), pygame.SRCALPHA)
			self.effect.fill(highlight_color)

	def update(self):
		if self.status != 2:
			if self.selected:
				self.surface.blit(self.image, (self.x+self.selected_change[0], self.y+self.selected_change[1]))
				if self.highlight_color: self.surface.blit(self.effect, (self.x+self.selected_change[0]-self.highlight_offset[0]/2, self.y+self.selected_change[1]-self.highlight_offset[1]/2))
			else:
				self.surface.blit(self.image, (self.x, self.y))




class TextButton(pygame.sprite.Sprite, InterfaceElement):
	def __init__(self, surface, image, x, y, func=empty_function, args=(), kwargs={}, font_size=24, text="Default Text", color=(0,0,0), selected_change=(0,0), highlight_color = None, highlight_offset = (0, 0), status=0):
		pygame.sprite.Sprite.__init__(self)
		InterfaceElement.__init__(self, status)
		self.surface = surface
		self.image = image

		self.x, self.y = x, y
		self.selected_change = selected_change
		self.selected = False
		self.clicked = False

		self.func = func
		self.args = args
		self.kwargs = kwargs

		self.highlight_color = highlight_color
		self.highlight_offset = highlight_offset
		if highlight_color:
			image_size = image.get_size()
			self.effect = pygame.Surface((image_size[0]+highlight_offset[0], image_size[1]+highlight_offset[1]), pygame.SRCALPHA)
			self.effect.fill(highlight_color)

		self.text = text
		self.color = color
		self.font = pygame.font.Font('data/munro.ttf', font_size)
		self.text_box = self.font.render(self.text, True, color)
		text_size = self.text_box.get_size()
		self.textRect = pygame.Rect(0,0,0,0)
		self.textRect.center = (x+int(image.get_width()/2)-int(text_size[0]/2), y+int(image.get_height()/2)-int(text_size[1]/2))
		#self.textRect.center = (x+int(image.get_width()/2), y+int(image.get_height()/2))
		#self.charRect = self.textRect.move(5, 0)

	def update(self):
		if self.status != 2:
			self.surface.blit(self.image, (self.x, self.y))
			self.surface.blit(self.text_box, self.textRect)

			if self.selected and self.highlight_color:
				self.surface.blit(self.effect, (self.x-self.highlight_offset[0]/2, self.y-self.highlight_offset[1]/2))


def UpdateCards(events, mouse_pos, cards = []):
	for card_ in cards:
		card_.clicked = False
		if ButtonCollide(card_, mouse_pos):
			card_.selected = True
		else:
			card_.selected = False
	for event in events:
		if event.type == pygame.MOUSEBUTTONUP:
			for card_ in cards:
				if card_.selected and card_.status == 0:
					card_.func(*card_.args, **card_.kwargs)
					card_.clicked = True