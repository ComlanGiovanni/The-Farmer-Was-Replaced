# UNIFIED FARM - Tous les farms en boucle infinie
# Optimisé avec companions et multi-drones

clear()
change_hat(Hats.Brown_Hat)

# ========== UTILITY FUNCTIONS ==========

def wait_for_all_drones():
	while num_drones() > 1:
		pass

def move_to(x, y):
	while get_pos_x() < x:
		move(East)
	while get_pos_x() > x:
		move(West)
	while get_pos_y() < y:
		move(North)
	while get_pos_y() > y:
		move(South)

# ========== HAY FARM WITH COMPANIONS ==========

def farm_hay():
	world_size = get_world_size()
	companion_mapping = {}
	hay_mapping = {}
	
	def track_companion(curr_x, curr_y):
		result = get_companion()
		if result == None:
			return False
		
		target_entity, (target_x, target_y) = result
		
		if (target_x, target_y) not in companion_mapping:
			companion_mapping[(target_x, target_y)] = target_entity
			hay_mapping[(curr_x, curr_y)] = (target_x, target_y)
			return True
		return False
	
	def drone_hay_task():
		for i in range(2):
			for j in range(world_size):
				curr_x = get_pos_x()
				curr_y = get_pos_y()
				
				harvest()
				
				if get_ground_type() == Grounds.Soil:
					till()
				
				if (curr_x, curr_y) in companion_mapping:
					target_entity = companion_mapping[(curr_x, curr_y)]
					
					if target_entity == Entities.Carrot:
						if get_ground_type() != Grounds.Soil:
							till()
						plant(Entities.Carrot)
					elif target_entity != Entities.Grass:
						plant(target_entity)
				else:
					if (curr_x, curr_y) in hay_mapping:
						companion_pos = hay_mapping.pop((curr_x, curr_y))
						if companion_pos in companion_mapping:
							companion_mapping.pop(companion_pos)
					
					track_companion(curr_x, curr_y)
				move(North)
	
	move_to(0, 0)
	for i in range(world_size - 1):
		spawn_drone(drone_hay_task)
		move(East)
	drone_hay_task()

# ========== WOOD FARM WITH COMPANIONS ==========

def farm_wood():
	world_size = get_world_size()
	companion_mapping = {}
	tree_mapping = {}
	
	def tree_tile(curr_x, curr_y):
		return curr_x % 2 == curr_y % 2
	
	def track_companion(curr_x, curr_y):
		result = get_companion()
		if result == None:
			return False
		
		target_entity, (target_x, target_y) = result
		
		if (target_x, target_y) not in companion_mapping:
			companion_mapping[(target_x, target_y)] = target_entity
			tree_mapping[(curr_x, curr_y)] = (target_x, target_y)
			return True
		return False
	
	def drone_tree_task():
		for i in range(2):
			for j in range(world_size):
				curr_x = get_pos_x()
				curr_y = get_pos_y()
				
				if tree_tile(curr_x, curr_y):
					if can_harvest():
						harvest()
						plant(Entities.Tree)
					
					if (curr_x, curr_y) in tree_mapping:
						companion_pos = tree_mapping.pop((curr_x, curr_y))
						if companion_pos in companion_mapping:
							companion_mapping.pop(companion_pos)
					
					track_companion(curr_x, curr_y)
					
					if get_water() < 0.40:
						use_item(Items.Water)
				
				elif (curr_x, curr_y) in companion_mapping:
					target_entity = companion_mapping[(curr_x, curr_y)]
					harvest()
					
					if target_entity == Entities.Grass:
						if get_ground_type() != Grounds.Grassland:
							till()
					elif target_entity == Entities.Carrot:
						if get_ground_type() != Grounds.Soil:
							till()
					
					plant(target_entity)
				else:
					harvest()
					plant(Entities.Bush)
				
				move(North)
	
	move_to(0, 0)
	for i in range(world_size - 1):
		spawn_drone(drone_tree_task)
		move(East)
	drone_tree_task()

# ========== CARROT FARM WITH COMPANIONS ==========

