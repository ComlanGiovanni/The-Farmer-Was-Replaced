from lib import *

def handle_sunflower():
	harvest_if_ready()
	if get_entity_type() != Entities.Sunflower:
		plant(Entities.Sunflower)
	water_and_fertilize()

def farm_sunflower_callback(x, y):
	handle_sunflower()

def find_max_petals():
	world_size = get_world_size()
	max_petals = 0
	max_x = 0
	max_y = 0
	
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			if get_entity_type() == Entities.Sunflower:
				if can_harvest():
					petals = measure()
					if petals > max_petals:
						max_petals = petals
						max_x = x
						max_y = y
	
	return max_x, max_y, max_petals

def harvest_best_sunflower():
	max_x, max_y, max_petals = find_max_petals()
	if max_petals > 0:
		goto_pos(max_x, max_y)
		harvest()
		plant(Entities.Sunflower)
		water_and_fertilize()
	return_to_spawn()

def count_sunflowers():
	world_size = get_world_size()
	count = 0
	
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			if get_entity_type() == Entities.Sunflower:
				count += 1
	
	return_to_spawn()
	return count

def setup_sunflower_farm():
	clear_map()
	till_entire_map()
	traverse_map_snake(farm_sunflower_callback)
	return_to_spawn()

setup_sunflower_farm()

while True:
	traverse_map_snake(farm_sunflower_callback)
	
	if count_sunflowers() >= 10:
		harvest_best_sunflower()
	
	return_to_spawn()