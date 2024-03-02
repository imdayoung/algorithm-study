import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A_reversed = A[::-1]

increasing = [1] * N
decreasing = [1] * N

for i in range(N):
    for j in range(i):
        # 가장 긴 증가하는 부분 수열
        if A[i] > A[j]:
            increasing[i] = max(increasing[i], increasing[j] + 1)
        # 가장 긴 감소하는 부분 수열
        if A_reversed[i] > A_reversed[j]:
            decreasing[i] = max(decreasing[i], decreasing[j] + 1)

result = 0
for i in range(N):
    result = max(result, increasing[i] + decreasing[N - i - 1] - 1)

print(result)