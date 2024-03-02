from collections import deque


def rotate(graph, x_start, y_start, x_end, y_end):
    queue = deque()

    for y in range(y_start, y_end):
        queue.append(graph[x_start][y])
    for x in range(x_start, x_end):
        queue.append(graph[x][y_end])
    for y in range(y_end, y_start, -1):
        queue.append(graph[x_end][y])
    for x in range(x_end, x_start, -1):
        queue.append(graph[x][y_start])
    queue.appendleft(queue.pop())
    min_value = min(queue)

    for y in range(y_start, y_end):
        graph[x_start][y] = queue.popleft()
    for x in range(x_start, x_end):
        graph[x][y_end] = queue.popleft()
    for y in range(y_end, y_start, -1):
        graph[x_end][y] = queue.popleft()
    for x in range(x_end, x_start, -1):
        graph[x][y_start] = queue.popleft()

    return graph, min_value


def solution(rows, columns, queries):
    answer = []

    # 그래프 생성 및 초기화
    graph = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = num
            num += 1

    # 회전 진행
    for x1, y1, x2, y2 in queries:
        graph, min_value = rotate(graph, x1 - 1, y1 - 1, x2 - 1, y2 - 1)
        answer.append(min_value)

    return answer