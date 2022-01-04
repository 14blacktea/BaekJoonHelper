def solution():
	# E <= 15, S <= 28, M <= 19
	E_N, S_N, M_N = list(map(int, input().split(" ")))
	E_M, S_M,M_M = 0, 0, 0
	while True:
		E = (15 * E_M) + E_N
		S = (28 * S_M) + S_N
		M = (19 * M_M) + M_N
		if E == S and S == M:
			print(E)
			break
		if E < S: E_M += 1
		elif E > S or S < M: S_M += 1
		elif M < S:M_M += 1