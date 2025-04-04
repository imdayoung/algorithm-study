from collections import deque
import sys
input = sys.stdin.readline

answer = 0
n, m = map(int, input().rstrip().split())
targets = list(map(int, input().rstrip().split()))
queue = deque(i for i in range(1, n + 1))

for target in targets:
    if queue.index(target) <= len(queue) // 2:
        while queue[0] != target:
            queue.append(queue.popleft())
            answer += 1
    else:
        while queue[0] != target:
            queue.appendleft(queue.pop())
            answer += 1
    queue.popleft()

print(answer)