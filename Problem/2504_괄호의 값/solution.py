def solution():

	inputString = input()

	# 값이 없거나 하나인 경우
	if len(inputString) == 0 or len(inputString) == 1:
		print(0)
		return

	N = list() # 스택
	for i in inputString:
		# print(N)
		# 좌괄호는 상관 없음
		if i == "(" or i == "[":
			N.append(i)
			continue
		# 우괄호 처리
		if i == ")":
			if not '(' in N: # 처음으로 들어온 경우, 올바르지 않음, 길이가 0인지 확인하는 건 올바르지 못함 -> 숫자만 있을 수 있음
				print(0)
				return
			if N[-1] == "(": # 알맞음 2로 변환
				N.pop()
				# 그 이전 값이 숫자라면 더해줌
				if len(N) == 0: # 그 이전 값이 없는 경우
					N.append(str(2))
					continue
				if N[-1].isdigit(): N.append(str(int(N.pop()) + 2)) # 그 이전 값이 숫자 인 경우 더해주고
				else: N.append(str(2)) # 아니라면 2를 추가
			elif N[-1].isdigit(): # 마지막 값이 숫자라면
				# 그 이전 값 확인
				if N[-2] == "(": # 알맞은 경우, 2배
					temp = int(N.pop()) * 2
					N.pop()
					# 그 이전 값이 숫자라면 더해줌
					if len(N) == 0: # 그 이전 값이 없는 경우
						N.append(str(temp))
						continue
					if N[-1].isdigit(): N.append(str(int(N.pop()) + temp)) # 그 이전 값이 숫자 인 경우 더해주고
					else: N.append(str(temp)) # 아니라면 그대로 추가
				else: # ]가 들어온 경우, 올바르지 못함
					print(0)
					return
			else:
				print(0)
				return

		# 우괄호 처리 2
		if i == "]":
			if not '[' in N: # 처음으로 들어온 경우, 올바르지 않음
				print(0)
				return
			if N[-1] == "[": # 올바르게 들어온 경우 3으로 변환
				N.pop()
				# 그 이전 값이 숫자라면 더해줌
				if len(N) == 0: # 그 이전 값이 없는 경우
					N.append(str(3))
					continue
				if N[-1].isdigit(): N.append(str(int(N.pop()) + 3)) # 그 이전 값이 있다면 3을 더해줌
				else: N.append(str(3)) # 없다면 그냥 3을 추가
			elif N[-1].isdigit(): # 그 이전값이 숫자 인 경우
				if N[-2] == "[": # 알맞게 들어온 것임
					temp = int(N.pop()) * 3 # * 3배 해줌
					N.pop()
					# 그 이전 값이 숫자라면 더해줌
					if len(N) == 0: # 그 이전 값이 없는 경우
						N.append(str(temp))
						continue
					if N[-1].isdigit(): N.append(str(int(N.pop()) + temp)) # 그 이전값이 숫자 인경우 더해줌
					else: N.append(str(temp)) # 아닌 경우 그대로
				else: # '('인 경우, 잘못들어온 것임
					print(0)
					return
			else:
				print(0)
				return

	if "(" in N or ")" in N or "[" in N or "]" in N:
		print(0)
		return
	else:
		print(N[0])

	# 좌괄호는 상관없음
	# 우괄호가 들어오면 스택의 마지막을 확인 -> 올바르게 닫혔는지, 숫자인지
	# 숫자로 변환후에도 스택의 마지막 값을 또 확인하여 숫자라면 더해주어야함
	# 이러한 과정을 모두 거친 뒤, 괄호가 남아있다면 잘못된 경우임 ex. ((((

# solution()