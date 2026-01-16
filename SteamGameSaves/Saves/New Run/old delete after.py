def fast_harvest():
	if can_harvest():
		harvest()
		
def is_even(n):
	return n % 2 == 0

def is_not_even(n):
	return not is_even(n)

def till_ground():
	if get_ground_type() != Grounds.Soil:
		till()

def watering_ground(threshold=1):
	if num_items(Items.Water) > 1 and get_water() < 1:
		while get_water() < threshold:
			use_item(Items.Water)

#maybe measure if infected ? or fertilized juste work one ?
def fertilize_ground():
	if num_items(Items.Fertilizer) > 1:
		use_item(Items.Fertilizer)

def use_water_and_fertilizer():
	watering_ground(0.75)
	fertilize_ground()

def plant_carrot():
	fast_harvest()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	use_water_and_fertilizer()

def plant_grass():
	fast_harvest()
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	use_water_and_fertilizer()

def plant_sunflower():
	fast_harvest()
	if get_entity_type() != Entities.Sunflower:
		plant(Entities.Sunflower)
	use_water_and_fertilizer()

def plant_cactus():
	fast_harvest()
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)
	use_water_and_fertilizer()
	
	
	
	directions = [North, East, South, West]

def is_origin():
	return (get_pos_x() == 0 and get_pos_y() == 0)

def origin():
	if (get_pos_x() == 0 and get_pos_y() == 0):
		return
	while (get_pos_x() > 0):
		move(West)
	while (get_pos_y() > 0):
		move(South)

def zig_zig_origin():
	if is_origin():
		return
	while not is_origin():
		if (get_pos_x() > 0):
			move(West)
		if (get_pos_y() > 0):
			move(South)

def display_drone_position():
	print(get_pos_x())
	print(get_pos_y())

def is_valid_position(x, y):
	world_size = get_world_size()
	return 0 <= x < world_size and 0 <= y < world_size

def move_up():
	if get_pos_y() < get_world_size() - 1:
		move(North)

def move_down():
	if get_pos_y() > 0:
		move(South)

def move_right():
	if get_pos_x() < get_world_size() - 1:
		move(East)

def move_left():
	if get_pos_x() > 0:
		move(West)

def move_diagonal_up_right():
	move_up()
	move_right()

def move_diagonal_up_left():
	move_up()
	move_left()

def move_diagonal_down_right():
	move_down()
	move_right()

def move_diagonal_down_left():
	move_down()
	move_left()
		
def move_to_edge_horizontal(direction):
	world_size = get_world_size()
	
	if direction == "right":
		while get_pos_x() < world_size - 1:
			move(East)
	elif direction == "left":
		while get_pos_x() > 0:
			move(West)

def move_to_edge_vertical(direction):
	world_size = get_world_size()
	
	if direction == "up":
		while get_pos_y() < world_size - 1:
			move(North)
	elif direction == "down":
		while get_pos_y() > 0:
			move(South)

def move_n_times(direction_index, n):
	for i in range(n):
		move(directions[direction_index])

#no need abs() but i think we unlock it at a moment
def goto_pos(target_x, target_y):
	if not is_valid_position(target_x, target_y):
		print("out of map")
		return
	dx = target_x - get_pos_x()
	dy = target_y - get_pos_y()
	
	if dx > 0:
		move_n_times(1, dx)
	if dx < 0:
		move_n_times(3, -dx)
	if dy > 0:
		move_n_times(0, dy)
	if dy < 0:
		move_n_times(2, -dy)
	
	
#it's would be great if i can choose the direction
#def spiral_from_spawn():
	#zig_zig_origin()
	#distance = get_world_size()
	#while distance > 1:
		
	
from minilib import *

def plant_only(seed):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if seed == Entities.Carrot:
				till()
				if num_items(Items.Hay) > 1 and num_items(Items.Wood) > 1:
					plant(seed)
			plant(seed)
			move(North)
		move(East)

def collect():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() == Entities.Carrot:
				fast_harvest()
				plant(Entities.Carrot)
			if get_entity_type() == Entities.Tree:
				fast_harvest()
				plant(Entities.Tree)
			if get_entity_type() == Entities.Grass:
				fast_harvest()
				plant(Entities.Grass)
			move(North)
		move(East)

def simple_collect():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			fast_harvest()
			move(North)
		move(East)

def plant_tree():
	number_of_tile = get_world_size() * get_world_size()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if is_even(number_of_tile):
				plant(Entities.Tree)
			number_of_tile -= 1
			move(North)
		number_of_tile += 1
		move(East)
	
import clean
from minilib import *
from movement import *

def till_map():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till_ground()
			move(North)
		move(East)
		

def plant_sunflower_on_map():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant_sunflower()
			move(North)
		move(East)

def harvers_map():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			fast_harvest()
			move(North)
		move(East)

