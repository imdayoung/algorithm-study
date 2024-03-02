from collections import deque


def solution(queue1, queue2):
    answer = 0
    
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    
    # queue의 합이 홀수이면 원소 합을 같게 만들 수 없음
    if (sum_q1 + sum_q2) % 2 == 1:
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    n = len(q1)
    
    for _ in range(n * 3):
        if sum_q1 < sum_q2:
            temp = q2.popleft()
            q1.append(temp)
            sum_q1 += temp
            sum_q2 -= temp
        elif sum_q1 > sum_q2:
            temp = q1.popleft()
            q2.append(temp)
            sum_q1 -= temp
            sum_q2 += temp
        else:
            return answer
        
        answer += 1
    
        if len(q1) == 0 or len(q2) == 0:
            return -1
    
    return -1