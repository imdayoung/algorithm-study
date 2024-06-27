import sys
from collections import deque
import copy


def rotate_by_direction(gear, n, d):
    if d == 1:
        gear[n].appendleft(gear[n].pop())
    else:
        gear[n].append(gear[n].popleft())

    return gear


def get_rotated_gear(n, d):
    next_gears = rotate_by_direction(copy.deepcopy(gears), n, d)
    
    d_left = d * -1
    for i in range(n - 1, -1, -1):
        if gears[i][2] == gears[i + 1][6]:
            break
        next_gears = rotate_by_direction(next_gears, i, d_left)
        d_left *= -1
        
    d_right = d * -1
    for i in range(n + 1, T):
        if gears[i][6] == gears[i - 1][2]:
            break
        next_gears = rotate_by_direction(next_gears, i, d_right)
        d_right *= -1
        
    return next_gears


answer = 0

T = int(sys.stdin.readline())
gears = [deque(list(map(int, sys.stdin.readline().rstrip()))) for _ in range(T)]

K = int(sys.stdin.readline())
for _ in range(K):
    gear, direction = map(int, sys.stdin.readline().split())
    gears = get_rotated_gear(gear - 1, direction)
    
for gear in gears:
    if gear[0] == 1:
        answer += 1
        
print(answer)
