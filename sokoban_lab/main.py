import sokoban
import display_sokoban
import curses

boards = sokoban.create_board('first_level.sokoban')
max_x = 0
max_y = 0
for board in boards[0]:
	if board[0] > max_x:
		max_x = board[0]
	if board[1] > max_y:
		max_y = board[1]
while(True):
	display_sokoban.display_sokoban(boards, (max_x,max_y))
	change_pos = input("Where?")	
	directions = {
				"w": (-1,0),
				"a": (0,-1),
				"s": (1,0),
				"d": (0, 1)
			}
	if change_pos in directions:
		change_pos = directions[change_pos]
		sokoban.move_player(boards, change_pos)
	elif change_pos == "q":
		exit()
	else:
		print("wasd to move, q to quit.")

