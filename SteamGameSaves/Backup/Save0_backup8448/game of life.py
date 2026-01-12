from lib import *

def count_neighbors(x, y, state):
	count = 0
	world_size = get_world_size()
	
	for dx in [-1, 0, 1]:
		for dy in [-1, 0, 1]:
			if dx == 0 and dy == 0:
				continue
			nx = (x + dx) % world_size
			ny = (y + dy) % world_size
			if (nx, ny) in state:
				count += 1
	return count

def read_state():
	world_size = get_world_size()
	state = set()
	
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			if get_entity_type() == Entities.Bush:
				state.add((x, y))
	
	return_to_spawn()
	return state

def apply_state(state):
	world_size = get_world_size()
	
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			should_be_alive = (x, y) in state
			is_alive = get_entity_type() == Entities.Bush
			
			if should_be_alive and not is_alive:
				plant(Entities.Bush)
			elif not should_be_alive and is_alive:
				harvest()
	
	return_to_spawn()

def game_of_life_step():
	world_size = get_world_size()
	current_state = read_state()
	next_state = set()
	
	for x in range(world_size):
		for y in range(world_size):
			neighbors = count_neighbors(x, y, current_state)
			alive = (x, y) in current_state
			
			if alive and (neighbors == 2 or neighbors == 3):
				next_state.add((x, y))
			elif not alive and neighbors == 3:
				next_state.add((x, y))
	
	apply_state(next_state)

def init_random(density):
	clear_map()
	world_size = get_world_size()
	
	for x in range(world_size):
		for y in range(world_size):
			if random() < density:
				goto_pos(x, y)
				plant(Entities.Bush)
	
	return_to_spawn()

def init_glider():
	clear_map()
	pattern = [
		(1, 0),
		(2, 1),
		(0, 2),
		(1, 2),
		(2, 2)
	]
	
	for pos in pattern:
		x = pos[0]
		y = pos[1]
		goto_pos(x, y)
		plant(Entities.Bush)
	
	return_to_spawn()

def init_blinker():
	clear_map()
	world_size = get_world_size()
	center = world_size // 2
	
	pattern = [
		(center - 1, center),
		(center, center),
		(center + 1, center)
	]
	
	for pos in pattern:
		x = pos[0]
		y = pos[1]
		goto_pos(x, y)
		plant(Entities.Bush)
	
	return_to_spawn()

def init_toad():
	world_size = get_world_size()
	center = world_size // 2
	
	pattern = [
		(center, center),
		(center + 1, center),
		(center + 2, center),
		(center - 1, center + 1),
		(center, center + 1),
		(center + 1, center + 1)
	]
	
	for pos in pattern:
		x = pos[0]
		y = pos[1]
		goto_pos(x, y)
		plant(Entities.Bush)
	
	return_to_spawn()

def init_beacon():
	clear_map()
	world_size = get_world_size()
	center = world_size // 2
	
	pattern = [
		(center, center),
		(center + 1, center),
		(center, center + 1),
		(center + 3, center + 2),
		(center + 2, center + 3),
		(center + 3, center + 3)
	]
	
	for pos in pattern:
		x = pos[0]
		y = pos[1]
		goto_pos(x, y)
		plant(Entities.Bush)
	
	return_to_spawn()

def init_pulsar():
	clear_map()
	world_size = get_world_size()
	center = world_size // 2
	
	pattern = [
		(center - 6, center - 4), (center - 6, center - 3), (center - 6, center - 2),
		(center - 6, center + 2), (center - 6, center + 3), (center - 6, center + 4),
		(center - 1, center - 4), (center - 1, center - 3), (center - 1, center - 2),
		(center - 1, center + 2), (center - 1, center + 3), (center - 1, center + 4),
		(center + 1, center - 4), (center + 1, center - 3), (center + 1, center - 2),
		(center + 1, center + 2), (center + 1, center + 3), (center + 1, center + 4),
		(center + 6, center - 4), (center + 6, center - 3), (center + 6, center - 2),
		(center + 6, center + 2), (center + 6, center + 3), (center + 6, center + 4),
		(center - 4, center - 6), (center - 3, center - 6), (center - 2, center - 6),
		(center + 2, center - 6), (center + 3, center - 6), (center + 4, center - 6),
		(center - 4, center - 1), (center - 3, center - 1), (center - 2, center - 1),
		(center + 2, center - 1), (center + 3, center - 1), (center + 4, center - 1),
		(center - 4, center + 1), (center - 3, center + 1), (center - 2, center + 1),
		(center + 2, center + 1), (center + 3, center + 1), (center + 4, center + 1),
		(center - 4, center + 6), (center - 3, center + 6), (center - 2, center + 6),
		(center + 2, center + 6), (center + 3, center + 6), (center + 4, center + 6)
	]
	
	for pos in pattern:
		x = pos[0]
		y = pos[1]
		goto_pos(x, y)
		plant(Entities.Bush)
	
	return_to_spawn()

till_entire_map()
init_glider()

for i in range(100):
	game_of_life_step()