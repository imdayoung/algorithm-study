from collections import defaultdict

T = int(input())
for tc in range(1, T + 1):
    stops = defaultdict(int)

    N = int(input())
    buses = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    passing = [int(input()) for _ in range(P)]

    print(buses)

    for start, end in buses:
        for i in range(start, end + 1):
            stops[i] += 1

    print(f"#{tc}", end = " ")
    for j in passing:
        print(stops[j], end = " ")
    print()