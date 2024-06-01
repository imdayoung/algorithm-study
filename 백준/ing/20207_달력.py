import sys
sys.stdin = open("input.txt")


N = int(sys.stdin.readline())
plans = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plans.sort(key = lambda x : (x[0], x[1]))
print(plans)