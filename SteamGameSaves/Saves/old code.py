while True:
	till()
	plant(Entities.Carrot)
	plant(Entities.Bush)
	move(North)
	if can_harvest():
		harvest()
	move(North)
	if can_harvest():
		harvest()
	move(South)
	if can_harvest():
		harvest()
	move(South)
	if can_harvest():
		harvest()
		
		print("Hello World")
print(0.24)
quick_print("output.txt")
print("this is a line")
#Every ouput get printed in the output.txt file
pet_the_piggy()
do_a_flip()
clear()

while True:
	till()
	plant(Entities.Carrot)
	move(North)
	plant(Entities.Bush)
	move(North)
	harvest()
	
	

	
	
	
while True:
	if can_harvest():
		harvest()
	move(North)
	if can_harvest():
		harvest()
	plant(Entities.Carrot)
	move(North)
	if can_harvest():
		harvest()
	plant(Entities.Bush)
	do_a_flip()	
	
	
	
	
while True:
	do_a_flip()
	do_a_flip()
	do_a_flip()
	if can_harvest():
		harvest()
	move(North)
	if can_harvest():
		harvest()
	plant(Entities.Carrot)
	move(North)
	if can_harvest():
		harvest()
	plant(Entities.Bush)
	do_a_flip()
	do_a_flip()
	do_a_flip()
	move(South)
	move(South)
	
	
	
	while True:
		move(North)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(North)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(East)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(South)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(South)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(East)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(North)
	if can_harvest():
		harvest()
	move(North)
	move(West)
	move(West)
	move(West)
	
	
if can_harvest():
	harvest()
plant(Entities.Tree)

while True:
	for i in range(6):
		if can_harvest():
			harvest()
		plant(Entities.Carrot)
		move(North)
	move(East)
	
	while True:
		move(North)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(North)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(East)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(South)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(South)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(East)
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	move(North)
	if can_harvest():
		harvest()
	move(North)
	move(West)
	move(West)
	move(West)
	world_x, world_y = get_world_size(), get_world_size()


def return_to_spawn():
	player_x, player_y = get_pos_x(), get_pos_y()
#verifier si on eset deja a 00 et sortie de la fonction
	while player_x > 0:
		move(West)
		player_x = get_pos_x()
	while player_y > 0:
		move(South)
		player_y = get_pos_y()

def print_position():
	player_x, player_y = get_pos_x(), get_pos_y()
	print(player_x)
	print(player_y)
	
	
	
	
def visite_all_tile():
	return_to_spawn()
	world_x, world_y = get_world_size(), get_world_size()
	number_of_tile = world_x * world_y
	tile_visited = 1
	for i in range(3):
		for i in range(world_x - 1):
			move(North)
			tile_visited += 1
		move(East)
		tile_visited += 1
		for i in range(world_x - 1):
			move(South)
			tile_visited += 1
		move(East)
		
#reset player position
return_to_spawn()

#Setting Variable for looping
world_x, world_y = get_world_size(), get_world_size()
number_of_tile = world_x * world_y
tile_visited = 1

harvest()
if get_ground_type() != Grounds.Soil:
	till()

for i in range(4):

	for i in range(world_x - 1):
		move(North)
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
	
		tile_visited += 1

	move(East)
	tile_visited += 1
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()


	for i in range(world_x - 1):
		move(South)
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		tile_visited += 1

	move(East)
	harvest()
	if get_ground_type() != Grounds.Soil:
		till()


		
		
		
		
		
from pos_lib import *

#reset player position
return_to_spawn()

#Setting Variable for looping
world_x, world_y = get_world_size(), get_world_size()
number_of_tile = world_x * world_y
tile_visited = 1


#funtion define
def is_even(n):
	return n % 2 == 0

def watering_grounds():
	water_value = get_water()
	while water_value < 1:
		use_item(Items.Water)
		water_value = get_water()
		if water_value > 1:
			pass

