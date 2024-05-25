import sys


# C명을 늘리기 위해 투자해야하는 최솟값
C, N = map(int, sys.stdin.readline().split())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(cities)
