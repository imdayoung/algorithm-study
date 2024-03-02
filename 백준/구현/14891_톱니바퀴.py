from collections import deque
import sys
import copy


def rotate(n, d):
    # 시계 방향
    if d == 1:
        gears_temp[n].appendleft(gears_temp[n].pop())
    # 반시계 방향
    else:
        gears_temp[n].append(gears_temp[n].popleft())


left, right = 6, 2

gears = [deque(list(map(int, sys.stdin.readline().rstrip()))) for _ in range(4)]
gears_temp = copy.deepcopy(gears)

K = int(sys.stdin.readline())
for _ in range(K):
    n, d = map(int, sys.stdin.readline().rstrip().split())
    n -= 1
    rotate(n, d)
    queue = deque([(n, d)])
    visited = [False] * 4
    visited[n] = True
    while queue:
        n, d = queue.popleft()
        d *= -1
        for next_n in [n + 1, n - 1]:
            if next_n > 3 or next_n < 0:
                continue
            if not visited[next_n]:
                visited[next_n] = True
                if (next_n == n + 1 and gears[next_n][left] != gears[n][right]) or (next_n == n - 1 and gears[next_n][right] != gears[n][left]):
                    rotate(next_n, d)
                    queue.append((next_n, d))
    gears = copy.deepcopy(gears_temp)

result = 0
for i in range(4):
    if gears[i][0] == 1:
        result += 2 ** i
print(result)