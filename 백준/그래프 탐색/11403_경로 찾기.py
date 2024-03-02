import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
G = [[INF] * N for _ in range(N)]
answer = [[0] * N for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        # 이동 비용이 1이라고 전제
        if temp[j] == 1:
            G[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for i in range(N):
    for j in range(N):
        if G[i][j] < INF:
            answer[i][j] = 1

for r in answer:
    print(*r)