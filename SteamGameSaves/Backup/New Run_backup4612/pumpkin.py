from navigation import goto_pos, move_to_origin
from sorting import quicksort_tuples
from farming import *

def plant_pumpkin_map():
	move_to_origin()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() != Entities.Pumpkin:
				if get_ground_type() != Grounds.Soil:
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
	return get_entity_type() == Entities.Dead_Pumpkin

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

def farm_mega_pumpkin():
	plant_pumpkin_map()
	
	while True:
		has_dead = check_and_replant_dead()
		
		if not has_dead:
			move_to_origin()
			harvest()
			return True