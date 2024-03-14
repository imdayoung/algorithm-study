import sys


T = int(sys.stdin.readline())
for _ in range(T):
    answer = 0

    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort(reverse = True)
    B.sort(reverse = True)

    idx = 0
    for i in range(N):
        for j in range(idx, M):
            if A[i] > B[j]:
                break
            idx += 1
        answer += M - idx

    print(answer)