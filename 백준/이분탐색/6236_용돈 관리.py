import sys


N, M = map(int, sys.stdin.readline().split())
cost = [int(sys.stdin.readline()) for _ in range(N)]
answer = sum(cost)

start, end = min(cost), sum(cost)
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    in_cash = 0
    for today in cost:
        # K원을 인출해도 사용할 수 없는 경우(답이 될 수 없는 경우)
        if mid < today:
            start = mid + 1
            break
        # 통장에 집어넣고 다시 K원을 인출해야 하는 경우
        if in_cash < today:
            in_cash = mid
            cnt += 1
        in_cash -= today

    else:
        if cnt <= M:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
        
print(answer)