# 맞닿는 곳의 인덱스: 2(오른쪽), 6(왼쪽)
# 맞닿은 극이 다르면 반대 방향으로 회전
import sys
from collections import deque


def rotate(n, d):
    next_gears = [deque([]) for _ in range(T)]
    # 왼쪽 기어
    for i in range():
        if gears[i][2] == gears[i + 1][6]:
            break
        if d == 1:
        gears[i]
        next_gears[i] = 
        d *= -1
        
    # 오른쪽 기어
    for i in range(n + 1, T):
        
    return next_gears


T = int(sys.stdin.readline())
gears = [deque(list(map(int, sys.stdin.readline().rstrip()))) for _ in range(T)]
print(gears)

K = int(sys.stdin.readline())
for _ in range(K):
    gear, direction = map(int, sys.stdin.readline().split())
    gears = rotate(gear - 1, direction)
    