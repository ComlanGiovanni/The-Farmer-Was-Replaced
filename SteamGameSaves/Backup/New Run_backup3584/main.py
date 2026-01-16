from movement import *
from navigation import *
from farming import *
from sunflower import *

def demo_basic_movements():
	zig_zag_origin()
	display_drone_position()
	
	move_up()
	display_drone_position()
	
	move_right()
	display_drone_position()
	
	move_diagonal_down_left()
	display_drone_position()


def demo_navigation():
	zig_zag_origin()
	display_drone_position()
	
	goto_pos(4, 4)
	display_drone_position()
	
	goto_pos(7, 2)
	display_drone_position()
	
	goto_pos(100, 100)
	
	zig_zag_origin()
	display_drone_position()


def demo_edges():
	zig_zag_origin()
	
	move_to_edge_vertical("up")
	display_drone_position()
	
	move_to_edge_horizontal("right")
	display_drone_position()
	
	move_to_edge_vertical("down")
	display_drone_position()

	origin()
	display_drone_position()


def demo_grid_pattern():
	zig_zag_origin()
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if is_even(get_pos_x() + get_pos_y()):
				do_a_flip()
			move(North)
		move(East)
	zig_zag_origin()


def demo_selective_farming():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			x = get_pos_x()
			
			# Zone 1: Buissons
			if x == 0 or x == 1:
				plant(Entities.Bush)
			
			# Zone 2: Carottes
			elif x == 2 or x == 3:
				till_ground()
				plant(Entities.Carrot)
			
			# Zone 3: Arbres en alternance
			elif x >= 4:
				if is_even(get_pos_y()):
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
			
			move(North)
		move(East)

def demo_all_hats():
	hats = [
		Hats.Brown_Hat,
		Hats.Golden_Cactus_Hat,
		Hats.Golden_Carrot_Hat,
		Hats.Golden_Gold_Hat,
		Hats.Golden_Pumpkin_Hat,
		Hats.Golden_Sunflower_Hat,
		Hats.Golden_Tree_Hat,
		Hats.Gray_Hat,
		Hats.Green_Hat,
		Hats.Purple_Hat,
		Hats.Straw_Hat,
		Hats.Traffic_Cone
	]
	
	for hat in hats:
		change_hat(hat)
		do_a_flip()

def run_all_demos():
	demo_basic_movements()
	demo_navigation()
	demo_edges()
	demo_grid_pattern()
	demo_selective_farming()
	demo_all_hats()
	

def main_farming_loop():
	while True:
		clear()
		change_hat(Hats.Golden_Gold_Hat)
		do_a_flip()
		harvest_map()
		till_map()
		plant_entity_map(Entities.Pumpkin)
		harvest_map()
		plant_trees_alternating()
		harvest_map()
		plant_entity_map(Entities.Carrot)
		apply_water_and_fertilizer_map()
		harvest_map()
		plant_sunflowers_map()
		harvest_sunflowers_optimally()


def plant_trees_alternating():
	number_of_tile = get_world_size() * get_world_size()
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if is_even(number_of_tile):
				plant_tree()
			number_of_tile -= 1
			move(North)
		number_of_tile += 1
		move(East)

def quick_farm_carrots():
	while True:
		clear()
		till_map()
		plant_entity_map(Entities.Carrot)
		apply_water_and_fertilizer_map()
		harvest_map()


def quick_farm_sunflowers():
	while True:
		clear()
		till_map()
		plant_sunflowers_map()
		harvest_sunflowers_optimally()


def quick_farm_wood():
	while True:
		harvest_map()
		plant_entity_map(Entities.Tree)
		apply_water_and_fertilizer_map()


#--------------------------------------------------


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



#clear()
#spirale_couverture()
#clear()
#spirale()
#origin()

#pump()
#check_dead()



#--------------------------------------------------

main_farming_loop()

# run_all_demos()
# quick_farm_carrots()
# quick_farm_sunflowers()
# quick_farm_wood()