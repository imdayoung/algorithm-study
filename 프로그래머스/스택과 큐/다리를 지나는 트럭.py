from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    sum_ongoing = 0
    ongoing_queue = deque([0] * bridge_length)
    waiting_queue = deque(truck_weights)
    
    while ongoing_queue:
        temp = ongoing_queue.popleft()
        sum_ongoing -= temp
        # 대기 트럭이 있는 경우
        if waiting_queue:
            # 대기 트럭에 있는 트럭이 다리 위에 올라갈 수 있는 경우
            if sum_ongoing + waiting_queue[0] <= weight and len(ongoing_queue) < bridge_length:
                temp = waiting_queue.popleft()
                sum_ongoing += temp
                ongoing_queue.append(temp)
                
            # 무게 초과 또는 다리 길이 이슈로 다리 위에 올라갈 수 없는 경우
            else:
                ongoing_queue.append(0)
        time += 1
        
    return time