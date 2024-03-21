from collections import deque


def solution(n, wires):
    answer = -1
    tree = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = wires[i][0], wires[i][1]
        tree[a].append(b)
        tree[b].append(a)

    parent = [i for i in range(n + 1)]
    print(tree)
    return answer



print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# 3
print(solution(4, [[1,2],[2,3],[3,4]]))
# 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
# 1