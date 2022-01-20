import sys
from itertools import permutations

def solution():

	N = int(sys.stdin.readline().rstrip())

	score_list = list()
	for _ in range(N):
		score_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

	# 순서 조합
	temp_list = list(range(1,9)) # 1 ~ 8 # 1번타자는 4번에 넣어줄 거임
	perms = list(permutations(temp_list))

	max_score = 0 # 점수 체크

	# 순서 별
	for perm in perms:
		# 4번타자 고정
		order = list(perm)
		order.insert(3, 0)

		start_player = 0 # 타자 순번
		out = 0 # 아웃된 플레이어 수
		score = 0 # 점수
		game = 0 # 이닝
		ru1, ru2, ru3 = 0, 0, 0

		# 이닝 별
		while game < len(score_list): # 이닝 수 초과되면 종료, 아웃은 반드시 있으므로 게임은 끝남
			# 게임 시작
			hit = score_list[game][order[start_player]] # 안타: 1, 2루타: 2, 3루타: 3, 홈런: 4, 아웃: 0

			# 다음 타자
			start_player = (start_player + 1) % 9

			if hit == 0: # out 인 경우
				out += 1
				# 겜끝났는지 확인
				if out == 3:
					game += 1  # 이닝 수 올리기
					ru1, ru2, ru3 = 0, 0, 0
					out = 0  # 아웃수 초기화
			elif hit == 1: # 1루타
				score += ru3
				ru1, ru2, ru3 = 1, ru1, ru2
			elif hit == 2: # 2루타
				score += (ru2 + ru3)
				ru1, ru2, ru3 = 0, 1, ru1
			elif hit == 3: # 3루타
				score += (ru1 + ru2 + ru3)
				ru1, ru2, ru3 = 0, 0, 1
			else: # 홈런
				score += (ru1 + ru2 + ru3 + 1)
				ru1, ru2, ru3 = 0, 0, 0  # 초기화

		# 게임이 완전히 끝난 경우
		max_score = max(max_score, score)

	print(max_score)

solution()