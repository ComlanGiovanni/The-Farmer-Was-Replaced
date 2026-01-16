from navigation import goto_pos
from navigation import move_to_origin # can be on one line ?
from sorting import quicksort_tuples
from farming import *

def sort_row(size):
	for _ in range(size):
		for _ in range(size - 1):
			if measure(East) < measure():
				swap(East)
			move(East)

def sort_column(size):
	for _ in range(size):
		for _ in range(size - 1):
			if measure(North) < measure():
				swap(North)
			move(North)

def sort_cactus_field():
	size = get_world_size()

	# 1. Trier toutes les lignes
	move_to_origin()
	for _ in range(size):
		sort_row(size)
		if can_move(North):
			move(North)

	# 2. Trier toutes les colonnes
	move_to_origin()
	for _ in range(size):
		sort_column(size)
		if can_move(East):
			move(East)

	# 3. Récolte globale (1 seul appel)
	move_to_origin()
	harvest()

def plant_cactus_map():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			fast_harvest()
			if get_entity_type() != Entities.Cactus:
				till()
				plant(Entities.Cactus)

			if num_items(Items.Water) > 1 and get_water() < 0.75:
				while get_water() < 0.75:
					use_item(Items.Water)
			
			if num_items(Items.Fertilizer) > 1:
				use_item(Items.Fertilizer)
			
			move(North)
		move(East)	
		