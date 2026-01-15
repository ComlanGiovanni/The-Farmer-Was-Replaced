while True:
	sort_cactus_wrong_order()
	clear_map_with_drones()

	till_entire_map_with_drones()
	
	farm_with_drones(farm_grass_callback)
	
	clear_map_with_drones()

	farm_with_drones(farm_trees_checkerboard)
	
	clear_map_with_drones()
	
	farm_with_drones(farm_carrot_callback)
	
	clear_map_with_drones()
	
	farm_sunflowers()
	
	clear_map_with_drones()
	
	farm_mega_pumpkin()
	
	clear_map_with_drones()
	
	farm_cactus()

	clear_map_with_drones()
	
	farm_maze()