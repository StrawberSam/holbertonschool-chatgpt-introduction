def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 5)

def check_winner(board):
	# Vérifie les lignes
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	# Vérifie les colonnes
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True

	# Diagonales
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True

	return False

def is_full(board):
	return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	player = "X"

	while not check_winner(board) and not is_full(board):
		print_board(board)
		try:
			row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
			col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

			if 0 <= row <= 2 and 0 <= col <= 2:
				if board[row][col] == " ":
					board[row][col] = player
					player = "O" if player == "X" else "X"
				else:
					print("That spot is already taken! Try again.\n")
			else:
				print("Invalid input. Row and column must be between 0 and 2.\n")
		except ValueError:
			print("Please enter a valid number!\n")

	print_board(board)
	if check_winner(board):
		print("Player " + ("O" if player == "X" else "X") + " wins! 🎉")
	else:
		print("It's a draw! 🤝")

tic_tac_toe()
