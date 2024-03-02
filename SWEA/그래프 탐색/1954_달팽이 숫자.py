import sys
sys.stdin = open("input.txt", "r")

def draw():
    num = 1
    direction = 1
    x, y = 0, -1

    for _ in range(N):
        y += 1
        graph[x][y] = num
        num += 1

    for i in range(N - 1, 0, -1):
        # 아래 또는 위
        for _ in range(i):
            if direction == 1:
                x += 1
            else:
                x -= 1
            graph[x][y] = num
            num += 1

        # 왼쪽 또는 오른쪽
        for _ in range(i):
            if direction == 1:
                y -= 1
            else:
                y += 1
            graph[x][y] = num
            num += 1

        direction *= -1
        
T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc}")
    N = int(input())

    graph = [[0] * N for _ in range(N)]
    
    draw()
    for g in graph:
        print(*g)