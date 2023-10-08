import sys

def create_board(f):
	board = {}
	boardMovable = {}
	if f:
		with open(f, 'r') as boards:
			line_list = boards.readlines()
			maxy = 0
			boxes = 1
			for x in range(len(line_list)):
				if len(line_list[x]) > maxy:
					maxy = len(line_list[x])
				for y in range(len(line_list[x])):
					if line_list[x][y] == '#':
						create_wall(board, (x, y))
					elif line_list[x][y] == '.':
						create_loading_place(board, (x, y))
					elif line_list[x][y] == 'o':
						create_box(boardMovable, (x, y), boxes)
						boxes += 1
					elif line_list[x][y] == '@':
						create_player(boardMovable, (x, y))
	boards = [board, boardMovable]
	return boards

def create2_board(line_list):
	board = {}
	boardMovable = {}
	boxes = 1
	for x in range(len(line_list)):
		for y in range(len(line_list[x])):
			if line_list[x][y] == '#':
				create_wall(board, (x, y))
			elif line_list[x][y] == '.':
				create_loading_place(board, (x, y))
			elif line_list[x][y] == 'o':
				create_box(boardMovable, (x, y), boxes)
				boxes += 1
			elif line_list[x][y] == '@':
				create_player(boardMovable, (x, y))
	return board

def create_board_menu(f_lvls):
	board_menu = {}
	level = []
	if f_lvls:
		with open(f_lvls, 'r') as levels:
			level_counter = 1
			line_list = levels.readlines()
			for x in range(len(line_list)):
				if line_list[x] == '\n':
					board_menu[level_counter] = level
					level_counter += 1
					level = []
				else:
					level.append(line_list[x])
	return board_menu

def create_wall(board, pos):
	board[pos] = '#'

def create_box(board, pos, name):
	board[pos] = name

def create_loading_place(board, pos):
	board[pos] = '.'

def create_player(board, pos):
	board[pos] = "@"

def move_player(boards, change_pos):
	board = boards[0]	
	boardMovable =boards[1]
	player_pos = list(boardMovable.keys())[list(boardMovable.values()).index("@")]
	new_pos = (player_pos[0] + change_pos[0], player_pos[1] + change_pos[1])
	print(new_pos)
	if new_pos in board:
		if board[new_pos] == '#':
			return False
	if new_pos in boardMovable:
		if move_box(boards, change_pos, new_pos):	
			create_player(boardMovable, new_pos)
			boardMovable.pop(player_pos)
			return True
		else:
			return False
	else:
		create_player(boardMovable, new_pos)
		boardMovable.pop(player_pos)
		return True
#def move_player(board, c_pos):
#	new_pos = (board['@'][0] + c_pos[0], board['@'][1] + c_pos[1])
#	print(new_pos)
#	if new_pos in board:
#		if board[new_pos] == '#':
#			return False
#		if board[new_pos].__contains__('BOX'):
#			if move_box(board, c_pos, list(board.keys())[list(board.values()).index(new_pos)]):
#				set_player_pos(board, new_pos)
#				return True
#			else:
#				return False
#		else:
#			set_player_pos(board, new_pos)
#			return True
#	else:
#		set_player_pos(board, new_pos)
#		return True
#		

def move_box(boards, change_pos, pos):
	board = boards[0]
	boardMovable = boards[1]
	new_pos = (pos[0] + change_pos[0], pos[1] + change_pos[1])
	if new_pos in board: 
		if board[new_pos] == '#':
			return False
	if new_pos in boardMovable:
		if isinstance(boardMovable[new_pos], int):
			return False
	else:
		create_box(boardMovable, new_pos, boardMovable[pos])
		boardMovable.pop(pos)
		return True
