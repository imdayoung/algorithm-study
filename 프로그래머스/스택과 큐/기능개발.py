from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([0 for _ in range(len(progresses))])
    for i in range(len(progresses)):
        cnt = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            cnt += 1
        queue[i] = cnt
    
    while queue:
        start = queue.popleft()
        cnt = 1
        while True:
            if queue and queue[0] <= start:
                queue.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
    return answer