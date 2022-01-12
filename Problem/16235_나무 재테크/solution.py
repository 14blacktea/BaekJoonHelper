import sys


coord_x = [1, -1, 0, 0, 1, -1, 1, -1]
coord_y = [0, 0, 1, -1, 1, 1, -1, -1]
# coord_x = [-1, 0, 1, -1, 1, -1, 0, 1]
# coord_y = [-1, -1, -1, 0, 0, 1, 1, 1]

N, M, K = map(int, sys.stdin.readline().split())

# N은 좌표 크기
soil = list()
for i in range(N):
	soil.append(list(map(int, sys.stdin.readline().split())))

current = [[5] * N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]

# M은 나무 수
for _ in range(M):
	X, Y, Age = map(int, sys.stdin.readline().split())
	tree[X-1][Y-1].append(Age)

for _ in range(K):
	# 1년
	for i in range(N):
		for j in range(N):
			if tree[i][j]:  # 나무가 있는 경우
				tree[i][j].sort()
				add_food = 0
				update_tree = []
				for k in tree[i][j]:
					if k <= current[i][j]:
						current[i][j] -= k
						update_tree.append(k+1)
					else:
						add_food += (k // 2)
				tree[i][j] = []
				tree[i][j].extend(update_tree)
				current[i][j] += add_food
	# print("spring summer", tree, current)

	if not tree:
		print(0)
		sys.exit()

	for i in range(N):
		for j in range(N):
			if tree[i][j]:
				for k in tree[i][j]:
					if k % 5 == 0:
						for num in range(8):
							temp_x, temp_y = i + coord_x[num], j + coord_y[num]
							# if temp_x < 0 or temp_x >= N or temp_y < 0 or temp_y >= N:
							# 	continue
							if 0 <= temp_x < N and 0 <= temp_y < N:
								tree[temp_x][temp_y].append(1)
							# tree[temp_x][temp_y].extend([1] * len(temp))
			current[i][j] += soil[i][j]
	# print("fall winter", tree, current)

count = 0
for i in range(N):
	for j in range(N):
		count += len(tree[i][j])
print(count)

# 시간초과가 매우 심한 문제였다.
# Pypy3를 안쓰고 Python3로하면 통과가 되지 않는다.