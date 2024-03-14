from collections import deque
import sys


T = int(sys.stdin.readline())
for _ in range(T):
    answer = 0

    N = int(sys.stdin.readline())
    sorted_tree = [0] * N

    tree = list(map(int, sys.stdin.readline().split()))
    tree.sort()
    tree = deque(tree)

    for idx in range(N // 2):
        first = tree.popleft()
        sorted_tree[idx] = first
        second = tree.popleft()
        sorted_tree[N - 1 - idx] = second

    if tree:
        sorted_tree[N // 2] = tree.popleft()

    for i in range(N - 1):
        answer = max(answer, abs(sorted_tree[i + 1] - sorted_tree[i]))
    
    print(answer)