# 13M 23S
import sys


# 백트래킹? 그리디? DP?



N = int(sys.stdin.readline())
matrix_sizes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(matrix_sizes)

cal_cnt = []
for i in range(N - 1):
    cal_cnt.append(matrix_sizes[i][0] * matrix_sizes[i][1] * matrix_sizes[i + 1][1])
print(cal_cnt)

