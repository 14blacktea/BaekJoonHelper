import sys

def solution():
	N = int(input())
	S = set()

	for i in range(N):
		# x가 없는 경우
		cmd = sys.stdin.readline().rstrip().split(" ")
		if len(cmd) == 1:
			if cmd[0] == "all": S = set(range(1, 21))
			else: S.clear()
			continue
		# x가 존재하는 경우
		cmd, x = cmd[0], int(cmd[1])
		if cmd == "add": S.add(x)
		elif cmd == "check": print(1) if x in S else print(0)
		elif cmd == "remove": S.discard(x)
		elif cmd == "toggle":
			try: S.remove(x)
			except: S.add(x)

	# 당연히 add, check, remove, toggle의 사용이 all 보다 월등히 많을거라 생각해서 문자열로 처리 진행했었음
	# all 부분을 set(map(str, range(1, 21)))하고
	# 15번째 줄을 cmd = cmd, x로 하여 int형 변환없이 문자열로 처리하여 진행했으나 시간 초과가 남
	# all을 무지성으로 엄청 많이 반복하는 테스트 케이스가 존재하는 듯함