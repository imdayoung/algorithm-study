import sys
input = sys.stdin.readline

# 듣도 못한 사람의 수 n, 보도 못한 사람의 수 m
n, m = map(int, input().rstrip().split())

not_seen = set([input().rstrip() for _ in range(n)])
not_listened = set([input().rstrip() for _ in range(m)])

result = list(not_seen & not_listened)
result.sort()
print(len(result))
for r in result:
    print(r)