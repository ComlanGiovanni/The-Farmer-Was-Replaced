def fast_harvest():
	if can_harvest():
		harvest()

def is_even(n):
	return n % 2 == 0

def till_ground():
	if get_ground_type() != Grounds.Soil:
		till()

def watering_ground(threshold=1):
	if num_items(Items.Water) > 1 and get_water() < threshold:
		while get_water() < threshold:
			use_item(Items.Water)

def fertilize_ground():
	if num_items(Items.Fertilizer) > 1:
		use_item(Items.Fertilizer)

def use_water_and_fertilizer():
	watering_ground(0.67)
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

def plant_tree():
	fast_harvest()
	if get_entity_type() != Entities.Tree:
		plant(Entities.Tree)
	use_water_and_fertilizer()

def till_map():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till_ground()
			move(North)
		move(East)

def apply_water_and_fertilizer_map():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			use_water_and_fertilizer()
			move(North)
		move(East)

def harvest_map():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			fast_harvest()
			move(North)
		move(East)

def plant_entity_map(entity):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			fast_harvest()
			if get_entity_type() != entity:
				if get_entity_type == Entities.Carrot:
					till()
				plant(entity)
			use_water_and_fertilizer()
			move(North)
		move(East)