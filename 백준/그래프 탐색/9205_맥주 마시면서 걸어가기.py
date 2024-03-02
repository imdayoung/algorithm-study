from collections import deque
import sys


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if abs(x - x_festival) + abs(y - y_festival) <= 1000:
            return "happy"
        for i in range(n):
            if not visited[i]:
                x_conv, y_conv = conv[i]
                if abs(x - x_conv) + abs(y - y_conv) <= 1000:
                    queue.append((x_conv, y_conv))
                    visited[i] = 1
    return "sad"


t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    x_house, y_house = map(int, sys.stdin.readline().split())
    conv = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        conv.append((x, y))
    x_festival, y_festival = map(int, sys.stdin.readline().split())
    visited = [0 for _ in range(n + 1)]
    print(bfs(x_house, y_house))