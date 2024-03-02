import sys


N, M = map(int, sys.stdin.readline().split())
A = list(int(sys.stdin.readline().rstrip()) for _ in range(N))
A.sort()

answer = A[-1] - A[0]

start, end = 0, 0
while end != N:
    diff = A[end] - A[start]
    if diff < M:
        end += 1
        
    elif diff > M:
        start += 1
        answer = min(answer, diff)
        
    else:
        answer = M
        break
    
print(answer)


# # 메모리 초과
# from itertools import combinations
# import sys


# N, M = map(int, sys.stdin.readline().split())
# A = list(int(sys.stdin.readline().rstrip()) for _ in range(N))
# A.sort()
# answer = A[-1] - A[0]
# for x, y in list(combinations(A, 2)):
#     if abs(x - y) >= M:
#         answer = min(answer, abs(x -y))

# print(answer)