import sys
sys.stdin = open("input.txt")


for _ in range(4):
    # C명을 늘리기 위해 투자해야하는 최솟값
    C, N = map(int, sys.stdin.readline().split())
    cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cities.sort(key = lambda x:(x[0] / x[1]))
    print(cities)
        
# 8
# 4
# 10
# 45
