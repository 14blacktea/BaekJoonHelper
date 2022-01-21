from collections import deque

def solution():

	N, M, K = map(int, input().split()) # N은 격자, M은 불꽃 수, K는 상어 이동 명령 수

	# move
	# 7 0 1
	# 6   2
	# 5 4 3

	move_x = [0, 1, 1, 1, 0, -1, -1, -1]
	move_y = [-1, -1, 0, 1, 1, 1, 0, -1]

	# 격자 생성
	table = [[deque([]) for _ in range(N)] for _ in range(N)]

	# 불관리
	state = deque([])

	for _ in range(M):
		r, c, m, s, d = map(int, input().split()) # r, c 위치 m은 질량, s는 속력, d는 방향
		r, c = r - 1, c - 1
		table[r][c].append([m, s, d])
		state.append([r, c])

	for _ in range(K):
		temp = []
		temp_state = []
		fire_length = len(state)

		# 이동
		for _ in range(fire_length):
			r, c = state.popleft()
			for _ in range(len(table[r][c])):
				m, s, d = table[r][c].popleft()
				move_r, move_c = (r + (move_y[d] * s)) % N, (c + (move_x[d] * s)) % N
				temp_state.append([move_r, move_c])

				# 여기서 테이블에 미리 넣을 경우, for문 len(table[r][c])만큼 도는데 문제가 있음
				temp.append([move_r, move_c, m, s, d])

		# 이동 완료 후, 추가
		for move_r, move_c, m, s, d in temp:
			table[move_r][move_c].append([m, s, d])

		# print(state) # 이동 확인

		state = deque(temp_state)

		# 이동완료 후, 불 나누기
		fire_length = len(state)
		remove_list = []
		for i in range(fire_length):
			r, c = state[i]
			if len(table[r][c]) >= 2: # 2개 이상이라면
				total_m = 0
				total_s = 0
				length = len(table[r][c])
				prior_d = table[r][c][0][2]
				check = True
				while table[r][c]:
					m, s, d = table[r][c].popleft() # 요소를 하나씩 뽑아서 처리
					total_m += m
					total_s += s
					if (prior_d - d) % 2 != 0:
						check = False
					prior_d = d
				# 방향 정하기
				spread_d = [0, 2, 4, 6]
				if not check: spread_d = [1, 3, 5, 7]
				# print(total_m, total_s)
				# 변화된 m과 s
				total_m //= 5
				total_s //= length
				# m이 0이라면 소멸
				if total_m == 0:
					remove_list.append(i)
					continue
				# 분리된 불
				for move_d in spread_d:
					table[r][c].append([total_m, total_s, move_d])

		remove_list.reverse()

		if remove_list:
			for i in remove_list:
				del state[i]
		# print(table)

	# print(table)

	total = 0
	while state:
		r, c = state.popleft()
		for _ in range(len(table[r][c])):
			m, _, _ = table[r][c].popleft()
			total += m

	print(total)

solution()