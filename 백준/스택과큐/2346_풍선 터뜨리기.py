from collections import deque

answer = []
n = int(input())
balloons = deque(enumerate(map(int, input().split())))

while balloons:
    idx, paper = balloons.popleft()
    answer.append(idx + 1)

    if paper > 0:
        balloons.rotate(-(paper - 1))
    else:
        balloons.rotate(-paper)

print(*answer, sep = " ") 