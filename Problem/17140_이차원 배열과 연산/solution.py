from collections import Counter

def check(arr):
	new_arr = []
	max = 0
	for i in arr:
		temp_arr = []
		temp = dict(Counter(i)) # [(수, 수의 등장횟수)]
		temp = sorted(temp.items(), key=lambda item: (item[1], item[0]))
		for value, count in temp:
			if value == 0: continue
			temp_arr.extend([value, count])
		if max < len(temp_arr):
			max = len(temp_arr)
		new_arr.append(temp_arr)

	for i in range(len(new_arr)):
		if len(new_arr[i]) < max:
			new_arr[i].extend(([0] * (max - len(new_arr[i]))))

	return new_arr, max

def transpose(arr):
	new_arr = list(map(list, zip(*arr)))
	return new_arr

def solution():
	R, C, K = map(int, input().split())
	R -= 1
	C -= 1

	second = 0
	arr = []
	for _ in range(3):
		arr.append(list(map(int, input().split())))

	# 0초
	try:
		if arr[R][C] == K:
			print(second)
			return
	except:
		pass

	garo = 3
	sero = 3
	while True:
		if sero >= garo: # 행의 개수 >= 열의 개수
			arr, garo = check(arr)
		else: # 행의 개수 < 열의 개수
			arr = transpose(arr)
			arr, sero = check(arr)
			arr = transpose(arr)
		second += 1
		try:
			if arr[R][C] == K:
				print(second)
				break
		except:
			pass
		if second == 100:
			print(-1)
			break

solution()