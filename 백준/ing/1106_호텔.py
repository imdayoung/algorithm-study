import sys


C, N = map(int, sys.stdin.readline().split())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    cost = cities[i][0]
    amount = cities[i][1]
    
    