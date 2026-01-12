from lib import *

while True:
	do_a_flip()
	print("start")
	do_a_flip()
	for i in range(2):
		traverse_map_snake(farm_grass_callback)
	reset_for_next_farm()
	do_a_flip()
	for i in range(2):
		traverse_map_snake(farm_trees_checkerboard)
	reset_for_next_farm()
	do_a_flip()
	for i in range(2):
		traverse_map_snake(farm_carrot_callback)
	reset_for_next_farm()
	do_a_flip()
	
	
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
	
	for i in range(2):
		traverse_map_snake(farm_sunflower_callback)
	
	if count_sunflowers() >= 10:
			harvest_best_sunflower()
		
	reset_for_next_farm()
	do_a_flip()
	
	
	#
	
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
		do_a_flip()
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
		print("-")
		print(first_id)
		return center_id == first_id
	
	reset_for_next_farm()
	do_a_flip()
	plant_all_pumpkins()
	first_id = get_first_pumpkin_id()
	
	while True:
		if not check_and_replant_dead():
			if is_mega_pumpkin(first_id):
				harvest()
				break
	
	reset_for_next_farm()
	
	#
	
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
	
	reset_for_next_farm()
	do_a_flip()
	for i in range(2):
		traverse_map_snake(farm_cactus_callback)
	harvest_sorted_cactus()
	reset_for_next_farm()
	do_a_flip()
	print("end")