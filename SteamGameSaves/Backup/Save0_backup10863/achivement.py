from core import *

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
			