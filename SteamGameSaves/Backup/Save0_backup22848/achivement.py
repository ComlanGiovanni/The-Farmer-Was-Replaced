from core import *
from advanced import *

def sort_cactus_wrong_order():
	world_size = get_world_size()
	
	# Planter et faire pousser des cactus partout
	for x in range(world_size):
		for y in range(world_size):
			goto_pos(x, y)
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Cactus:
				plant(Entities.Cactus)
	
	# Attendre que tous soient adultes
	max_wait = 100
	for _ in range(max_wait):
		all_adult = True
		for x in range(world_size):
			for y in range(world_size):
				goto_pos(x, y)
				if get_entity_type() == Entities.Cactus and not can_harvest():
					all_adult = False
					break
			if not all_adult:
				break
		if all_adult:
			break
	
	# Trier dans le MAUVAIS ordre avec bubble sort
	changed = True
	iterations = 0
	while changed and iterations < 1000:
		changed = False
		iterations += 1
		
		for x in range(world_size):
			for y in range(world_size):
				goto_pos(x, y)
				current_size = measure()
				
				# North doit être <= (mauvais ordre)
				if y < world_size - 1:
					goto_pos(x, y + 1)
					north_size = measure()
					if north_size != None and current_size > north_size:
						goto_pos(x, y)
						swap(North)
						changed = True
						continue
				
				# East doit être <= (mauvais ordre)
				if x < world_size - 1:
					goto_pos(x, y)
					current_size = measure()
					goto_pos(x + 1, y)
					east_size = measure()
					if east_size != None and current_size > east_size:
						goto_pos(x, y)
						swap(East)
						changed = True
						continue
				
				# South doit être >= (mauvais ordre)
				if y > 0:
					goto_pos(x, y)
					current_size = measure()
					goto_pos(x, y - 1)
					south_size = measure()
					if south_size != None and current_size < south_size:
						goto_pos(x, y)
						swap(South)
						changed = True
						continue
				
				# West doit être >= (mauvais ordre)
				if x > 0:
					goto_pos(x, y)
					current_size = measure()
					goto_pos(x - 1, y)
					west_size = measure()
					if west_size != None and current_size < west_size:
						goto_pos(x, y)
						swap(West)
						changed = True


#def stack_overflow():
	#stack_overflow()

def recycle_maze_achievement_small():
	set_world_size(3)
	create_maze()
	
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	needed_substance = substance * 300
	
	quick_print("Substance nécessaire:", needed_substance)
	quick_print("Substance disponible:", num_items(Items.Weird_Substance))
	
	if num_items(Items.Weird_Substance) < needed_substance:
		quick_print("Pas assez de Weird_Substance !")
		return

	return_to_spawn()
	directions = [North, East, South, West]
	direction_index = 0
	
	while get_entity_type() != Entities.Treasure:
		right_index = (direction_index + 1) % 4
		if can_move(directions[right_index]):
			direction_index = right_index
			move(directions[direction_index])
		elif can_move(directions[direction_index]):
			move(directions[direction_index])
		else:
			direction_index = (direction_index - 1) % 4
	
	quick_print("Trésor initial trouvé à:", get_pos_x(), get_pos_y())
	
	for i in range(300):
		if get_entity_type() != Entities.Treasure:
			quick_print("Erreur itération", i, ": pas sur trésor, type:", get_entity_type())
			treasure_pos = measure()
			if treasure_pos != None:
				treasure_x, treasure_y = treasure_pos
				goto_pos(treasure_x, treasure_y)
			else:
				quick_print("measure() retourne None")
				return
		
		if not use_item(Items.Weird_Substance, substance):
			quick_print("Erreur: échec use_item à l'itération", i)
			return

		treasure_pos = measure()
		if treasure_pos == None:
			quick_print("Erreur: trésor introuvable après itération", i)
			return
		
		treasure_x, treasure_y = treasure_pos
		goto_pos(treasure_x, treasure_y)
		
		if (i + 1) % 50 == 0:
			quick_print("Progrès:", i + 1, "/ 300")
	
	quick_print("Achèvement 'Recyclage' débloqué !")

HATS = [
	Hats.Brown_Hat,
	Hats.Cactus_Hat,
	Hats.Carrot_Hat,
	Hats.Dinosaur_Hat,
	Hats.Gold_Hat
]

def fashion_show_achievement():
	x = 0

	for hat in HATS:
		def task(h=hat, tx=x):
			goto_pos(tx, 0)
			change_hat(h)
			while True:
				pass

		spawn_drone(task)
		x += 1

#def fashion_show_achievement():
	#for i in range(5):
		#def task(index=i):
			#goto_pos(index, 0)
			#change_hat(HATS[index])
			#while True:
				#pass

		#if not spawn_drone(task):
			#task()
			