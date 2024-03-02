import heapq
import sys


N = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(N)]
card.sort()

answer = 0
while len(card) > 1:
    v1 = heapq.heappop(card)
    v2 = heapq.heappop(card)
    temp = v1 + v2
    answer += temp
    heapq.heappush(card, temp)
print(answer)


# # 시간 초과
# # 아 작은 것끼리 합쳐서 가장 작은 수의 합을 먼저 만드는 걸 목표로 해야하나 보다
# from collections import deque
# import sys


# N = int(sys.stdin.readline())
# card = [int(sys.stdin.readline()) for _ in range(N)]
# card.sort()
# card = deque(card)

# answer = 0
# while len(card) > 1:
#     v1 = card.popleft()
#     v2 = card.popleft()
#     temp = v1 + v2
#     answer += temp
#     card.appendleft(temp)
# print(answer)