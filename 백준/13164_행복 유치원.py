import sys


N, K = map(int, sys.stdin.readline().split())
children = list(map(int, sys.stdin.readline().split()))
diff = [children[i + 1] - children[i] for i in range(N - 1)]
print(children)
print(diff)

