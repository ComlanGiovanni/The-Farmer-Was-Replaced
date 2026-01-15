# CORE.PY - Utilitaires de base
# Navigation, ressources, helpers

def return_to_spawn():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def goto_pos(target_x, target_y):
	current_x = get_pos_x()
	current_y = get_pos_y()
	
	if current_x < target_x:
		for i in range(target_x - current_x):
			move(East)
	elif current_x > target_x:
		for i in range(current_x - target_x):
			move(West)
	
	if current_y < target_y:
		for i in range(target_y - current_y):
			move(North)
	elif current_y > target_y:
		for i in range(current_y - target_y):
			move(South)

def print_position():
	print(get_pos_x())
	print(get_pos_y())

def is_even(n):
	return n % 2 == 0

def till_ground():
	if get_ground_type() != Grounds.Soil:
		till()

def watering_grounds(threshold=0.95):
	if num_items(Items.Water) > 200:
		while get_water() < threshold:
			use_item(Items.Water)

def fertilize():
	if num_items(Items.Fertilizer) > 200:
		use_item(Items.Fertilizer)

def water_and_fertilize():
	watering_grounds()
	fertilize()

def harvest_if_ready():
	if can_harvest():
		harvest()

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