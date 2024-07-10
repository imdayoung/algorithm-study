import sys


answers = []

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    temp = sorted(a[i - 1:j])
    answers.append(temp[k - 1])

for answer in answers:
    print(answer)
