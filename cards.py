import pygame
from main import CARD_SIZE, LITTLE_CARD_SIZE, COLOURS

class Card():
	def __init__(self, name, description, health, position_type, image, ability = None):
		self.name = name
		self.description = description
		self.health = health
		self.position_type = position_type
		self.unlocked = False # закриті картки недоступні гравцеві
		self.aility = ability # ту бі контінуед

		self.temp_img = pygame.image.load(f"img/{image}.jpg") # картка

		self.attached_to_drop_zone = None # для поля


	def position_card(self, x, y, initial = False):
		# x = 300 + i * ((SCREEN_WIDTH - 400 - CARD_SIZE[1]) / 7)
		# y = SCREEN_HEIGHT - (CARD_SIZE[1] / 3)

		self.x, self.y = x, y
		if initial: # ця змінна дозволяє запам'ятати попередню позицію
			self.initial_pos = (self.x, self.y)

	def draw_card(self, inventory = False):
		temp_img = self.temp_img.convert_alpha()
		self.image = pygame.transform.scale(temp_img, CARD_SIZE)

		# коричневі - недоступні
		if not self.unlocked:
			cover_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
			dark = COLOURS["brown"] + (128,) # альфа канал напівпрозорості
			cover_surface.fill(dark)

			self.image.blit(cover_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

		# зелені - екіпіровані
		if self.unlocked and inventory:
			cover_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
			green = COLOURS["green"] + (220,) # альфа канал напівпрозорості
			cover_surface.fill(green)

			self.image.blit(cover_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

		self.object_rect = self.image.get_rect()
		self.object_rect.center = (self.x, self.y)

		##### Пам'ятай додати щось на кшталт цього для оновлення кадру
		# images[num] = boxes[num].image #промальовка

	# функція виставлення на поле
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

	def unlock_card(self):
		self.unlocked = True

all_cards = {}


##### Тут можна додавати картки й робити тести #####

card1 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 2)
all_cards[id(card1)] = card1
card2 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 1)
all_cards[id(card2)] = card2
card3 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 3)
all_cards[id(card3)] = card3
card4 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 2)
all_cards[id(card4)] = card4
card5 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 1)
all_cards[id(card5)] = card5
card6 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 2)
all_cards[id(card6)] = card6
card7 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 3)
all_cards[id(card7)] = card7
card8 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 1)
all_cards[id(card8)] = card8
card9 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 1)
all_cards[id(card9)] = card9
card10 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 3)
all_cards[id(card10)] = card10
card11 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 1)
all_cards[id(card11)] = card11
card12 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 3)
all_cards[id(card12)] = card12
card13 = Card("Люта тєма", "Мутим лютий двіж!", 5, False, 2)
all_cards[id(card13)] = card13


# for a, b in all_cards.items():
# 	print(f"{a}	|	{b}")

card2.unlock_card()
card4.unlock_card()
card6.unlock_card()
card7.unlock_card()
card12.unlock_card()
