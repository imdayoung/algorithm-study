from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting_trucks = deque(truck_weights)
    on_bridge = deque([0] * bridge_length)
    on_bridge_weight = 0

    # 대기중인 트럭이 있거나 다리를 건너고 있는 트럭이 있는 경우 반복
    while waiting_trucks or on_bridge_weight > 0:
        answer += 1
        on_bridge_weight -= on_bridge.popleft()

        if waiting_trucks and on_bridge_weight + waiting_trucks[0] <= weight:
            next_truck = waiting_trucks.popleft()
            on_bridge.append(next_truck)
            on_bridge_weight += next_truck
        else:
            on_bridge.append(0)

    return answer


print(solution(2, 10, [7,4,5,6]))
# 8

print(solution(100, 100, [10]))
# 101

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
# 110