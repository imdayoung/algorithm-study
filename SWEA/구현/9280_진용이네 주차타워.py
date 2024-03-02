from collections import deque
import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    answer = 0
    n, m = map(int, input().split())
    parking_space = {i:0 for i in range(1, n + 1)}
    parking_car = {i:0 for i in range(1, m + 1)}
    price_per_weight = {i:int(input()) for i in range(1, n + 1)}
    car_weight = {i:int(input()) for i in range(1, m + 1)}

    queue = deque()
    for _ in range(m * 2):
        move = int(input())
        
        # 차가 주차장을 나감
        if move < 0:
            move *= -1
            # 대기 중인 차가 있으면 해당 주차 자리에 주차하고 가격 측정
            if queue:
                car = queue.popleft()
                parking_space[parking_car[move]] = car
                parking_car[car] = parking_car[move]
                parking_car[move] = 0
                answer += price_per_weight[parking_car[car]] * car_weight[car]
            # 대기 중인 차가 없으면 주차 자리가 비워짐
            else:
                parking_space[parking_car[move]] = 0
                parking_car[move] = 0
            
        # 차가 주차장에 들어옴
        else:
            for space, check in parking_space.items():
                # 주차장에 자리가 있는 경우 주차하고 가격 측정
                if check == 0:
                    parking_space[space] = move
                    parking_car[move] = space
                    answer += price_per_weight[space] * car_weight[move]
                    break
            # 주차장이 꽉 찬 경우 대기 목록에 삽입
            else:
                queue.append(move)
                

    print(f"#{tc} {answer}")