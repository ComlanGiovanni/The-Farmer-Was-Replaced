def farm_grass_callback(x, y):
	handle_grass()

def farm_carrot_callback(x, y):
	handle_carrot()

def farm_sunflower_callback(x, y):
	handle_sunflower()

def farm_cactus_callback(x, y):
	handle_cactus()

def farm_trees_checkerboard(x, y):
	if not is_even(x + y):
		handle_tree()