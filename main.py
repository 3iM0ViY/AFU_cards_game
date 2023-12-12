import pygame, os
import random

CARD_SIZE = (150, 220)
LITTLE_CARD_SIZE = (90, 140)
COLOURS = {
		"blue": (0, 123, 167),
		"yellow": (255, 195, 18),
		"green": (34, 153, 84),
		"red": (207, 0, 15),
		"wheat": (245, 222, 179),
		"purple": (136, 78, 160),
		"brown": (139, 69, 19),
		"orange": (235, 149, 50),
		"black": (0, 0, 0),
		"cream": (255, 245, 239)
	}

class Card():
	def __init__(self, i, SCREEN_WIDTH, SCREEN_HEIGHT):
		x = 300 + i * ((SCREEN_WIDTH - 400 - CARD_SIZE[1]) / 7)

		self.x, self.y = x, SCREEN_HEIGHT - (CARD_SIZE[1] / 3)
		self.initial_pos = (self.x, self.y)

		self.temp_img = pygame.image.load(f"img/1.jpg").convert_alpha()
		self.image = pygame.transform.scale(self.temp_img, CARD_SIZE)
		self.object_rect = self.image.get_rect()
		self.object_rect.center = (self.x, self.y)

		self.attached_to_drop_zone = None  # Дропнуто

	def attach_to_drop_zone(self, drop_zone, drop_zones, boxes):
		if drop_zone not in drop_zones:
			return

		drop_zone_index = drop_zones.index(drop_zone)

		num_cards_in_drop_zone = sum(1 for box in boxes if box.attached_to_drop_zone == drop_zone)
		offset_x = num_cards_in_drop_zone * (LITTLE_CARD_SIZE[0] + 10)  # відстань між картками
		self.object_rect.center = (drop_zone.x + drop_zone.width // 2 + offset_x, drop_zone.y + drop_zone.height // 2)
		self.attached_to_drop_zone = drop_zone

		# Маленька картинка
		self.image = pygame.transform.smoothscale(self.temp_img, LITTLE_CARD_SIZE)
		self.object_rect = self.image.get_rect()
		self.object_rect.center = (drop_zone.x + drop_zone.width // 2 + offset_x, drop_zone.y + drop_zone.height // 2)


def main():
	os.environ['SDL_VIDEO_CENTERED'] = '1'

	pygame.init()

	info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
	SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

	# SCREEN_WIDTH = 1000
	# SCREEN_HEIGHT = 800

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

	pygame.display.set_caption("Поворуши великим пальцем!")

	boxes, images = [], []


	drop_zone_height = 110
	drop_zones = []
	drop_zone_spacing = int(0.01 * SCREEN_HEIGHT)  # % відстані між рядами
	total_drop_zone_height = 6 * drop_zone_height + 5 * drop_zone_spacing
	start_y = (SCREEN_HEIGHT - total_drop_zone_height) // 2

	for i in range(6):
		drop_zone = pygame.Rect(300, start_y + i * (drop_zone_height + drop_zone_spacing), SCREEN_WIDTH - 600, drop_zone_height)
		drop_zones.append(drop_zone)

	hand_zone_height = 125
	hand_zones = [
		pygame.Rect(200, 0, SCREEN_WIDTH - 400, hand_zone_height),
		pygame.Rect(200, SCREEN_HEIGHT - hand_zone_height, SCREEN_WIDTH - 400, hand_zone_height)
	]


	for i in range(0, 8):
		new_card = Card(i, SCREEN_WIDTH, SCREEN_HEIGHT)

		boxes.append(new_card)
		images.append(new_card.image)

	active_box = None


	running = True
	while running:
		screen.fill(COLOURS["cream"])
		for event in pygame.event.get():

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				try:
					for num, box in enumerate(boxes):
						if box.object_rect.collidepoint(event.pos):
							active_box = num
				except:
					print("Ну й нахіба клікать просто так?!")

			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				try:
					for drop_zone in drop_zones: # додавання в ряд на відпускання миші
						if boxes[active_box].object_rect.colliderect(drop_zone):
							boxes[active_box].attach_to_drop_zone(drop_zone, drop_zones, boxes)
							images[active_box] = boxes[active_box].image #оновлення зображення
							break
					else:
						# якщо ряду не було, повернути назад до руки
						boxes[active_box].object_rect.x = boxes[active_box].initial_pos[0] - (CARD_SIZE[0]/2) 
						boxes[active_box].object_rect.y = boxes[active_box].initial_pos[1] - (CARD_SIZE[1]/2)
				except:
					print("Ну й нахіба клікать просто так?!")

				active_box = None

			if event.type == pygame.MOUSEMOTION and active_box is not None:
				# руханка
				boxes[active_box].object_rect.move_ip(event.rel)

				# колізія із стінками
				if boxes[active_box].object_rect.left < 0:
					boxes[active_box].object_rect.left = 0
				if boxes[active_box].object_rect.right > SCREEN_WIDTH:
					boxes[active_box].object_rect.right = SCREEN_WIDTH
				if boxes[active_box].object_rect.top < 0:
					boxes[active_box].object_rect.top = 0
				if boxes[active_box].object_rect.bottom > SCREEN_HEIGHT:
					boxes[active_box].object_rect.bottom = SCREEN_HEIGHT

			if event.type == pygame.QUIT:
				running = False

		# Дроп зони
		for drop_zone in drop_zones:
			pygame.draw.rect(screen, COLOURS["wheat"], drop_zone)

		# Рука гравця
		for hand_zone in hand_zones:
			pygame.draw.rect(screen, COLOURS["yellow"], hand_zone)

		# Малювання карток
		for index, image in enumerate(images):
			if index != active_box:
				screen.blit(image, boxes[index].object_rect)

		# Обрана картка завжди поверх
		if active_box is not None:
			screen.blit(images[active_box], boxes[active_box].object_rect)

		pygame.display.update()

if __name__=="__main__":
	main()