while True:
	if not is_even(tile_visited):
		if get_entity_type() == Entities.Tree:
			if can_harvest():
				harvest()
				plant(Entities.Tree)
				watering_grounds()
				use_item(Items.Fertilizer)
	for i in range(3):
	
		for i in range(world_x - 1):
			move(North)
			tile_visited += 1
			if not is_even(tile_visited):
				if get_entity_type() == Entities.Tree:
					if can_harvest():
						harvest()
						plant(Entities.Tree)
						watering_grounds()
						use_item(Items.Fertilizer)
			player_x = get_pos_x() #no need to get everytime i guess
			if player_x == 0 :
				if is_even(tile_visited):
					plant(Entities.Grass)
					watering_grounds()
					use_item(Items.Fertilizer)
			player_x = get_pos_x()
			if player_x == 2 :
				if is_even(tile_visited):
					plant(Entities.Grass)
					watering_grounds()
					use_item(Items.Fertilizer)
			if player_x == 4 :
				if is_even(tile_visited):
					plant(Entities.Grass)
					watering_grounds()
					use_item(Items.Fertilizer)
	
		move(East)
		tile_visited += 1
		if not is_even(tile_visited):
			if get_entity_type() == Entities.Tree:
				if can_harvest():
					harvest()
					plant(Entities.Tree)
					watering_grounds()
					use_item(Items.Fertilizer)
			player_x = get_pos_x()
		for i in range(world_x - 1):
			move(South)
			tile_visited += 1
			if not is_even(tile_visited):
				if get_entity_type() == Entities.Tree:
					if can_harvest():
						harvest()
						plant(Entities.Tree)
						watering_grounds()
						use_item(Items.Fertilizer)
			if player_x == 1:
				if is_even(tile_visited):
					plant(Entities.Carrot)
					watering_grounds()
					use_item(Items.Fertilizer)
			if player_x == 3:
				if is_even(tile_visited):
					plant(Entities.Carrot)
					watering_grounds()
					use_item(Items.Fertilizer)
			if player_x == 5:
				if is_even(tile_visited):
					plant(Entities.Carrot)
					watering_grounds()
					use_item(Items.Fertilizer)
		move(East)
		tile_visited += 1
		if not is_even(tile_visited):
			if get_entity_type() == Entities.Tree:
				if can_harvest():
					harvest()
					plant(Entities.Tree)
					watering_grounds()
					use_item(Items.Fertilizer)

from pos_lib import *

#reset player position
return_to_spawn()

#Setting Variable for looping
world_x, world_y = get_world_size(), get_world_size()
number_of_tile = world_x * world_y
tile_visited = 1

plant(Entities.Pumpkin)

while True:
	for i in range(6):
		for i in range(3):
		
			for i in range(world_x - 1):
				move(North)
				if get_entity_type() == Entities.Dead_Pumpkin :
					plant(Entities.Pumpkin)
				plant(Entities.Pumpkin)
				tile_visited += 1
		
			move(East)
			tile_visited += 1
			plant(Entities.Pumpkin)
		
			for i in range(world_x - 1):
				move(South)
				plant(Entities.Pumpkin)
				tile_visited += 1
		
			move(East)
			plant(Entities.Pumpkin)
	harvest()
		
from pos_lib import *
return_to_spawn()

def watering_grounds():
	while get_water() < 1:
		use_item(Items.Water)

def handle_tree():
	if get_entity_type() == Entities.Tree:
		if can_harvest():
			harvest()
			plant(Entities.Tree)
			watering_grounds()
			use_item(Items.Fertilizer)

def handle_even_column():
	x = get_pos_x()
	if x % 2 == 0:  # Colonnes paires (0,2,4,6,8,10)
		plant(Entities.Grass)
		watering_grounds()
		use_item(Items.Fertilizer)

def handle_odd_column():
	x = get_pos_x()
	if x % 2 == 1:  # Colonnes impaires (1,3,5,7,9,11)
		if get_entity_type() == Entities.Carrot:
			if can_harvest():
				harvest()
		plant(Entities.Carrot)
		watering_grounds()
		use_item(Items.Fertilizer)

