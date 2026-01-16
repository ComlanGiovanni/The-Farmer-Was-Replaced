from movement import *
from navigation import *
from farming import *
from sunflower import *






def plant_pump(entity):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			fast_harvest()
			if get_entity_type() != entity:
				plant(entity)
			use_water_and_fertilizer()
			move(North)
		move(East)

def check_dead():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if not harvest():
				plant(Entities.Pumpkin)
			use_water_and_fertilizer()
			move(North)
		move(East)

def pump():
		till_map()
		plant_pump(Entities.Pumpkin)

def move_direction(d, steps, flip=False):
	for i in range(steps):
		if not can_move(d):
			return
		till()
		plant(Entities.Sunflower)
		move(d)
		if flip:
			do_a_flip()

def spirale():
	size = get_world_size()
	steps = size - 1

	while steps > 0:
		move_direction(North, steps, False)
		move_direction(East, steps)

		steps -= 1

		move_direction(South, steps)
		move_direction(West, steps)

		steps -= 1

def work_and_move(direction):
	till()
	plant(Entities.Sunflower)
	move(direction)


def spirale_couverture():
	size = get_world_size()

	top = size - 1
	bottom = 0
	left = 0
	right = size - 1

	while left <= right and bottom <= top:

		# Nord
		while get_pos_y() < top:
			work_and_move(North)
		left += 1

		# Est
		while get_pos_x() < right:
			work_and_move(East)
		top -= 1

		# Sud
		while get_pos_y() > bottom:
			work_and_move(South)
		right -= 1

		# Ouest
		while get_pos_x() > left:
			work_and_move(West)
		bottom += 1

	