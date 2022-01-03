from collections import deque
import copy

def solution():
	# 사용될 간선 수와 시작점
	visit_num, lines, start = list(map(int, input().split()))

	# 연결 정리 (양방향 고려)
	connect = dict()
	for _ in range(lines):
		a, b = list(map(int, input().split()))
		# a
		if a in connect.keys():
			connect[a].append(b)
			connect[a].sort()
		else: connect[a] = [b]
		# b
		if b in connect.keys():
			connect[b].append(a)
			connect[b].sort()
		else: connect[b] = [a]

	# for bfs copy
	connect_b = copy.deepcopy(connect)

	# dfs
	dfs = []
	visit = [False] * (visit_num + 1)

	# 첫번째 처리
	stack = [start]
	while True:
		# 방문 요소가 없음
		if not stack:
			break
		# 뒤에서 부터 빼면서 방문 요소가 있을 경우, 방문 처리
		target = stack.pop()
		if visit[target]: continue # 이미 방문한 경우
		visit[target] = True # 방문 처리
		dfs.append(target)
		try: # 방문 요소를 뒤에 붙임
			adds = connect[target] # pop으로 빼낼 때 작은 수부터 빼야하므로 거꾸로 붙여줘야함
			adds.reverse()
			checked_adds = [i for i in adds if not visit[i]]
			stack.extend(checked_adds)
		except: # 연결된 요소가 없는 경우
			continue

	print(" ".join(list(map(str, dfs))))

	# bfs
	bfs = []
	visit = [False] * (visit_num + 1)

	# 첫번째 처리
	deque_ = deque([start])
	while True:
		# 방문 요소가 없음
		if not deque_:
			break
		# 앞에서 부터 빼면서 방문 요소가 있을 경우, 방문 처리
		target = deque_.popleft()
		if visit[target]: continue # 이미 방문한 경우
		visit[target] = True # 방문 처리
		bfs.append(target)
		try: # 방문 요소를 뒤에 붙임
			adds = connect_b[target]
			checked_adds = [i for i in adds if not visit[i]]
			deque_.extend(checked_adds)
		except: # 연결된 요소가 없는 경우
			continue

	print(" ".join(list(map(str, bfs))))