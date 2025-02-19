import sys


K = int(sys.stdin.readline())
C = int(sys.stdin.readline())

for _ in range(C):
    answer = 0
    
    M, N = map(int, sys.stdin.readline().split())
    
    diff = abs(M - N)
    remained = K - max(M, N)
    
    if M < N and diff - remained <= 1:
        answer = 1
    elif M > N and diff - remained <= 2:
        answer = 1
    elif M == N:
        answer = 1
        
    print(answer)
