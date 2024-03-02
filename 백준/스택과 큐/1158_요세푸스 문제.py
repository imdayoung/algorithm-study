import sys
from collections import deque

input = sys.stdin.readline().rstrip
n, k = map(int, input().split())

queue = deque()
for i in range(1, n + 1):
    queue.append(i)
result = []
i = 1

while queue:
    if i % k != 0:    # k번째가 아님
        num = queue.popleft()
        queue.append(num)
    else:
        out = queue.popleft()
        result.append(out)
    i += 1

print("<", end = '')
# for i in range(len(result) - 1):
#     print(result[i], end = ', ')
# print(result[-1], end = '')
print(*result, sep=', ', end = '')
print(">")