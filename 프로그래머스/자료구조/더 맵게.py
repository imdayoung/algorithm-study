import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()

    while scoville:
        min_value = heapq.heappop(scoville)
        if min_value >= K:
            break
        if not scoville:
            return -1
        next_min_value = heapq.heappop(scoville)
        new_value = min_value + next_min_value * 2
        
        heapq.heappush(scoville, new_value)
        answer += 1
    
    return answer


print(solution([6, 2], 6))
# 2