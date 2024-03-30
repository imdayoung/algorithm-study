from collections import deque


def count_part(start, graph, visited):
    cnt = 1
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                cnt += 1

    return cnt


def solution(n, wires):
    answer = n

    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # 주어진 이어진 전선을 탐색하며 둘이 이어지지 않았다고 가정하여 start와 연결된 송전탑의 수 구하기
    for start, cut in wires:
        visited = [False for _ in range(n + 1)]
        visited[start] = True
        # a와 b가 이어지지 않음 -> b쪽에 이어진 송전탑은 탐색하지 않음
        visited[cut] = True
        cnt = count_part(start, graph, visited)
        answer = min(answer, abs(n - cnt - cnt))

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# 3
print(solution(4, [[1,2],[2,3],[3,4]]))
# 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
# 1