from navigation import goto_pos
from sorting import quicksort_tuples
from farming import *

def print_sorted_sunflowers(sunflowers):
	for petals, x, y in sunflowers:
		quick_print("petals:", petals, "pos:", x, y)

def harvest_sunflowers_optimally():
	sunflowers = []
	
	# 1. Parcourir toute la carte et mesurer les tournesols
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			goto_pos(x, y)
			petals = measure()
			
			# Si c'est un tournesol (pétales > 0)
			if petals > 0:
				sunflowers.append((petals, x, y))
	
	# 2. Trier par nombre de pétales (décroissant)
	sunflowers = quicksort_tuples(sunflowers)
	print_sorted_sunflowers(sunflowers)
	# 3. Récolter dans l'ordre optimal
	for item in sunflowers:
		petals = item[0]
		x = item[1]
		y = item[2]
		
		goto_pos(x, y)
		harvest()


def plant_sunflowers_map():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			fast_harvest()
			if get_entity_type() != Entities.Sunflower:
				till()
				plant(Entities.Sunflower)

			if num_items(Items.Water) > 1 and get_water() < 0.75:
				while get_water() < 0.75:
					use_item(Items.Water)
			
			if num_items(Items.Fertilizer) > 1:
				use_item(Items.Fertilizer)
			
			move(North)
		move(East)