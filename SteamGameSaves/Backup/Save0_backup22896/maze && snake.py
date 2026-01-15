world_size = get_world_size()
world_size_minus_one = world_size - 1

edge_positions = [0, world_size_minus_one]

offlimit_columns_stage1 = {
}
offlimit_columns_stage2 = {
}
clear()
change_hat(Hats.Dinosaur_Hat)
apple_pos = measure()
squares_occupied = 1
game_complete = False
aggressive_stage = True


def measure_apple():
	global apple_pos
	global squares_occupied
	global apple_pos_queue
	apple_pos = measure()
	squares_occupied += 1
	
def move_and_check_apple(direction):
	global apple_pos

	if not move(direction):
		return False
	if (get_pos_x(), get_pos_y()) == apple_pos:
		measure_apple()

	return True

def move_to_col(target_x_pos, do_measure=True):
	global world_size
	global apple_pos
	curr_x = get_pos_x()
	
	direction = West
	if curr_x < target_x_pos:
		direction = East
	
	for x in range(abs(target_x_pos - curr_x)):
		this_check = move
		if do_measure:
			this_check = move_and_check_apple 
		if not this_check(direction):
			return False
	
	return True

def move_to_row(target_y_pos, do_measure=True):
	global world_size
	global apple_pos
	curr_y = get_pos_y()
	
	direction = South
	if curr_y < target_y_pos:
		direction = North
		
	for y in range(abs(target_y_pos - curr_y)):
		this_check = move
		if do_measure:
			this_check = move_and_check_apple 
		if not this_check(direction):
			return False
	
	return True

def transition_to_stage_2():
	global offlimit_columns_stage1
	global world_size
	global world_size_minus_one
	
	move_to_col(world_size_minus_one)
	move_to_row(0)
	
	offlimit_columns_stage1 = {
	}
	
	return False

def transition_to_stage_1():
	global offlimit_columns_stage2
	global world_size
	global world_size_minus_one
	
	move_to_col(0)
	move_to_row(world_size_minus_one)
	
	offlimit_columns_stage2 = {
	}
	
	return False

def stage_1_apple_collect():
	global apple_pos
	global world_size
	global offlimit_columns_stage1
	global offlimit_columns_stage2
	global world_size_minus_one
	
	apple_pos_x, apple_pos_y = apple_pos
	if apple_pos_y == 0 or apple_pos_x in edge_positions or (apple_pos_x in offlimit_columns_stage1 and apple_pos_y <= offlimit_columns_stage1[apple_pos_x]):
		return transition_to_stage_2()
	else:
		apple_x_odd = apple_pos_x % 2
		target_x_pos = apple_pos_x 
		if not apple_x_odd:
			target_x_pos = apple_pos_x - 1
		
		if target_x_pos <= get_pos_x():
			return transition_to_stage_2()
		else:
			move_to_col(target_x_pos)
			move_to_row(apple_pos_y)
			offlimit_columns_stage2[target_x_pos] = apple_pos_y
			offlimit_columns_stage2[target_x_pos + 1] = apple_pos_y
			move_and_check_apple(East)
			move_to_row(world_size_minus_one)
	
	return True

def stage_2_apple_collect():
	global apple_pos
	global world_size
	global offlimit_columns_stage1
	global offlimit_columns_stage2
	global world_size_minus_one
	
	apple_pos_x, apple_pos_y = apple_pos
	if apple_pos_y == world_size_minus_one or apple_pos_x in edge_positions or (apple_pos_x in offlimit_columns_stage2 and apple_pos_y >= offlimit_columns_stage2[apple_pos_x]):
		return transition_to_stage_1()
	else:
		apple_x_odd = apple_pos_x % 2
		target_x_pos = apple_pos_x 
		if apple_x_odd:
			target_x_pos = apple_pos_x + 1
		
		if target_x_pos >= get_pos_x():
			return transition_to_stage_1()
		else:
			move_to_col(target_x_pos)
			move_to_row(apple_pos_y)
			offlimit_columns_stage1[target_x_pos] = apple_pos_y
			offlimit_columns_stage1[target_x_pos - 1] = apple_pos_y
			move_and_check_apple(West)
			move_to_row(0)
	
	return True

def move_to_right_col_wavy():
	global world_size
	global world_size_minus_one
	global offlimit_columns_stage1

	# Assume curr x is zero
	for x in range(world_size):
		if x % 2:
			target_y = 1
			if x in offlimit_columns_stage1:
				target_y = offlimit_columns_stage1[x] + 1
			while get_pos_y() != target_y:
				move(South)
			move(East)
		else: # x is even, go up to top row, then move right
			while get_pos_y() != world_size_minus_one:
				move(North)
			move(East)

def find_top_left():
	global world_size_minus_one
	
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() < world_size_minus_one:
		move(North)
	

def transition_to_route():
	find_top_left()
	move_to_right_col_wavy()
	while get_pos_y() != 0:
		move(South)
	while get_pos_x() != 0:
		move(West)
	

# STAGE 1
move_to_row(world_size_minus_one)

while aggressive_stage:
	while stage_1_apple_collect() and get_pos_x() < world_size_minus_one:
		pass
		
	
	while stage_2_apple_collect() and get_pos_x() > 0:
		pass
	
	if squares_occupied > (world_size_minus_one) * 4 - 4:
		break

transition_to_route()

while True:
	for i in range(world_size / 2):
		game_complete = not move_to_row(world_size_minus_one, False)
		game_complete = game_complete or not move(East)
		game_complete = game_complete or not move_to_row(1, False)
		if i != world_size / 2 - 1:
			game_complete = game_complete or not move(East)
		
		if game_complete:
			break

	game_complete = game_complete or not move_to_row(0, False)
	game_complete = game_complete or not move_to_col(0,)
	
	if game_complete:
		break
		
change_hat(Hats.Straw_Hat)

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

def explore_option_iterative(start_direction):
	global ALL_DIRECTIONS
	if not move(start_direction):
		return False
	
	path_stack = [(start_direction, 0)]
	
	while path_stack and num_items(Items.Gold) < 9863168000000:
		if get_entity_type() == Entities.Treasure:
			harvest()
			start_maze()
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

def start_maze():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def search():
	global drone_id
	global ALL_DIRECTIONS

	for _ in range(drone_id):
		do_a_flip()
		
	if drone_id % 2:
		ALL_DIRECTIONS = ALL_DIRECTIONS[::-1]
	if drone_id % 3:
		ALL_DIRECTIONS[0], ALL_DIRECTIONS[1] = (ALL_DIRECTIONS[1], ALL_DIRECTIONS[0])
	if drone_id % 5:
		ALL_DIRECTIONS[1], ALL_DIRECTIONS[3] = (ALL_DIRECTIONS[3], ALL_DIRECTIONS[1])
	
	while True:
		for direction in ALL_DIRECTIONS:
			if explore_option_iterative(direction):
				break
drone_id = 0
start_maze()
for i in range(max_drones()):
	drone_id = i
	spawn_drone(search)

drone_id = 0

search()