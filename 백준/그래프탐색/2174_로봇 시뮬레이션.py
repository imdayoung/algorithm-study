import sys


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction_dict = {'N':0, 'E':1, 'S':2, 'W':3}

A, B = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(A)] for _ in range(B)]

N, M = map(int, sys.stdin.readline().split())
directions = {}
locations = {}
for i in range(1, N + 1):
    x, y, d = map(str, sys.stdin.readline().split())
    graph[B - int(y)][int(x) - 1] = i
    locations[i] = (B - int(y), int(x) - 1)
    directions[i] = direction_dict[d]

commands = []
for _ in range(M):
    robot, command, repeat = map(str, sys.stdin.readline().split())
    commands.append((int(robot), command, int(repeat)))
    
for robot, command, repeat in commands:
    if command == 'L':
        directions[robot] = (directions[robot] - repeat) % 4
    elif command == 'R':
        directions[robot] = (directions[robot] + repeat) % 4
    elif command == 'F':
        for _ in range(repeat):
            nx = locations[robot][0] + dx[directions[robot]]
            ny = locations[robot][1] + dy[directions[robot]]
            if nx < 0 or nx > B - 1 or ny < 0 or ny > A - 1:
                print(f"Robot {robot} crashes into the wall")
                exit()
            if graph[nx][ny] != 0:
                print(f"Robot {robot} crashes into robot {graph[nx][ny]}")
                exit()

            graph[locations[robot][0]][locations[robot][1]] = 0
            graph[nx][ny] = robot
            locations[robot] = (nx, ny)

print("OK")