from collections import deque
                        

def is_certain(n, node, winners, losers):
    cnt = 1

    visited = [False for _ in range(n + 1)]
    visited[node] = True

    # 나를 이긴 사람들을 이긴 사람은 나를 이김
    queue = deque([node])
    while queue:
        x = queue.popleft()
        # node를 이긴 사람들에 대해
        for i in winners[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1

    # 나한테 진 사람들한테 진 사람은 나한테 짐
    queue = deque([node])
    while queue:
        x = queue.popleft()
        for i in losers[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1

    if cnt == n:
        return True
    return False


def solution(n, results):
    answer = 0

    winners = [[] for _ in range(n + 1)]    # 나를 이긴 사람들
    losers = [[] for _ in range(n + 1)]     # 나한테 진 사람들

    for w, l in results:
        winners[l].append(w)
        losers[w].append(l)
    
    for i in range(1, n + 1):
        if is_certain(n, i, winners, losers):
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# 2