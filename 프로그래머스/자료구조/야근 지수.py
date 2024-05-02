import heapq


def solution(n, works):
    answer = 0

    hq = [-work for work in works]
    heapq.heapify(hq)

    for _ in range(n):
        temp = heapq.heappop(hq)
        if temp == 0:
            break
        heapq.heappush(hq, temp + 1)

    for work in hq:
        answer += work ** 2

    return answer