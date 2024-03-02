import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
belts = deque(list(map(int, sys.stdin.readline().split())))
robot_on_belts = deque([False] * N * 2)
broken = 0
cnt = 0

while broken < K:
    # 1. 벨트 회전
    belts.appendleft(belts.pop())
    robot_on_belts.appendleft(robot_on_belts.pop())

    # 1-1. 로봇이 내리는 위치에 도달하면 즉시 내림
    if robot_on_belts[N - 1]:
        robot_on_belts[N - 1] = False

    # 2. 가장 먼저 벨트에 올라간 로봇부터 이동할 수 있다면 이동
    for i in range(N - 2, -1, -1):
        if robot_on_belts[i] and not robot_on_belts[i + 1] and belts[i + 1] > 0:
            robot_on_belts[i] = False
            robot_on_belts[i + 1] = True
            belts[i + 1] -= 1
            if belts[i + 1] == 0:
                broken += 1
            if i + 1 == N - 1:
                robot_on_belts[i + 1] = False

    # 3. 올리는 위치에 있는 칸의 5내구도가 0이 아니면 올리는 위치에 로봇 올림
    if belts[0] > 0:
        robot_on_belts[0] = True
        belts[0] -= 1
        if belts[0] == 0:
            broken += 1

    cnt += 1
    
print(cnt)