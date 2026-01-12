from lib import *

# CROP MANAGEMENT - Specific

def handle_tree():
	if get_entity_type() == Entities.Tree:
		harvest_if_ready()
		plant(Entities.Tree)
		watering_grounds()
		fertilize()

def handle_pumpkin():
	entity = get_entity_type()
	
	if can_harvest():
		harvest()
	
	if entity == Entities.Dead_Pumpkin or entity == None:
		plant(Entities.Pumpkin)
	
	watering_grounds()
	fertilize()

def handle_carrot():
	if can_harvest():
		harvest()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	watering_grounds()
	fertilize()

def handle_sunflower():
	if can_harvest():
		harvest()
	if get_entity_type() != Entities.Sunflower:
		plant(Entities.Sunflower)
	watering_grounds()
	fertilize()

def handle_cactus():
	if can_harvest():
		harvest()
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)
	watering_grounds()
	fertilize()

def handle_grass():
	if can_harvest():
		harvest()
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	watering_grounds()
	fertilize()


# FARMING PATTERNS

def farm_only_carrots(x, y):
	handle_carrot()

def farm_mixed_zones(x, y):
	if x < 2:
		handle_tree()
	elif x < 4:
		handle_pumpkin()
	elif x < 6:
		handle_carrot()
	elif x < 8:
		handle_sunflower()
	elif x < 10:
		handle_cactus()
	else:
		handle_grass()

def farm_pumpkin_and_carrot(x, y):
	world_size = get_world_size()
	if x < world_size // 2:
		handle_pumpkin()
	else:
		handle_carrot()

def farm_trees_checkerboard(x, y):
	tile_number = y * get_world_size() + x
	if not is_even(tile_number):
		handle_tree()

# MAIN FARMING LOOPS

def farm(pattern_function):
	return_to_spawn()
	
	while True:
		traverse_map_snake(pattern_function)
		return_to_spawn()