def farm_carrots():
	world_size = get_world_size()
	companion_mapping = {}
	carrot_mapping = {}
	
	def track_companion(curr_x, curr_y):
		result = get_companion()
		if result == None:
			return False
		
		target_entity, (target_x, target_y) = result
		
		if (target_x, target_y) not in companion_mapping:
			companion_mapping[(target_x, target_y)] = target_entity
			carrot_mapping[(curr_x, curr_y)] = (target_x, target_y)
			return True
		return False
	
	def prepare_and_plant(entity_type):
		if entity_type in (Entities.Carrot, Entities.Bush, Entities.Tree) and get_ground_type() != Grounds.Soil:
			till()
		plant(entity_type)
	
	def drone_carrot_task():
		for i in range(2):
			for j in range(world_size):
				curr_x = get_pos_x()
				curr_y = get_pos_y()
				
				harvest()
				
				if (curr_x, curr_y) in companion_mapping:
					target_entity = companion_mapping[(curr_x, curr_y)]
					prepare_and_plant(target_entity)
					
					if target_entity == Entities.Carrot and get_water() < 0.10:
						use_item(Items.Water)
				
				elif (curr_x, curr_y) in carrot_mapping:
					prepare_and_plant(Entities.Carrot)
					
					if get_water() < 0.10:
						use_item(Items.Water)
					
					companion_pos = carrot_mapping.pop((curr_x, curr_y))
					if companion_pos in companion_mapping:
						companion_mapping.pop(companion_pos)
					
					track_companion(curr_x, curr_y)
				else:
					prepare_and_plant(Entities.Carrot)
					
					if get_water() < 0.10:
						use_item(Items.Water)
					
					track_companion(curr_x, curr_y)
				move(North)
	
	move_to(0, 0)
	for i in range(world_size - 1):
		spawn_drone(drone_carrot_task)
		move(East)
	drone_carrot_task()

# ========== SUNFLOWER FARM ==========

def farm_sunflowers():
	world_size = get_world_size()
	
	def harvest_column():
		for i in range(64):
			if get_pos_y() != 0:
				move_to(get_pos_x(), 0)
			
			for _ in range(world_size):
				if get_ground_type() != Grounds.Soil:
					till()
				
				if get_water() < 0.75:
					use_item(Items.Water)
				
				if can_harvest():
					harvest()
				
				if get_entity_type() == None:
					plant(Entities.Sunflower)
				
				move(North)
	
	move_to(0, 0)
	for i in range(world_size - 1):
		spawn_drone(harvest_column)
		move(East)
	harvest_column()

# ========== PUMPKIN FARM ==========

def farm_pumpkins():
	world_size = get_world_size()
	needs_till = True
	
	def check_pumpkin():
		if get_pos_x() != 0:
			move(East)
		
		left_id = measure()
		move(West)
		right_id = measure()
		move(East)
		
		return left_id == right_id
	
	def check_done():
		return measure() == measure(South)
	
	def drone_plant_loop():
		if needs_till:
			for _ in range(world_size):
				till()
				move(North)
		
		for _ in range(world_size):
			plant(Entities.Pumpkin)
			move(North)
		
		while not check_done():
			for _ in range(world_size):
				while not can_harvest():
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
					use_item(Items.Fertilizer)
				move(North)
	
	move_to(0, 0)
	for _ in range(world_size - 1):
		spawn_drone(drone_plant_loop)
		move(East)
	drone_plant_loop()
	
	wait_for_all_drones()
	harvest()
	move(East)

# ========== CACTUS FARM WITH SORTING ==========

