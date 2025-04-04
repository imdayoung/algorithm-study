from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])
    
while len(queue) != 1:
    queue.append(queue.popleft())
    for _ in range(k - 1):
        if len(queue) > 1:
            queue.popleft()

print(queue[0])