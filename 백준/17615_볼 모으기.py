import sys


N = int(sys.stdin.readline())
balls = list(map(str, sys.stdin.readline().rstrip()))

cur = N - 2     # 현재 index
comp = N - 1    # 비교 대상
while cur != -1:
    while balls[comp] == balls[cur]:
        cur -= 1
    comp -= 1

# R B R BBB R B R B R B
# R B R BBB R B R B R R
