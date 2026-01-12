HATS = [
	Hats.Brown_Hat,
	Hats.Cactus_Hat,
	Hats.Carrot_Hat,
	Hats.Dinosaur_Hat,
	Hats.Gold_Hat,
]

def fashion_show_achievement():
	drones = []

	for hat in HATS:
		def drone_task(h=hat):
			change_hat(h)
			# le drone peut terminer immédiatement

		drone = spawn_drone(drone_task)
		if drone is not None:
			drones.append(drone)
			