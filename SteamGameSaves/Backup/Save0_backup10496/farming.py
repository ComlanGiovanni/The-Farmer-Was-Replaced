# CROP MANAGEMENT - Generic

def handle_crop(crop_type):
	harvest_if_ready()
	if get_entity_type() != crop_type:
		plant(crop_type)
	watering_grounds()
	fertilize()

def handle_grass():
	harvest_if_ready()
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	water_and_fertilize()

def handle_tree():
	harvest_if_ready()
	if get_entity_type() != Entities.Tree:
		plant(Entities.Tree)
	water_and_fertilize()
		
def handle_carrot():
	harvest_if_ready()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	water_and_fertilize()

def handle_sunflower():
	harvest_if_ready()
	if get_entity_type() != Entities.Sunflower:
		plant(Entities.Sunflower)
	water_and_fertilize()

def handle_cactus():
	harvest_if_ready()
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)
	water_and_fertilize()
	
def handle_pumpkin():
	entity = get_entity_type()
	
	if can_harvest():
		harvest()
	
	if entity == Entities.Dead_Pumpkin or entity == None:
		plant(Entities.Pumpkin)
	
	water_and_fertilize()