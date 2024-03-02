from collections import deque
import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
initial_cards = [0] * N
initial_index = deque([i for i in range(N)])

target_number = N
for skill in A:
    if skill == 1:
        card_index = initial_index[0]
        initial_index.popleft()
    elif skill == 2:
        card_index = initial_index[1]
        initial_index.remove(card_index)
    else:
        card_index = initial_index[-1]
        initial_index.pop()

    initial_cards[card_index] = target_number
    target_number -= 1

print(*initial_cards)