def quicksort_sunflowers(sunflowers):
	if len(sunflowers) <= 1:
		return sunflowers
	
	pivot = sunflowers[len(sunflowers) // 2][0]
	left = []
	middle = []
	right = []
	
	for item in sunflowers:
		petals = item[0]
		if petals > pivot:
			left.append(item)
		elif petals == pivot:
			middle.append(item)
		else:
			right.append(item)
	
	return quicksort_sunflowers(left) + middle + quicksort_sunflowers(right)

def harvest_sunflowers_optimally():
	sunflowers = []
	
	# 1. Mesurer tous les tournesols
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			goto_pos(x, y)
			petals = measure()
			if petals > 0:
				sunflowers.append((petals, x, y))
	
	# 2. Trier (du plus grand au plus petit)
	sunflowers = quicksort_sunflowers(sunflowers)
	
	# 3. Récolter dans l'ordre
	for item in sunflowers:
		goto_pos(item[1], item[2])
		harvest()

#clear()
#till_map()
#plant_sunflower_on_map()
#harvest_sunflowers_optimally()
#till_map()
#plant_sunflower_on_map()
#harvest_sunflowers_optimally()
#plant_sunflower_on_map()
#harvers_map()

#clear()
#zig_zig_origin()
move_to_edge_vertical("up") 
move_left()
move_left()
goto_pos(4,4)
goto_pos(2,2)

zig_zig_origin()

def full_engrais():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			use_water_and_fertilizer()
			move(North)
		move(East)

while True:
	clear()
	change_hat(Hats.Golden_Gold_Hat)
	do_a_flip()
	clean.simple_collect()
	clean.plant_tree()
	full_engrais()
	clean.collect()
	clean.plant_only(Entities.Carrot)
	full_engrais()
	clean.simple_collect()
	clear()
	till_map()
	plant_sunflower_on_map()
	harvest_sunflowers_optimally()


empty_list = []

hats_name = [Hats.Brown_Hat,
			Hats.Golden_Cactus_Hat,
			Hats.Golden_Carrot_Hat,
			Hats.Golden_Gold_Hat,
			Hats.Golden_Pumpkin_Hat,
			Hats.Golden_Sunflower_Hat,
			Hats.Golden_Tree_Hat,
			Hats.Golden_Tree_Hat,
			Hats.Gray_Hat,
			Hats.Green_Hat,
			Hats.Purple_Hat,
			Hats.Straw_Hat,
			Hats.Traffic_Cone]

x = 0
while x < len(hats_name) - 1:
	print(hats_name[x])
	pet_the_piggy()
	change_hat(hats_name[x])

def water():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_water() < 1 and num_items(Items.Water) > 1:
				use_item(Items.Water)
			move(North)
		move(East)

def check_item(item):
	if num_items(item) > 1:
		return 

for i in range(get_world_size()):
	for j in range(get_world_size()):
		if get_pos_x() == 1:
			plant(Entities.Bush)
		if get_pos_x() == 2:
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
		if get_pos_x() == 3:
			if is_even(get_pos_y()): 
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		elif get_pos_x() == 4:
			if not is_even(get_pos_y()): 
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		move(North)
	move(East)

#num_unlocked(Unlocks.Carrots)
#num_unlocked(Unlocks.Senses)

for i in range(2):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() == Entities.Bush:
				if can_harvest():
					harvest()
				plant(Entities.Bush)
			elif get_ground_type() == Grounds.Soil:
				if can_harvest():
					harvest()
				if num_items(Items.Hay) > 1 and num_items(Items.Wood) > 1:
					plant(Entities.Carrot)
			else:
				if get_pos_x() == 3:
					if can_harvest():
						harvest()
					if is_even(get_pos_y()):
						plant(Entities.Tree)
					else:
						plant(Entities.Bush)
				if can_harvest():
					harvest()
			move(North)
		move(East)

clear()


while True:
	for i in range(get_world_size()):
		harvest()
		move(North)
	move(East)
	for i in range(get_world_size()):
		plant(Entities.Bush)
		move(North)
	move(East)
	if can_harvest():
		harvest()
#ceci est un commentaire

harvest()
do_a_flip()
harvest()

change_hat(Hats.Brown_Hat)
##Hat after finishing the game
change_hat(Hats.Golden_Cactus_Hat)
change_hat(Hats.Golden_Carrot_Hat)
change_hat(Hats.Golden_Gold_Hat)
change_hat(Hats.Golden_Pumpkin_Hat)
change_hat(Hats.Golden_Sunflower_Hat)
change_hat(Hats.Golden_Tree_Hat)
change_hat(Hats.Golden_Tree_Hat)
##Hat after finishing the game
change_hat(Hats.Gray_Hat)
change_hat(Hats.Green_Hat)
change_hat(Hats.Purple_Hat)
change_hat(Hats.Straw_Hat)
change_hat(Hats.Traffic_Cone)