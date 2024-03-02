from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(i for i in priorities)
    queue = deque(list(enumerate(priorities)))
    print(queue)
    
    while queue:
        idx, val = queue.popleft()
        priorities.popleft()
        
        if len(priorities) == 0 or val >= max(priorities):
            answer += 1
            if idx == location:
                break
        else:
            queue.append((idx, val))
            priorities.append(val)
                
    return answer