directions = [North, East, South, West]

def move_up():
	if get_pos_y() < get_world_size() - 1:
		move(North)

def move_down():
	if get_pos_y() > 0:
		move(South)

def move_right():
	if get_pos_x() < get_world_size() - 1:
		move(East)

def move_left():
	if get_pos_x() > 0:
		move(West)

def move_diagonal_up_right():
	move_up()
	move_right()

def move_diagonal_up_left():
	move_up()
	move_left()

def move_diagonal_down_right():
	move_down()
	move_right()

def move_diagonal_down_left():
	move_down()
	move_left()

def move_n_times(direction_index, n):
	for i in range(n):
		move(directions[direction_index])

def move_to_edge_horizontal(direction):
	world_size = get_world_size()
	
	if direction == "right":
		while get_pos_x() < world_size - 1:
			move(East)
	elif direction == "left":
		while get_pos_x() > 0:
			move(West)

def move_to_edge_vertical(direction):
	world_size = get_world_size()
	
	if direction == "up":
		while get_pos_y() < world_size - 1:
			move(North)
	elif direction == "down":
		while get_pos_y() > 0:
			move(South)