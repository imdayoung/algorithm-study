import sys
input = sys.stdin.readline

def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if A[i][j] == 1:
                A[i][j] = 0
            else:
                A[i][j] = 1

N, M = map(int, input().split())
A, B = [], []
for _ in range(N):
    A.append(list(map(int, input().rstrip())))
for _ in range(N):
    B.append(list(map(int, input().rstrip())))
count = 0

# # 3X3 행렬보다 작은 경우
# if N < 3 or M < 3:
#     if A == B:
#         print(0)
#     else:
#         print(-1)

# 3X3 행렬보다 큰 경우
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            count += 1

if A == B:
    print(count)
else:
    print(-1)