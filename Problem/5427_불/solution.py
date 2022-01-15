from collections import deque

def solution():

	TestNum = int(input())

	# 북, 서, 동, 남
	coord_x = [0, -1, 1, 0]
	coord_y = [-1, 0, 0, 1]

	for _ in range(TestNum):
		M, N = map(int, input().split()) # M은 열, N은 행
		# 빌딩 구성
		building = list()
		fire_coord = deque([])
		SK = deque([])
		for idx in range(N):
			temp = list(input())
			for jdx, check in enumerate(temp):
				if check == "*": fire_coord.append([idx, jdx]) # 행렬
				elif check == "@": SK.append([idx, jdx]) # 행렬
			building.append(temp)

		start = 1  # 상근이 이동 시작
		building[SK[0][0]][SK[0][1]] = 1 # 상근이가 탈출구에 있을 수도 있음
		if SK[0][0] == 0 or SK[0][0] == N - 1 or SK[0][1] == 0 or SK[0][1] == M - 1:
			print(1)
			continue

		update_check = False # 끝에 도달한 경우

		while True:
			keep = []
			# 불 퍼져라
			for _ in range(len(fire_coord)):
				X, Y = fire_coord.popleft()
				for i in range(4):
					temp_X, temp_Y = X + coord_x[i], Y + coord_y[i]
					if temp_X < 0 or temp_X >= N or temp_Y < 0 or temp_Y >= M:
						continue
					value = building[temp_X][temp_Y]
					if value != "#" and value != "*":
						if building[temp_X][temp_Y] == start: keep.append([temp_X, temp_Y])
						else:
							building[temp_X][temp_Y] = "*"
							fire_coord.append([temp_X, temp_Y])

			count = 0 # 상근이 이동이 없다면 break

			start += 1

			# 상근아 이동하자
			for _ in range(len(SK)):
				X, Y = SK.popleft()
				for i in range(4):
					temp_X, temp_Y = X + coord_x[i], Y + coord_y[i]
					if temp_X < 0 or temp_X >= N or temp_Y < 0 or temp_Y >= M:
						# print(X, Y, temp_X, temp_Y)
						continue
					value = building[temp_X][temp_Y]
					# print(value, temp_X, temp_Y)
					if value == ".":
						if temp_X == 0 or temp_X == N - 1 or temp_Y == 0 or temp_Y == M - 1:
							print(start)
							update_check = True
							break
						building[temp_X][temp_Y] = start
						SK.append([temp_X, temp_Y])
						count += 1

				if update_check:
					break

			if count == 0 or update_check: break

			for X, Y in keep:
				building[X][Y] = "*"

		# print(building)

		if not update_check:
			print("IMPOSSIBLE")

solution()