world_size = get_world_size()

while True:
	# Serpent pattern
	for col in range(world_size):
		# Direction du mouvement
		if col % 2 == 0:
			direction = North
			handler = handle_even_column
		else:
			direction = South
			handler = handle_odd_column
		
		# Traiter la case actuelle
		handle_tree()
		handler()
		
		# Avancer dans la colonne
		for row in range(world_size - 1):
			move(direction)
			handle_tree()
			handler()
		
		# Passer à la colonne suivante (sauf à la fin)
		if col < world_size - 1:
			move(East)
from pos_lib import *
return_to_spawn()

def watering_grounds():
	while get_water() < 1:
		use_item(Items.Water)

def fertilize():
	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)

def handle_crop(crop_type):
	if can_harvest():
		harvest()
	if get_entity_type() != crop_type:
		plant(crop_type)
	#watering_grounds()
	#fertilize()

world_size = get_world_size()

while True:
	for col in range(world_size):
		if col % 2 == 0:
			direction = North
		else:
			direction = South
		
		for row in range(world_size):
			x = get_pos_x()
			y = get_pos_y()
			
			if x < 2:
				handle_crop(Entities.Tree)
			elif x < 4:
				handle_crop(Entities.Pumpkin)
			elif x < 6:
				handle_crop(Entities.Carrot)
			elif x < 8:
				handle_crop(Entities.Sunflower)
			elif x < 10: 
				handle_crop(Entities.Cactus)
			else:
				handle_crop(Entities.Grass)
			
			if row < world_size - 1:
				move(direction)
		
		if col < world_size - 1:
			move(East)
	
	return_to_spawn()


#reset player position
return_to_spawn()

#Setting Variable for looping
world_x, world_y = get_world_size(), get_world_size()
number_of_tile = world_x * world_y

while True:
	if get_ground_type() == Grounds.Soil:
		if can_harvest():
			harvest()
			plant(Entities.Grass)
		else:
			plant(Entities.Grass)
	
	for i in range(3):
	
		for i in range(world_x - 1):
			move(North)
			if get_ground_type() == Grounds.Soil:
					if can_harvest():
						harvest()
						plant(Entities.Grass)
					else:
						plant(Entities.Grass)
	
		move(East)
		if get_ground_type() == Grounds.Soil:
			if can_harvest():
				harvest()
				plant(Entities.Grass)
			else:
				plant(Entities.Grass)
	
	
		for i in range(world_x - 1):
			move(South)
			if get_ground_type() == Grounds.Soil:
				if can_harvest():
					harvest()
					plant(Entities.Grass)
				else:
					plant(Entities.Grass)
	
		move(East)
		if get_ground_type() == Grounds.Soil:
			if can_harvest():
				harvest()
				plant(Entities.Grass)
			else:
				plant(Entities.Grass)
	
from pos_lib import *

#reset player position
return_to_spawn()

#Setting Variable for looping
world_x, world_y = get_world_size(), get_world_size()
number_of_tile = world_x * world_y
tile_visited = 1


#funtion define
def is_even(n):
	return n % 2 == 0


harvest()
print(tile_visited)
if not is_even(tile_visited):
	plant(Entities.Tree)

for i in range(3):

	for i in range(world_x - 1):
		move(North)
		tile_visited += 1
		if not is_even(tile_visited):
			plant(Entities.Tree)

	move(East)
	tile_visited += 1
	if not is_even(tile_visited):
		plant(Entities.Tree)



	for i in range(world_x - 1):
		move(South)
		tile_visited += 1
		if not is_even(tile_visited):
			plant(Entities.Tree)

	move(East)
	tile_visited += 1
	if not is_even(tile_visited):
			plant(Entities.Tree)


		def watering_grounds():
	water_value = get_water()
	while water_value < 0.5:
		use_item(Items.Water)
		water_value = get_water()
		if water_value > 1:
			pass
				