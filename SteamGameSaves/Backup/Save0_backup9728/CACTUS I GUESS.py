from lib import *

def handle_cactus():
	harvest_if_ready()
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)
	water_and_fertilize()

def farm_cactus_callback(x, y):
	handle_cactus()

def get_cactus_size(x, y):
	goto_pos(x, y)
	if get_entity_type() == Entities.Cactus and can_harvest():
		size = measure()
		return_to_spawn()
		return size
	return_to_spawn()
	return None

def check_sorted_chain(x, y):
	world_size = get_world_size()
	directions = [North, East, South, West]
	offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	
	current_size = get_cactus_size(x, y)
	if current_size == None:
		return False
	
	for i in range(4):
		dx, dy = offsets[i]
		nx, ny = x + dx, y + dy
		
		if nx >= 0 and nx < world_size and ny >= 0 and ny < world_size:
			neighbor_size = get_cactus_size(nx, ny)
			
			if neighbor_size != None:
				if neighbor_size == current_size + 1 or neighbor_size == current_size - 1:
					return True
	
	return False

def find_best_cactus_to_harvest():
	world_size = get_world_size()
	best_x = -1
	best_y = -1
	
	for x in range(world_size):
		for y in range(world_size):
			if check_sorted_chain(x, y):
				best_x = x
				best_y = y
				return best_x, best_y
	
	return best_x, best_y

def harvest_sorted_cactus():
	x, y = find_best_cactus_to_harvest()
	if x != -1:
		goto_pos(x, y)
		harvest()
		plant(Entities.Cactus)
		water_and_fertilize()
	return_to_spawn()

def setup_cactus_farm():
	clear_map()
	till_entire_map()
	return_to_spawn()

setup_cactus_farm()

while True:
	traverse_map_snake(farm_cactus_callback)
	harvest_sorted_cactus()
	return_to_spawn()