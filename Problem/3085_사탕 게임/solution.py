import sys

def max_value(M):
	max = 0
	# Check
	for i in range(len(M[0])):
		count = 0
		prior = None
		for j in range(len(M[0])):
			if M[i][j] == prior:
				count += 1
			else:
				count = 1
				prior = M[i][j]
			if max < count: max = count

	# Transpose
	for i in range(len(M[0])):
		count = 0
		prior = None
		for j in range(len(M[0])):
			if M[j][i] == prior:
				count += 1
			else:
				count = 1
				prior = M[j][i]
			if max < count: max = count

	return max

def solution():
	N = int(sys.stdin.readline().rstrip())
	M = []
	for _ in range(N):
		M.append(list(sys.stdin.readline().rstrip()))

	# 현재 맥스값 확인
	max = max_value(M)
	if max == N:
		print (max)
		return
	# 아래랑, 오른쪽만 보면 되제
	x = [0, 1]
	y = [1, 0]

	# 각 요소를 돌면서
	for i in range(N):
		for j in range(N):
			down, right = None, None
			currentCandy = M[i][j]
			if i != N - 1: down = M[i + y[0]][j + x[0]]
			if j != N - 1: right = M[i + y[1]][j + x[1]]
			nearCandy = [down, right]
			for idx, near in enumerate(nearCandy):
				if near == None or near == currentCandy:
					continue

				# 인접 교환
				M[i][j] = near
				M[i + y[idx]][j + x[idx]] = currentCandy
				# 맥스 값 설정
				temp = max_value(M)
				# 되돌리기
				M[i][j] = currentCandy
				M[i + y[idx]][j + x[idx]] = near
				if temp > max: max = temp
				if max == N:
					print(max)
					return
	print(max)

	# 생각해보니, 왼쪽과 위쪽은 바꿔볼 필요가 없다
	# 순차적으로 진행하며, 아래쪽과 오른쪽만 바꿔보면 충분
	# 또한, 행렬 교환에서 deepcopy를 이용하여 행렬을 복사하고 바꾸는 과정을 진행했는데
	# 이것 보단, 다시 원상복귀 시켜주는게 더 빠른 듯 하다
	# Todo: 지금은 연결의 최대 값을 찾을 때 행렬 전체에 대해서 반복문을 수행하지만, 그럴 필요 없이 바뀐 행렬에 대해서만 최대 연결 수를 찾도록 개선 가능