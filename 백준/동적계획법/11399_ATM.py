n = int(input())
times = list(map(int, input().split()))

times.sort()
d = [times[0]] + [0 for _ in range(n - 1)]
for i in range(1, n):
    d[i] = d[i - 1] + times[i]

print(sum(d))