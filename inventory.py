import pygame, os
from main import CARD_SIZE, LITTLE_CARD_SIZE, COLOURS
from cards import all_cards

class Collection():
	"""Клас для всіх карт доступних у грі"""
	def __init__(self, all_cards):
		self.deck = all_cards

	def find_card_by_id(self, id): # об'єкт картки можна знайти по id
		return self.deck[id]

	def add_cards(self, cards): # коли буде БД, тут можна буде її оновлювати
		self.deck = cards

	def calculate_grid_position(self, index): # сіточка в меню
		column_width = 150
		row_height = 150
		margin = 20

		column = index % 6  # карт в рядку
		row = index // 6 # карт в колоні

		x = 200 + column * (CARD_SIZE[0] + margin)
		y = 240 + row * (CARD_SIZE[1] + margin)

		return x, y

class Inventory(Collection):
	"""Клас інвентаря гравця - цю колоду він може брати до самої гри"""
	def __init__(self, all_cards):
		super().__init__(all_cards)
		self.inventory = []
		self.required = 12 # мінімум кард для початку

	def add_to_inventory(self, id):
		card = self.find_card_by_id(id)
		if card.unlocked: # закриті картки не можна брати
			self.inventory.append(card)
			card.draw_card(inventory = True) # зелений
			# print("Card added and painted")

	def remove_from_inventory(self, id):
		card = self.find_card_by_id(id) #
		for used in self.inventory: # Тут можна оптимізувати
			if card == used: 
				self.inventory.remove(card)
				card.draw_card(inventory = False) # колір скидається
				# print("Card removed and painted")

	def check_requirements(self): # критерії колоди
		if len(self.inventory) >= self.required:
			return True
		else:
			return False
		

def main():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()

	info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
	SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

	boxes, images = [], []

	pygame.display.set_caption("Поворуши великим пальцем!")

	title_font = pygame.font.Font(None, 48)
	title_text = title_font.render("КОЛЕКЦІЯ КАРТОК", True, COLOURS["black"])
	title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 70))

	collection = Collection(all_cards)
	inventory = Inventory(all_cards)
	p = 0
	for i, card in collection.deck.items():
		x, y = collection.calculate_grid_position(p)
		card.position_card(x, y)
		card.draw_card()

		boxes.append(card)
		images.append(card.image)

		p += 1

	active_box = None

	running = True
	while running:
		screen.fill(COLOURS["cream"])
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				try:
					for num, box in enumerate(boxes):
						if box.object_rect.collidepoint(event.pos):
							card_id = id(box)
							selected_card = collection.find_card_by_id(card_id)

							if selected_card not in inventory.inventory:
								inventory.add_to_inventory(card_id)
								images[num] = boxes[num].image #промальовка
							else:
								inventory.remove_from_inventory(card_id)
								images[num] = boxes[num].image
				except:
					print("Ну й нахіба клікать просто так?!")

			if event.type == pygame.QUIT:
				running = False
		

		screen.blit(title_text, title_rect)

		for index, image in enumerate(images):
			if index != active_box:
				screen.blit(image, boxes[index].object_rect)	



		pygame.display.update()

if __name__ == "__main__":
	main()