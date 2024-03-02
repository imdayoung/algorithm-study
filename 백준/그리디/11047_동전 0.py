import sys
input = sys.stdin.readline

count = 0
N, K = map(int, input().split())
prices = []
for _ in range(N):
    price = int(input())
    if price <= K:
        prices.append(price)
prices.sort(reverse = True)

for price in prices:
    count += K // price
    K %= price

    if K == 0:
        break

print(count)