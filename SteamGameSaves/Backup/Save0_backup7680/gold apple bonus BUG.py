from lib import *

def setup_cactus_for_dino():
	change_hat(Hats.Traffic_Cone)

	world_size = get_world_size()
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			plant(Entities.Cactus)
			water_and_fertilize()
	
	return_to_spawn()
	
	while True:
		all_ready = True
		for x in range(world_size):
			for y in range(world_size):
				goto_pos(x, y)
				if not can_harvest():
					all_ready = False
		
		if all_ready:
			for x in range(world_size):
				for y in range(world_size):
					goto_pos(x, y)
					harvest()
			return_to_spawn()
			return

def snake_path():
	world_size = get_world_size()
	
	for col in range(world_size):
		if col % 2 == 0:
			for row in range(world_size):
				if row < world_size - 1:
					move(North)
		else:
			for row in range(world_size):
				if row < world_size - 1:
					move(South)
		
		if col < world_size - 1:
			move(East)

def farm_bones(target_length):
	setup_cactus_for_dino()
	
	change_hat(Hats.Dinosaur_Hat)
	
	length = 0
	
	while length < target_length:
		next_pos = measure()
		next_x = next_pos[0]
		next_y = next_pos[1]
		goto_pos(next_x, next_y)
		length += 1
	
	change_hat(Hats.Traffic_Cone)
	return_to_spawn()

farm_bones(100)