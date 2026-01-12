from lib import *

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
	return center_id == first_id

return_to_spawn()
clear_map()
till_entire_map()
plant_all_pumpkins()
first_id = get_first_pumpkin_id()

while True:
	if not check_and_replant_dead():
		if is_mega_pumpkin(first_id):
			harvest()
			break