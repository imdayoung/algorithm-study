from collections import deque
import sys
input = sys.stdin.readline

# 테스트케이스의 수
t = int(input().rstrip())

for _ in range(t):
    count = 0
    # 문서의 개수 n, 몇 번째로 인쇄되었는 지 궁금한 문서가 현재 큐에서 m번재에 놓여 있음(맨 왼쪽은 0번째)
    n, m = map(int, input().rstrip().split())
    # n개 문서의 중요도(1이상 9이하, 중복 가능)
    queue = deque(list(map(int, input().rstrip().split())))
    
    while queue:
        priority = max(queue)
        front = queue.popleft()
        m -= 1

        # 맨 앞에 있던 것이 중요도가 가장 높은 문서였을 경우
        if front == priority:
            count += 1
            # 맨 앞에 있던 것이 타겟 문서인 경우
            if m < 0:
                print(count)
                break

        # 맨 앞에 있던 것이 중요도가 가장 높은 문서가 아니었을 경우
        else:
            queue.append(front)
            # 맨 앞에 있던 것이 타겟 문서인 경우
            if m < 0:
                m = len(queue) - 1