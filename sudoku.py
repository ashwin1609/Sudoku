import numpy as np

board = []
print("Enter the values for the Board:")
for i in range(9):
	matrix = []
	for j in range(9):
		matrix.append(int(input()))
	board.append(matrix)


# Function to check if the numbers are not repeated in a row/column or within the box
def checker(board, y, x, num):
	# checks row
	for i in range(9):
		if board[y][i] == num:
			return False
	# checks column
	for j in range(9):
		if board[j][x] == num:
			return False
	# checks within the box
	x0 = (x//3)*3
	y0 = (y//3)*3

	for i in range(0, 3):
		for j in range(0, 3):
			if board[y0+i][x0+j] == num:
				return False

	return True


def solver(board):

	# finds the empty box
	# Empty box is given by zero
	# Traverse through each row
	for i in range(9):
		# Traverse through each column
		for j in range(9):
			if board[i][j] == 0:
				# Try each number between 1 and 10
				for num in range(1,10):
					if checker(board,i,j,num):
						board[i][j] = num
						solver(board)
						# if no option was possible
						board[i][j] = 0
				return False
	print(np.matrix(board))


solver(board)
