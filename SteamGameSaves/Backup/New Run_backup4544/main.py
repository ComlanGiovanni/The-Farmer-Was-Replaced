from movement import *
from navigation import *
from farming import *
from sunflower import *
from cactus import *
from pumpkin import *

from testing import *

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
	
#aller voir les fonction de plant et pouvoir planter
#meme si on a deja un block till
def main_farming_loop():
	while True:
		clear()
		change_hat(Hats.Golden_Gold_Hat)
		do_a_flip()
		harvest_map()
		till_map()
		plant_trees_alternating()
		harvest_map()
		plant_entity_map(Entities.Carrot)
		harvest_map()
		plant_sunflowers_map()
		harvest_sunflowers_optimally()
		plant_cactus_map()
		clear()
		sort_cactus_field()



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


def cover_map_boustrophedon(start_axis="horizontal"):
	size = get_world_size()

	# On part de (0,0)
	till()

	if start_axis == "horizontal":
		go_positive = True  # Est puis Ouest

		for y in range(size):
			# Parcours horizontal
			for _ in range(size - 1):
				if go_positive:
					move(East)
				else:
					move(West)
				till()

			# Changement de ligne
			if y < size - 1:
				move(North)
				till()
				go_positive = not go_positive

	elif start_axis == "vertical":
		go_positive = True  # Nord puis Sud

		for x in range(size):
			# Parcours vertical
			for _ in range(size - 1):
				if go_positive:
					move(North)
				else:
					move(South)
				till()

			# Changement de colonne
			if x < size - 1:
				move(East)
				till()
				go_positive = not go_positive

main_farming_loop()





clear()
plant_cactus_map()
sort_cactus_field()



clear()

plant_sunflowers_map()
harvest_sunflowers_optimally()
		
cover_map_boustrophedon("horizontal")
cover_map_boustrophedon("vertical")
quick_print("tick -> ",get_tick_count())
quick_print("time -> ", get_time())

while True:
	do_a_flip()

for y in range(get_world_size()):
		for x in range(get_world_size()):
			goto_pos(x, y)
			till()

clear()

spirale_couverture()

clear()

for y in range(get_world_size()):
		for x in range(get_world_size()):
			goto_pos(y, x)
			till()


do_a_flip()

print("{{{{{", do_a_flip(), "}}}}}")
print("###", origin(), "###")
print(get_time())

goto_pos(13, 10)

print(get_cost(Unlocks.Megafarm))
move_up()
print(unlock(Unlocks.Megafarm))
for i in range(2):
	move_up()
print(get_cost(Entities.Pumpkin))
for i in range(3):
	move_up()
	move_right()
print(get_cost(Entities.Bush))
for i in range(4):
	move_up()
cost = get_cost(Entities.Carrot)
move_left()
move_down()

get_cost(Unlocks.Loops, 0)
get_cost(Unlocks.Leaderboard, 0)

for item in cost:
	quantite_de_cet_objet_necessaire = cost[item]
	
	print(quantite_de_cet_objet_necessaire)

clear()

#spirale_couverture()
#clear()
#spirale()
#origin()

#pump()
#check_dead()


#--------------------------------------------------

# run_all_demos()
# quick_farm_carrots()
# quick_farm_sunflowers()
# quick_farm_wood()