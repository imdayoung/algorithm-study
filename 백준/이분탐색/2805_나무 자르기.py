import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    take = 0
    for tree in trees:
        if tree > mid:
            take += tree - mid
    
    if take > M:
        start = mid + 1
        
    elif take < M:
        end = mid - 1

    else:
        end = mid
        break

print(end)


