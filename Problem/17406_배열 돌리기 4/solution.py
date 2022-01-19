import copy
from itertools import permutations
import sys

def check_min_value(arr):
	return min([sum(i) for i in arr])

def do_rotate(arr, r, c, s):
	temp_arr = copy.deepcopy(arr)
	for i in range(1, s + 1):
		# 행처리
		for k in range(c-1-i, c-1+i):
			arr[r-1-i][k+1] = temp_arr[r-1-i][k] # 첫 행
		for k in range(c-1+i, c-1-i, -1):
			arr[r-1+i][k-1] = temp_arr[r-1+i][k] # 마지막 행

		# 열처리
		for k in range(r-1-i, r-1+i):
			arr[k+1][c-1+i] = temp_arr[k][c-1+i] # 오른쪽 열
		for k in range(r-1+i, r-1-i, -1):
			arr[k-1][c-1-i] = temp_arr[k][c-1-i] # 오른쪽 열

	return arr

def solution():
	# N, M, K
	N, M, K = map(int, sys.stdin.readline().rstrip().split())

	arr = []
	for _ in range(N):
		arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

	K_arr = []
	for _ in range(K):
		K_arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

	perm = list(range(K))
	perm = list(permutations(perm))
	# print(perm) # 순열
	# 원본 arr
	# print(arr)

	answers = []

	# 순열마다
	for each_perm in perm:
		# 원본 복사
		rotate_arr = copy.deepcopy(arr)
		# 순서에 맞게 rotate 시전
		for each_K in each_perm:
			r, c, s = K_arr[each_K]
			rotate_arr = do_rotate(rotate_arr, r, c, s)
		# rotate 시전 후, 가장 작은 값 append
		min_value = check_min_value(rotate_arr)
		if min_value == 0:
			print(0)
			return
		answers.append(min_value)

	# 가장 작은 값 출력
	print(min(answers))

solution()