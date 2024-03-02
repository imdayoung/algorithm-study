from collections import deque

N = int(input())

queue = deque([1])
count = [0] * (10 ** 6 + 1)
while queue:
    x = queue.popleft()
    if x == N:
        print(count[x])
        break
    for nx in [x * 3, x * 2, x + 1]:
        if nx <= 10 ** 6:
            queue.append(nx)
            count[nx] = count[x] + 1