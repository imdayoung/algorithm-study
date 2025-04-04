from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    cmd_line = input()
    cmd = cmd_line.split()[0]
    if cmd == "push_front":
        queue.appendleft(int(cmd_line.split()[1]))
    elif cmd == "push_back":
        queue.append(int(cmd_line.split()[1]))
    elif cmd == "pop_front":
        num = queue.popleft() if queue else -1
        print(num)
    elif cmd == "pop_back":
        num = queue.pop() if queue else -1
        print(num)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        num = 0 if queue else 1
        print(num)
    elif cmd == "front":
        num = queue[0] if queue else -1
        print(num)
    elif cmd == "back":
        num = queue[-1] if queue else -1
        print(num)