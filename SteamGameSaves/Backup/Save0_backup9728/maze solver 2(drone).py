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

while True:
	create_maze()
	solve_maze_wall_follower()