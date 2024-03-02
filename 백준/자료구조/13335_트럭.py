from collections import deque


time = 0
n, w, L = map(int, input().split())
truck = deque(list(map(int, input().split())))
bridge = deque([0 for _ in range(w)])

while truck:
    bridge.popleft()
    time += 1

    # 다음 트럭이 바로 다리 위로 올라가도 되는 경우
    if sum(bridge) + truck[0] <= L:
        bridge.append(truck.popleft())
    # 다음 트럭이 대기해야 하는 경우
    else:
        bridge.append(0)

    # 모든 트럭이 다리 위에 올라와 있는 상태
    if not truck:
        time += w

print(time)