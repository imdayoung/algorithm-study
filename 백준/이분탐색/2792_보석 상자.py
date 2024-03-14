import sys


N, M = map(int, sys.stdin.readline().split())
jewels = [int(sys.stdin.readline()) for _ in range(M)]

answer = max(jewels)

start = 1
end = max(jewels)

while start <= end:
    child_need = 0
    mid = (start + end) // 2

    for jewel in jewels:
        child_need += jewel // mid
        if jewel % mid != 0:
            child_need += 1
    
    if child_need <= N:
        answer = min(answer, mid)
        end = mid - 1
    else:
        start = mid + 1

print(answer)