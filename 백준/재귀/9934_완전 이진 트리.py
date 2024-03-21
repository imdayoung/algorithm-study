def divide(level, arr, n):
    if level == K:
        return
    
    divide(level + 1, arr[:n // 2], n // 2)
    levels[level].append(arr[n // 2])
    divide(level + 1, arr[n // 2 + 1:], n // 2)


K = int(input())
buildings = list(map(int, input().split()))

levels = [[] for _ in range(K)]
divide(0, buildings, 2 ** K - 1)

for l in levels:
    print(*l)