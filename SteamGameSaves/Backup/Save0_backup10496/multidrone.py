from core import *

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
def farm_with_drones(callback):
	return_to_spawn()
	world_size = get_world_size()
	drones = []
	
	def farm_row():
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
	
def farm_row():
	for i in range(world_size):
		x = get_pos_x()
		y = get_pos_y()
		callback(x, y)
		if i < world_size - 1:
			move(East)
				
def plant_pumpkin_row():
	world_size = get_world_size()
	for i in range(world_size):
		plant(Entities.Pumpkin)
		water_and_fertilize()
		if i < world_size - 1:
			move(East)
			
def plant_all_pumpkins_with_drones():
	return_to_spawn()
	world_size = get_world_size()
	drones = []
	
	for row in range(world_size):
		drone = spawn_drone(plant_pumpkin_row)
		if drone != None:
			drones.append(drone)
		else:
			plant_pumpkin_row()
		if row < world_size - 1:
			move(North)
	
	for drone in drones:
		wait_for(drone)
	
	return_to_spawn()

def check_and_replant_dead_row():
	world_size = get_world_size()
	has_dead = False
	
	for i in range(world_size):
		entity = get_entity_type()
		
		if entity == Entities.Dead_Pumpkin:
			has_dead = True
			plant(Entities.Pumpkin)
			water_and_fertilize()
		
		if i < world_size - 1:
			move(East)
	
	return has_dead

def check_and_replant_dead_with_drones():
	return_to_spawn()
	world_size = get_world_size()
	drones = []
	
	for row in range(world_size):
		drone = spawn_drone(check_and_replant_dead_row)
		if drone != None:
			drones.append(drone)
		else:
			check_and_replant_dead_row()
		if row < world_size - 1:
			move(North)
	
	results = []
	for drone in drones:
		result = wait_for(drone)
		if result:
			results.append(result)
	
	return_to_spawn()
	return len(results) > 0
	
def check_pumpkin_ids_row(first_id):
	world_size = get_world_size()
	
	for i in range(world_size):
		entity = get_entity_type()
		
		if entity == Entities.Pumpkin:
			pumpkin_id = measure()
			if pumpkin_id != first_id:
				return False
		
		if i < world_size - 1:
			move(East)

def is_mega_pumpkin_with_drones(first_id):
	if first_id == None:
		return False
	
	return_to_spawn()
	world_size = get_world_size()
	drones = []
	
	def check_row():
		return check_pumpkin_ids_row(first_id)
	
	for row in range(world_size):
		drone = spawn_drone(check_row)
		if drone != None:
			drones.append(drone)
		else:
			result = check_row()
			if not result:
				return_to_spawn()
				return False
		if row < world_size - 1:
			move(North)
	
	for drone in drones:
		result = wait_for(drone)
		if not result:
			return_to_spawn()
			return False
	
	return_to_spawn()
	return True

