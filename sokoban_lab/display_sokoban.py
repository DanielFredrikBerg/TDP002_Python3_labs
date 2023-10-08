import sokoban

def display_sokoban(boards, dimensions):
	board = boards[0]
	boardMovable = boards[1]
	height = dimensions[0] + 1
	width = dimensions[1] + 1
	for x in range(height):
		for y in range(width):
			if (x, y) in boardMovable:
				if isinstance(boardMovable[(x,y)], int):
					print('o', end='')
				else:
					print(boardMovable[(x, y)], end='')
			elif (x, y) in board.keys():
				print(board[(x,y)], end='')
			else:
				print(' ', end='')
		print()
