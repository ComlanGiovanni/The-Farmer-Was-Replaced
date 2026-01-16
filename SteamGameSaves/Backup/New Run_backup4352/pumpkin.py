from navigation import goto_pos, move_to_origin
from sorting import quicksort_tuples
from farming import *

def plant_pumpkin_map():
	move_to_origin()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			fast_harvest()
			if get_entity_type() != Entities.Pumpkin:
				till()
				plant(Entities.Pumpkin)
			
			if num_items(Items.Water) > 1 and get_water() < 0.75:
				while get_water() < 0.75:
					use_item(Items.Water)
			
			if num_items(Items.Fertilizer) > 1:
				use_item(Items.Fertilizer)
			
			move(North)
		move(East)

def is_pumpkin_dead():
	return get_entity_type() == Entities.Dead_Pumpkin and not can_harvest()

def check_and_replant_dead():
	move_to_origin()
	has_dead = False
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if is_pumpkin_dead():
				plant(Entities.Pumpkin)
				use_water_and_fertilizer()
				has_dead = True
			move(North)
		move(East)
	
	return has_dead

def get_first_pumpkin_id():
	world_size = get_world_size()
	
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			entity = get_entity_type()
			
			if entity == Entities.Pumpkin:
				first_id = measure()
				if first_id != None:
					move_to_origin()
					return first_id
	
	move_to_origin()
	return None

def check_pumpkin_ids_row(first_id):
	world_size = get_world_size()
	
	for i in range(world_size):
		entity = get_entity_type()
		
		if entity != Entities.Pumpkin:
			return False
		
		current_id = measure()
		
		if current_id == None or current_id != first_id:
			return False
		
		if i < world_size - 1:
			move(East)
	
	return True

def is_mega_pumpkin(first_id):
	if first_id == None:
		return False
	
	move_to_origin()
	world_size = get_world_size()
	
	for row in range(world_size):
		result = check_pumpkin_ids_row(first_id)
		
		if not result:
			move_to_origin()
			return False
		
		if row < world_size - 1:
			move_to_origin()
			for _ in range(row + 1):
				move(North)
	
	move_to_origin()
	return True

def farm_mega_pumpkin():
	plant_pumpkin_map()
	
	max_iterations = 50
	iteration = 0
	
	while iteration < max_iterations:
		iteration += 1
		
		has_dead = check_and_replant_dead()
		
		if not has_dead:
			first_id = get_first_pumpkin_id()
			
			if first_id != None and is_mega_pumpkin(first_id):
				move_to_origin()
				harvest()
				return True
	
	return False