

from IPython.display import clear_output

def display_board(board):

	clear_output()

	print('___________________')
	print('|  ' + board[7] +'  |  ' + board[8] +'  |  ' + board[9] + '  |')
	print('|_____|_____|_____|')
	print('|  ' + board[4] +'  |  ' + board[5] +'  |  ' + board[6] + '  |')
	print('|_____|_____|_____|')
	print('|  ' + board[1] +'  |  ' + board[2] +'  |  ' + board[3] + '  |')
	print('|_____|_____|_____|')

test_board = ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']

#display_board(test_board)

##
def player_input():

	marker = ''

	# keep asking player 1 to choose X or O

	while marker != 'X' and marker != 'O':
		marker = input('Player 1, choose X or O: ').upper()

		# assign player 2, the opposite marker
		player1 = marker

		if player1 == 'X':
			player2 = 'O'
		else:
			player2 = 'X'

	print(f'\nPlayer 1 is {player1} and player 2 is {player2}')

	return (player1, player2)

# player_input()

##
def place_marker(board, marker, position):

	board[position] = marker

'''
##
def win_check(board, mark):
	# all ROWS, check if marker matches
	return( (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
	# all COLUMNS, check if marker matches
	(board[7] == mark and board[4] == mark and board[1] == mark) or
	(board[8] == mark and board[5] == mark and board[2] == mark) or
	(board[9] == mark and board[6] == mark and board[3] == mark) or

	# 2 DIAGONALS, check if marker matches
	(board[7] == mark and board[5] == mark and board[3] == mark) or
	(board[9] == mark and board[5] == mark and board[1] == mark) )
'''

def win_check(board, mark):
	# win TIC TAC TOE
	if(
	# all ROWS, check if marker matches
	( board[1] == board[2] == board[3] == mark ) or
	( board[4] == mark and board[5] == mark and board[6] == mark ) or
	( board[7] == board[8] == board[9] == mark ) or

	# all COLUMNS, check if marker matches
	( board[1] == board[4] == board[7] == mark ) or
	( board[2] == mark and board[5] == mark and board[8] == mark ) or
	( board[3] == board[6] == board[9] == mark ) or

	# 2 DIAGONALS, check if marker matches
	( board[1] == board[5] == board[9] == mark ) or
	( board[3] == mark and board[5] == mark and board[7] == mark ) ):

		#print('YOU WON, CONGRATS!')
		return True
	else:
		return False


#win_check(test_board, 'X')


##
import random
def choose_first():

	flip = random.randint(0, 1)

	if flip == 0:
		return 'Player 1'
	else:
		return 'Player 2'

##
def space_check(board, position):

	return board[position] == ' '

##
def full_board_check(board):

	for i in range(1,10):
		if space_check(board, i):
			return False

	# board is full
	return True

##
def player_choice(board):

	position = 0

	while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
		position = int( input(f'{n_player}, enter a position: (1 - 9) ') )

	return position


##
def replay():

	choice = input('play again? (Y or N) ')

	return (choice == 'Y' or choice == 'y')




""" 

(CODING THE GAME)

"""

# while loop to keep running the game

print('Welcome to Tic Tac Toe')

while True:

	## play the game

	# set everything up (board, whos first, choose markers)
	TTT_board = [' '] * 10

	player1_marker, player2_marker = player_input()

	turn = choose_first()

	print('\n' + turn + ' will go first\n' )

	play_game = input('Start the game? ( Y-N ) ')

	if play_game == 'Y' or 'y':
		game_on = True
	elif play_game == 'N' or 'n':
		game_on = False

	# gameplay

	while game_on:

		if turn == 'player 1':

			# show the board
			display_board(TTT_board)
			# choose a position
			n_player = 'Player 1'
			position = player_choice(TTT_board)
			#place the marker
			place_marker(TTT_board, player1_marker, position)

			# check if the won
			if win_check(TTT_board, player1_marker):
				display_board(TTT_board)
				print('\nPlayer 1 has WON!!!')
				game_on = False

			# or check if there is a tie (if not then its player 2 turn)
			else:
				if full_board_check(TTT_board):
					display_board(TTT_board)
					print(' TIE!!')
					break # or (game_on = False)

				else:
					turn = 'player 2'

		else: ## player 2 turn

			# show the board
			display_board(TTT_board)
			# choose a position
			n_player = 'Player 2'
			position = player_choice(TTT_board)
			# place the marker
			place_marker(TTT_board, player2_marker, position)

			# check if the won
			if win_check(TTT_board, player2_marker):
				display_board(TTT_board)
				print('Player 2 has WON!!!')
				game_on = False

			# or check if there is a tie (if not then its player 1 turn)
			else:
				if full_board_check(TTT_board):
					display_board(TTT_board)
					print('TIE!!')
					game_on = False  # or (break)

				else:
					turn = 'player 1'

	# break out of the while loop on replay
	if not replay():
		break































