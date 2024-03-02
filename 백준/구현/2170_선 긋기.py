import sys


answer = 0

N = int(sys.stdin.readline())
lines = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key = lambda x:(x[0], x[1]))

start, end = lines[0][0], lines[0][1]
if N == 1:
    answer = end - start
    
for i in range(1, N):
    new_start = lines[i][0]
    new_end = lines[i][1]

    # 기존 선과 독립된 경우
    if new_start > end:
        answer += (end - start)
        start = new_start
        end = new_end

    # 기존 선에 영향을 미치는 경우
    else:
        if new_end > end:
            end = new_end

    if i == N - 1:
        answer += (end - start)

print(answer)