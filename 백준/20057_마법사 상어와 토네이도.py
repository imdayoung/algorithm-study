import sys


def move():
    print("nn")
    
    
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d = 0
amount = 1

N = int(sys.stdin.readline())
tornado = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cur_x, cur_y = N // 2, N // 2
while cur_x != 1 or cur_y != 1:
    next_x, next_y = move()
    