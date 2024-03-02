from collections import deque


def solution(people, limit):
    people.sort()
    queue = deque(people)
    answer = 0
    
    while queue:
        out = queue.pop()
        answer += 1
        if not queue:
            break
        if queue[0] + out <= limit:
            queue.popleft()
        
    return answer