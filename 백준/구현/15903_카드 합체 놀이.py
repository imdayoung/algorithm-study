import sys


n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

for _ in range(m):
    temp = cards[0] + cards[1]
    cards[0], cards[1] = temp, temp
    cards.sort()

print(sum(cards))