from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    cmd = input().rstrip()
    if cmd == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        queue.append(cmd.split()[1])