# ADVANCED.PY - Algorithmes avancés
# Mega pumpkin, sunflower optimization, maze solving, cactus sorting

from core import *
from farming import *
from callback import *
from multidrone import *

# ========== SUNFLOWERS ==========

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

def farm_sunflowers():
	for i in range(2):
		farm_with_drones(farm_sunflower_callback)
	
	if count_sunflowers() >= 10:
		harvest_best_sunflower()

# ========== PUMPKINS ==========

def get_first_pumpkin_id():
	world_size = get_world_size()
	
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			entity = get_entity_type()
			
			if entity == Entities.Pumpkin:
				first_id = measure()
				return_to_spawn()
				return first_id
	
	return_to_spawn()
	return None

def farm_mega_pumpkin():
	plant_all_pumpkins_with_drones()
	
	max_iterations = 50
	iteration = 0
	
	while iteration < max_iterations:
		iteration += 1
		
		has_dead = check_and_replant_dead_with_drones()
		
		if not has_dead:
			first_id = get_first_pumpkin_id()
			
			if first_id != None and is_mega_pumpkin_with_drones(first_id):
				harvest()
				return

# ========== CACTUS ==========

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

def farm_cactus():
	for i in range(2):
		farm_with_drones(farm_cactus_callback)
	harvest_sorted_cactus()

# ========== MAZE ==========

def create_maze():
	return_to_spawn()
	till_entire_map_with_drones()
	return_to_spawn()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def turn_right(direction_index):
	return (direction_index + 1) % 4

def turn_left(direction_index):
	return (direction_index - 1) % 4

def solve_maze_wall_follower():
	directions = [North, East, South, West]
	direction_index = 0
	
	while get_entity_type() != Entities.Treasure:
		right_index = turn_right(direction_index)
		
		if can_move(directions[right_index]):
			direction_index = right_index
			move(directions[direction_index])
		elif can_move(directions[direction_index]):
			move(directions[direction_index])
		else:
			direction_index = turn_left(direction_index)
	
	harvest()

def farm_maze():
	create_maze()
	solve_maze_wall_follower()