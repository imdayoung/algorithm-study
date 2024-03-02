from collections import deque
A, B = map(int, input().split())

queue = deque()
queue.append((1, A))
while queue:
    cnt, num = queue.popleft()
    if num == B:
        print(cnt)
        break

    if num * 2 <= B:
        queue.append((cnt + 1, num * 2))

    if num * 10 + 1 <= B:
        queue.append((cnt + 1, num * 10 + 1))

else:
    print(-1)