import sys
input = sys.stdin.readline

# 지름길의 개수 N, 고속도로의 길이 D
N, D = map(int, input().split())
dp = [i for i in range(D + 1)]

shorts = []
for _ in range(N):
    start, end, length = map(int, input().split())
    # 지름길의 길이가 도착 위치와 시작 위치의 길이보다 작고
    # 지름길의 도착 위치가 고속도로의 길이보다 짧을 때에만 지름길 정보에 저장
    if length < end - start and end <= D:
        shorts.append((start, end, length))
shorts = sorted(shorts, key = lambda x:x[0])

for start, end, length in shorts:
    if start == 0 and dp[start] + length < dp[end]:
        dp[end] = dp[start] + length

for i in range(1, D + 1):
    dp[i] = min(dp[i - 1] + 1, dp[i])
    for start, end, length in shorts:
        if start == i and dp[start] + length < dp[end]:
            dp[end] = dp[start] + length

print(dp[D])