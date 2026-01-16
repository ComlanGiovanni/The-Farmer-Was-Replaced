from movement import *

# ===== VÉRIFICATIONS DE POSITION =====
def is_origin():
	return get_pos_x() == 0 and get_pos_y() == 0

def is_valid_position(x, y):
	world_size = get_world_size()
	return 0 <= x < world_size and 0 <= y < world_size

def display_drone_position():
	print("Position: (" + str(get_pos_x()) + ", " + str(get_pos_y()) + ")")

def origin():
	if is_origin():
		return
	
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def zig_zag_origin():
	if is_origin():
		return
	
	while not is_origin():
		if get_pos_x() > 0:
			move(West)
		if get_pos_y() > 0:
			move(South)

def goto_pos(target_x, target_y):
	if not is_valid_position(target_x, target_y):
		print("Position hors de la carte: (" + str(target_x) + ", " + str(target_y) + ")")
		return False
	
	dx = target_x - get_pos_x()
	dy = target_y - get_pos_y()
	
	if dx > 0:
		move_n_times(1, dx)   # Est
	elif dx < 0:
		move_n_times(3, -dx)  # Ouest
	
	if dy > 0:
		move_n_times(0, dy)   # Nord
	elif dy < 0:
		move_n_times(2, -dy)  # Sud
	
	return True