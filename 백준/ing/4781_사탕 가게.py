import sys


while True:
    n, m = map(float, sys.stdin.readline().split())
    if n == 0.0 and m == 0.00:
        break

    dp = [[ for _ in range()] for _ in range()]

    candies = []
    for _ in range(int(n)):
        c, p = map(float, sys.stdin.readline().split())
        candies.append([int(c), p])
    print(candies)

    for candy in candies:
        