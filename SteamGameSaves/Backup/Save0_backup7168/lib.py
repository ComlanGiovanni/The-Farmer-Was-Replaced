# UTILITY FUNCTIONS - Navigation & Position

def print_position():
	print(get_pos_x())
	print(get_pos_y())

##
#optimisation possilbe si le robot est deja a 
##
def return_to_spawn():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def is_even(n):
	return n % 2 == 0

def till_ground():
	if get_ground_type() != Grounds.Soil:
		till()

def goto_pos(target_x, target_y):
	current_x = get_pos_x()
	current_y = get_pos_y()
	
	# Déplacement horizontal
	if current_x < target_x:
		for i in range(target_x - current_x):
			move(East)
	elif current_x > target_x:
		for i in range(current_x - target_x):
			move(West)
	
	# Déplacement vertical
	if current_y < target_y:
		for i in range(target_y - current_y):
			move(North)
	elif current_y > target_y:
		for i in range(current_y - target_y):
			move(South)

# UTILITY FUNCTIONS - Resources

def watering_grounds(threshold=0.95):
	if num_items(Items.Water) > 2000:
		while get_water() < threshold:
			use_item(Items.Water)

def fertilize():
	if num_items(Items.Fertilizer) > 20000:
		use_item(Items.Fertilizer)

def water_and_fertilize():
	watering_grounds()
	fertilize()

def till_ground():
	if get_ground_type() != Grounds.Soil:
		till()
# MAP TRAVERSAL

def traverse_map_snake(action_callback):
	world_size = get_world_size()
	
	for col in range(world_size):
		if col % 2 == 0:
			direction = North
		else:
			direction = South
		
		for row in range(world_size):
			x, y = get_pos_x(), get_pos_y()
			action_callback(x, y)
			
			if row < world_size - 1:
				move(direction)
		
		if col < world_size - 1:
			move(East)

def traverse_map_snake_simple():
	world_size = get_world_size()
	
	for col in range(world_size):
		if col % 2 == 0:
			direction = North
		else:
			direction = South
		
		for row in range(world_size):
			if row < world_size - 1:
				move(direction)
		
		if col < world_size - 1:
			move(East)	

def traverse_map_spiral(action_callback):
	return_to_spawn()
	world_size = get_world_size()
	
	x = 0
	y = 0
	dx = 1
	dy = 0
	
	visited = set()
	
	for i in range(world_size * world_size):
		action_callback(x, y)
		visited.add((x, y))
		
		# Calculer la prochaine position
		next_x = x + dx
		next_y = y + dy
		
		# Vérifier si on doit tourner
		if (next_x < 0 or next_x >= world_size or 
			next_y < 0 or next_y >= world_size or 
			(next_x, next_y) in visited):
			# Tourner à droite (90 degrés dans le sens horaire)
			if dx == 1 and dy == 0:
				dx, dy = 0, 1
			elif dx == 0 and dy == 1:
				dx, dy = -1, 0
			elif dx == -1 and dy == 0:
				dx, dy = 0, -1
			elif dx == 0 and dy == -1:
				dx, dy = 1, 0
		
		# Avancer dans la nouvelle direction
		x += dx
		y += dy
		
		# Se déplacer physiquement
		if i < world_size * world_size - 1:
			if dx == 1:
				move(East)
			elif dx == -1:
				move(West)
			elif dy == 1:
				move(North)
			elif dy == -1:
				move(South)

def traverse_map_spiral_simple():
	return_to_spawn()
	world_size = get_world_size()
	
	x = 0
	y = 0
	dx = 1
	dy = 0
	
	visited = set()
	
	for i in range(world_size * world_size):
		visited.add((x, y))
		
		next_x = x + dx
		next_y = y + dy
		
		if (next_x < 0 or next_x >= world_size or 
			next_y < 0 or next_y >= world_size or 
			(next_x, next_y) in visited):
			if dx == 1 and dy == 0:
				dx, dy = 0, 1
			elif dx == 0 and dy == 1:
				dx, dy = -1, 0
			elif dx == -1 and dy == 0:
				dx, dy = 0, -1
			elif dx == 0 and dy == -1:
				dx, dy = 1, 0
		
		x += dx
		y += dy
		
		if i < world_size * world_size - 1:
			if dx == 1:
				move(East)
			elif dx == -1:
				move(West)
			elif dy == 1:
				move(North)
			elif dy == -1:
				move(South)
# MAP OPERATIONS

def execute_on_all_tiles(action_callback, clear_entities=True):
	def tile_action(x, y):
		harvest_if_ready()
		if clear_entities:
			entity = get_entity_type()
			if entity != None:
				harvest()
		if action_callback != None:
			action_callback(x, y)
	
	traverse_map_snake(tile_action)
	return_to_spawn()

# Utilisation avec des fonctions normales
def do_nothing():
	pass

def till_tile(x, y):
	till_ground()

def clear_map():
	execute_on_all_tiles(do_nothing())

def till_entire_map():
	execute_on_all_tiles(till_tile)

##
#clear_map and till_entier_map have same code
#i think i should make one function for it and call it 
#for both right ?
##

# CROP MANAGEMENT - Generic

def handle_crop(crop_type):
	harvest_if_ready()
	if get_entity_type() != crop_type:
		plant(crop_type)
	watering_grounds()
	fertilize()

def harvest_if_ready():
	if can_harvest():
		harvest()			
#
		
		
def handle_tree():
	harvest_if_ready()
	if get_entity_type() != Entities.Tree:
		plant(Entities.Tree)
	water_and_fertilize()

def farm_trees_checkerboard(x, y):
	if not is_even(x + y):
		handle_tree()
		
def handle_pumpkin():
	entity = get_entity_type()
	
	if can_harvest():
		harvest()
	
	if entity == Entities.Dead_Pumpkin or entity == None:
		plant(Entities.Pumpkin)
	
	water_and_fertilize()

#mofier world_size pour la taille de la farm voulue
def farm_pumpkin_grid():
	world_size = get_world_size()
	return_to_spawn()
	
	while True:
		for x in range(world_size):
			for y in range(world_size):
				goto_pos(x, y)
				handle_pumpkin()
		return_to_spawn()


def handle_carrot():
	harvest_if_ready()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	water_and_fertilize()

def farm_carrot_callback(x, y):
	handle_carrot()
	
def handle_grass():
	harvest_if_ready()
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	water_and_fertilize()

def farm_grass_callback(x, y):
	handle_grass()

def reset_for_next_farm():
	clear_map()
	return_to_spawn()
	do_a_flip()	