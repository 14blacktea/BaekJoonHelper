from itertools import product
import copy

def check_max(matrix):
	max_V = 0
	for i in matrix:
		max_V = max(max_V, max(i))
	return max_V

def play_game(matrix, direction):
	if direction == 0: # 왼
		for i in range(len(matrix)):
			temp = [element for element in matrix[i] if element != 0]
			change = list()
			prior = 0
			for element in temp:
				if element == prior:
					change.pop()
					change.append(element * 2)
					prior = 0
				else:
					change.append(element)
					prior = element
			matrix[i] = change + [0] * (len(matrix) - len(change))
	elif direction == 2: # 오른쪽
		for i in range(len(matrix)):
			temp = [element for element in matrix[i] if element != 0]
			change = list()
			prior = 0
			temp.reverse()
			for element in temp:
				if element == prior:
					change.pop()
					change.append(element * 2)
					prior = 0
				else:
					change.append(element)
					prior = element
			matrix[i] = list(reversed(change + [0] * (len(matrix) - len(change))))
	elif direction == 1: # 위
		for i in range(len(matrix)):
			temp = list()
			for j in range(len(matrix)):
				if matrix[j][i] != 0:
					temp.append(matrix[j][i])
			change = list()
			prior = 0
			for element in temp:
				if element == prior:
					change.pop()
					change.append(element * 2)
					prior = 0
				else:
					change.append(element)
					prior = element
			change = change + [0] * (len(matrix) - len(change))
			for j in range(len(matrix)):
				matrix[j][i] = change[j]
	elif direction == 3: # 아래
		for i in range(len(matrix)):
			temp = list()
			for j in range(len(matrix)-1, -1, -1):
				if matrix[j][i] != 0:
					temp.append(matrix[j][i])
			change = list()
			prior = 0
			for element in temp:
				if element == prior:
					change.pop()
					change.append(element * 2)
					prior = 0
				else:
					change.append(element)
					prior = element
			change = change + [0] * (len(matrix) - len(change))
			for j in range(len(matrix)-1, -1, -1):
				matrix[j][i] = change[len(matrix)-1-j]

	return matrix


def solution():
	direction = [0, 1, 2, 3] # 왼, 위, 오, 아

	N = int(input())

	matrix = list()
	for _ in range(N):
		matrix.append(list(map(int, input().split())))

	check = list(product(direction, repeat=5))

	max_V = 0
	for game in check:
		copy_matrix = copy.deepcopy(matrix)
		for dir in game:
			copy_matrix = play_game(copy_matrix, dir)
		# check max
		result = check_max(copy_matrix)
		max_V = max(max_V, result)
	print(max_V)


solution()