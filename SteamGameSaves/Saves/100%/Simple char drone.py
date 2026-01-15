from core import *
from farming import *
from callback import *
from multidrone import *
from advanced import *
from achivement import *


FONT = {
	'A': [[1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1], [1,0,0,0,1], [0,1,1,1,0]],
	'B': [[1,1,1,1,0], [1,0,0,0,1], [1,1,1,1,0], [1,0,0,0,1], [1,1,1,1,0]],
	'C': [[0,1,1,1,0], [1,0,0,0,1], [1,0,0,0,0], [1,0,0,0,1], [0,1,1,1,0]],
	'D': [[1,1,1,1,0], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,0]],
	'E': [[1,1,1,1,1], [1,0,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,1,1,1]],
	'F': [[1,0,0,0,0], [1,0,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,1,1,1]],
	'G': [[0,1,1,1,0], [1,0,0,0,1], [1,0,1,1,1], [1,0,0,0,0], [0,1,1,1,0]],
	'H': [[1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1]],
	'I': [[1,1,1,1,1], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0], [1,1,1,1,1]],
	'J': [[0,1,1,0,0], [1,0,0,1,0], [0,0,0,1,0], [0,0,0,1,0], [0,0,1,1,1]],
	'K': [[1,0,0,0,1], [1,0,0,1,0], [1,1,1,0,0], [1,0,0,1,0], [1,0,0,0,1]],
	'L': [[1,1,1,1,1], [1,0,0,0,0], [1,0,0,0,0], [1,0,0,0,0], [1,0,0,0,0]],
	'M': [[1,0,0,0,1], [1,0,0,0,1], [1,0,1,0,1], [1,1,0,1,1], [1,0,0,0,1]],
	'N': [[1,0,0,0,1], [1,0,0,1,1], [1,0,1,0,1], [1,1,0,0,1], [1,0,0,0,1]],
	'O': [[0,1,1,1,0], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [0,1,1,1,0]],
	'P': [[1,0,0,0,0], [1,0,0,0,0], [1,1,1,1,0], [1,0,0,0,1], [1,1,1,1,0]],
	'Q': [[0,1,1,1,1], [1,0,1,0,1], [1,0,0,0,1], [1,0,0,0,1], [0,1,1,1,0]],
	'R': [[1,0,0,0,1], [1,0,0,1,0], [1,1,1,1,0], [1,0,0,0,1], [1,1,1,1,0]],
	'S': [[1,1,1,1,0], [0,0,0,0,1], [0,1,1,1,0], [1,0,0,0,0], [0,1,1,1,1]],
	'T': [[0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0], [1,1,1,1,1]],
	'U': [[0,1,1,1,0], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1]],
	'V': [[0,0,1,0,0], [0,1,0,1,0], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1]],
	'W': [[1,0,0,0,1], [1,1,0,1,1], [1,0,1,0,1], [1,0,0,0,1], [1,0,0,0,1]],
	'X': [[1,0,0,0,1], [0,1,0,1,0], [0,0,1,0,0], [0,1,0,1,0], [1,0,0,0,1]],
	'Y': [[0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,1,0,1,0], [1,0,0,0,1]],
	'Z': [[1,1,1,1,1], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [1,1,1,1,1]],
}

def draw_single_pixel(x, y):
	goto_pos(x, y)
	if get_ground_type() == Grounds.Grassland:
		till()
	entity = get_entity_type()
	if entity != None:
		harvest()
	plant(Entities.Sunflower)
	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)

def erase_single_pixel(x, y):
	goto_pos(x, y)
	entity = get_entity_type()
	if entity != None:
		harvest()
	if get_ground_type() == Grounds.Soil:
		till()

# Dessine un caractere avec un drone par pixel
def draw_char_with_drones(char, start_x, start_y):
	if char not in FONT:
		return
	
	pattern = FONT[char]
	pixels_to_draw = []
	
	for row in range(5):
		for col in range(5):
			if pattern[row][col] == 1:
				pixels_to_draw.append((start_x + col, start_y + row))
	
	drones = []
	
	for pixel_x, pixel_y in pixels_to_draw:
		def draw_pixel_at():
			draw_single_pixel(pixel_x, pixel_y)
		
		drone = spawn_drone(draw_pixel_at)
		if drone == None:
			draw_pixel_at()
		else:
			drones.append(drone)
	
	for drone in drones:
		wait_for(drone)

def erase_char_with_drones(char, start_x, start_y):
	if char not in FONT:
		return
	
	pattern = FONT[char]
	pixels_to_erase = []
	
	for row in range(5):
		for col in range(5):
			if pattern[row][col] == 1:
				pixels_to_erase.append((start_x + col, start_y + row))
	
	drones = []
	
	for pixel_x, pixel_y in pixels_to_erase:
		def erase_pixel_at():
			erase_single_pixel(pixel_x, pixel_y)
		
		drone = spawn_drone(erase_pixel_at)
		if drone == None:
			erase_pixel_at()
		else:
			drones.append(drone)
	
	for drone in drones:
		wait_for(drone)

def write_text_simple():
	set_world_size(9)
	
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	drone = ['D','R','O','N','E']
	
	start_x = 2
	start_y = 2
	
	for char in drone:
		if char in FONT:
			draw_char_with_drones(char, start_x, start_y)
			
			# Pause
			for i in range(200):
				pass

			erase_char_with_drones(char, start_x, start_y)

write_text_simple()