from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    queue = deque(list(map(int, input().split())))

    buy = 0
    cnt = 0
    res = 0
    highest = max(queue)

    while queue:
        if queue[0] < highest:
            buy += queue[0]
            cnt += 1
            queue.popleft()
        elif queue[0] == highest:
            res += cnt * highest - buy
            queue.popleft()
            if queue:
                highest = max(queue)
                buy = 0
                cnt = 0
        else:
            queue.popleft()

    print(f"#{tc} {res}")