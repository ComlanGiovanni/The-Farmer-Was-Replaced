HATS = [
	Hats.Brown_Hat,
	Hats.Cactus_Hat,
	Hats.Carrot_Hat,
	Hats.Dinosaur_Hat,
	Hats.Gold_Hat,
	Hats.Gray_Hat,
	Hats.Green_Hat
]

def fashion_show_achievement():
	drones = []

	def idle():
		pass  # le drone n'a pas besoin de travailler

	for hat in HATS:
		drone = spawn_drone(idle)
		use_item(hat, drone)
		drones.append(drone)

	# attendre que tous les drones soient bien initialisés
	for drone in drones:
		wait_for(drone)
		