import sys


def binary_search(num):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if num > limits[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return start


answer = []
names = []
limits = []

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    name, limit = sys.stdin.readline().split()
    names.append(name)
    limits.append(int(limit))

for _ in range(M):
    answer.append(names[binary_search(int(sys.stdin.readline()))])

print(*answer, sep = "\n")