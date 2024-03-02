import sys


N = int(sys.stdin.readline())
towel = list(map(int, sys.stdin.readline().split()))
answer = [0] * N

stack = []
for t in range(N):
    # stack이 비어있는 경우
    if not stack:
        answer[t] = 0
        stack.append((t + 1, towel[t]))

    # 현재 탑의 높이가 stack의 가장 위 탑의 높이보다 높을 경우
    elif towel[t] > stack[-1][1]:
        while stack and towel[t] > stack[-1][1]:
            stack.pop()
        if stack:
            answer[t] = stack[-1][0]
        stack.append((t + 1, towel[t]))
    
    # 현재 탑의 높이가 stack의 가장 위 탑의 높이보다 낮을 경우
    elif towel[t] < stack[-1][-1]:
        answer[t] = stack[-1][0]
        stack.append((t + 1, towel[t]))

print(*answer)