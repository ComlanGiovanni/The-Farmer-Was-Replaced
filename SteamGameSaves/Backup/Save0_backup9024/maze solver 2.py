from lib import *

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

def solve_maze_with_measure():
	treasure_pos = measure()
	treasure_x = treasure_pos[0]
	treasure_y = treasure_pos[1]
	
	visited = set()
	path = []
	
	def backtrack():
		if len(path) > 0:
			last_dir = path.pop()
			opposite = [South, West, North, East]
			move(opposite[last_dir])
	
	directions = [North, East, South, West]
	
	while get_entity_type() != Entities.Treasure:
		current_x = get_pos_x()
		current_y = get_pos_y()
		visited.add((current_x, current_y))
		
		moved = False
		for i in range(4):
			if can_move(directions[i]):
				next_x = current_x
				next_y = current_y
				
				if directions[i] == North:
					next_y += 1
				elif directions[i] == South:
					next_y -= 1
				elif directions[i] == East:
					next_x += 1
				elif directions[i] == West:
					next_x -= 1
				
				if (next_x, next_y) not in visited:
					move(directions[i])
					path.append(i)
					moved = True
					break
		
		if not moved:
			backtrack()
	
	harvest()

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