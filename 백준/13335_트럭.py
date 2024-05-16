import sys
from collections import deque


time = 0

n, w, L = map(int, sys.stdin.readline().split())
trucks = deque(list(map(int, sys.stdin.readline().split())))

on_bridge = deque([0 for _ in range(w)])
on_bridge_weight = 0

while trucks or on_bridge_weight != 0:
    on_bridge_weight -= on_bridge.popleft()

    if trucks:
        if on_bridge_weight + trucks[0] <= L:
            temp = trucks.popleft()
            on_bridge.append(temp)
            on_bridge_weight += temp
        else:
            on_bridge.append(0)

    time += 1

print(time)