def farm_cactus():
	world_size = get_world_size()
	hats = [Hats.Green_Hat, Hats.Purple_Hat]
	
	def move_to_x(x_target):
		while get_pos_x() < x_target:
			move(East)
		while get_pos_x() > x_target:
			move(West)
	
	def move_to_y(y_target):
		while get_pos_y() < y_target:
			move(North)
		while get_pos_y() > y_target:
			move(South)
	
	def drone_plant_cacti():
		change_hat(hats[get_pos_x() % 2])
		for j in range(world_size):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			move(North)
	
	def shake_col():
		change_hat(hats[get_pos_x() % 2])
		left = 0
		right = world_size - 1
		
		while left < right:
			move_to_y(left)
			loc_last_swap = left
			y_curr = get_pos_y()
			
			while y_curr < right:
				if measure() > measure(North):
					swap(North)
					loc_last_swap = y_curr
				move(North)
				y_curr += 1
			
			right = loc_last_swap
			if left >= right:
				break
			
			move_to_y(right)
			loc_last_swap = right
			y_curr = get_pos_y()
			
			while y_curr > left:
				if measure(South) > measure():
					swap(South)
					loc_last_swap = y_curr
				move(South)
				y_curr -= 1
			
			left = loc_last_swap
	
	def shake_row():
		change_hat(hats[get_pos_y() % 2])
		left = 0
		right = world_size - 1
		
		while left < right:
			move_to_x(left)
			loc_last_swap = left
			x_curr = get_pos_x()
			
			while x_curr < right:
				if measure() > measure(East):
					swap(East)
					loc_last_swap = x_curr
				move(East)
				x_curr += 1
			
			right = loc_last_swap
			if left >= right:
				break
			
			move_to_x(right)
			loc_last_swap = right
			x_curr = get_pos_x()
			
			while x_curr > left:
				if measure(West) > measure():
					swap(West)
					loc_last_swap = x_curr
				move(West)
				x_curr -= 1
			
			left = loc_last_swap
	
	move_to(0, 0)
	for i in range(world_size - 1):
		spawn_drone(drone_plant_cacti)
		move(East)
	drone_plant_cacti()
	wait_for_all_drones()
	
	move_to(0, 0)
	for i in range(world_size - 1):
		spawn_drone(shake_col)
		move(East)
	shake_col()
	wait_for_all_drones()
	
	move_to(0, 0)
	for i in range(world_size - 1):
		spawn_drone(shake_row)
		move(North)
	shake_row()
	wait_for_all_drones()
	
	harvest()

# ========== MAZE FARM ==========

def farm_maze():
	ALL_DIRECTIONS = [North, South, East, West]
	
	def opposite_direction(direction):
		if direction == North:
			return South
		elif direction == East:
			return West
		elif direction == South:
			return North
		elif direction == West:
			return East
	
	def explore_option_iterative(start_direction, drone_id):
		if not move(start_direction):
			return False
		
		path_stack = [(start_direction, 0)]
		
		while path_stack:
			if get_entity_type() == Entities.Treasure:
				harvest()
				return True
			
			last_move_direction, next_dir_index = path_stack[-1]
			
			while next_dir_index < len(ALL_DIRECTIONS):
				explore_direction = ALL_DIRECTIONS[next_dir_index]
				path_stack[-1] = (last_move_direction, next_dir_index + 1)
				
				if opposite_direction(explore_direction) != last_move_direction:
					if move(explore_direction):
						path_stack.append((explore_direction, 0))
						break
				
				next_dir_index += 1
			
			if next_dir_index == len(ALL_DIRECTIONS):
				path_stack.pop()
				move(opposite_direction(last_move_direction))
		
		move(opposite_direction(start_direction))
		return False
	
	def search_drone(drone_id):
		dirs = ALL_DIRECTIONS
		if drone_id % 2:
			dirs = dirs[::-1]
		
		while True:
			for direction in dirs:
				if explore_option_iterative(direction, drone_id):
					break
	
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
	for i in range(max_drones() - 1):
		spawn_drone(search_drone(i))
	
	search_drone(0)

# ========== MAIN LOOP ==========

while True:
	clear()
	
	farm_hay()
	wait_for_all_drones()
	
	clear()
	
	farm_wood()
	wait_for_all_drones()
	
	clear()
	
	farm_carrots()
	wait_for_all_drones()
	
	clear()
	
	farm_pumpkins()
	wait_for_all_drones()
	
	clear()
	
	farm_cactus()
	wait_for_all_drones()
	
	clear()
	
	farm_sunflowers()
	wait_for_all_drones()

	clear()