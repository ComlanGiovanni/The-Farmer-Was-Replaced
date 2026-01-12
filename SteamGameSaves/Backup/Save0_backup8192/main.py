from lib import *

def till_row():
	world_size = get_world_size()
	for i in range(world_size):
		if get_ground_type() != Grounds.Soil:
			till()
		if i < world_size - 1:
			move(East)

def till_entire_map_with_drones():
	return_to_spawn()
	world_size = get_world_size()
	drones = []
	
	for row in range(world_size):
		drone = spawn_drone(till_row)
		if drone != None:
			drones.append(drone)
		else:
			till_row()
		if row < world_size - 1:
			move(North)
	
	for drone in drones:
		wait_for(drone)
	
	return_to_spawn()

def clear_map_with_drones():
	return_to_spawn()
	world_size = get_world_size()
	drones = []
	
	def clear_row():
		for i in range(world_size):
			harvest_if_ready()
			entity = get_entity_type()
			if entity != None:
				harvest()
			if i < world_size - 1:
				move(East)
	
	for row in range(world_size):
		drone = spawn_drone(clear_row)
		if drone != None:
			drones.append(drone)
		else:
			clear_row()
		if row < world_size - 1:
			move(North)
	
	for drone in drones:
		wait_for(drone)
	
	return_to_spawn()

def farm_with_drones(callback):
	return_to_spawn()
	world_size = get_world_size()
	drones = []
	
	def farm_row():
		do_a_flip()
		for i in range(world_size):
			x = get_pos_x()
			y = get_pos_y()
			callback(x, y)
			if i < world_size - 1:
				move(East)
	
	for row in range(world_size):
		drone = spawn_drone(farm_row)
		if drone != None:
			drones.append(drone)
		else:
			farm_row()
		if row < world_size - 1:
			move(North)
	
	for drone in drones:
		wait_for(drone)
	
	return_to_spawn()

def handle_grass():
	harvest_if_ready()
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	water_and_fertilize()

def farm_grass_callback(x, y):
	handle_grass()

def handle_tree():
	harvest_if_ready()
	if get_entity_type() != Entities.Tree:
		plant(Entities.Tree)
	water_and_fertilize()

def farm_trees_checkerboard(x, y):
	if not is_even(x + y):
		handle_tree()

def handle_carrot():
	harvest_if_ready()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	water_and_fertilize()

def farm_carrot_callback(x, y):
	handle_carrot()

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

def farm_sunflowers():
	for i in range(2):
		farm_with_drones(farm_sunflower_callback)
	
	if count_sunflowers() >= 10:
		harvest_best_sunflower()

def plant_all_pumpkins():
	world_size = get_world_size()
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			plant(Entities.Pumpkin)
			water_and_fertilize()
	return_to_spawn()

def check_and_replant_dead():
	world_size = get_world_size()
	has_dead = False
	
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			entity = get_entity_type()
			
			if entity == Entities.Dead_Pumpkin:
				has_dead = True
				plant(Entities.Pumpkin)
				water_and_fertilize()
	
	return_to_spawn()
	return has_dead

def get_first_pumpkin_id():
	goto_pos(0, 0)
	first_id = measure()
	return_to_spawn()
	return first_id

def is_mega_pumpkin(first_id):
	world_size = get_world_size()
	goto_pos(world_size // 2, world_size // 2)
	center_id = measure()
	return_to_spawn()
	print(center_id)
	print(first_id)
	return center_id == first_id

def farm_mega_pumpkin():
	plant_all_pumpkins()
	first_id = get_first_pumpkin_id()
	
	while True:
		if not check_and_replant_dead():
			if is_mega_pumpkin(first_id):
				harvest()
				break

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

while True:
	clear_map_with_drones()
	till_entire_map_with_drones()
	
	for i in range(2):
		farm_with_drones(farm_grass_callback)
	
	clear_map_with_drones()
	till_entire_map_with_drones()
	
	for i in range(2):
		farm_with_drones(farm_trees_checkerboard)
	
	clear_map_with_drones()
	till_entire_map_with_drones()
	
	for i in range(2):
		farm_with_drones(farm_carrot_callback)
	
	clear_map_with_drones()
	till_entire_map_with_drones()
	
	farm_sunflowers()
	
	clear_map_with_drones()
	till_entire_map_with_drones()
	
	farm_mega_pumpkin()
	
	clear_map_with_drones()
	till_entire_map_with_drones()
	
	farm_cactus()
	till_entire_map_with_drones()
	farm_maze()