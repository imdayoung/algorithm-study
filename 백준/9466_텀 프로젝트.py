# 44M 1S
# 시간초과 ,,,,,,,,,,,,,,
import sys
from collections import deque


def travel(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        std = queue.popleft()
        # 탐색 진행 중 마지막 학생이 start 학생을 선택하면 마무리됨
        if students[std] == start:
            return visited[std] + 1
        
        # 탐색 진행 중 자기 자신을 선택한 학생이 있거나
        # 이미 탐색했던 학생을 다시 탐색하게 되면 망한 팀
        if std == students[std] or visited[students[std]] != -1:
            return -1
        
        # 위의 상황 외에는 계속 탐색을 진행해도 됨
        queue.append(students[std])
        visited[students[std]] = visited[std] + 1


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    students = [0] + list(map(int, sys.stdin.readline().split()))
    
    answer = 0
    

    for i in range(1, n + 1):
        # 자기 자신을 선택한 학생
        if i == students[i]:
            # answer -= 1
            continue

        else:
            visited = [-1 for _ in range(n + 1)]
            temp = travel(i)
            if temp == -1:
                answer += 1

    print(answer)