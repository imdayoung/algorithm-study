import sys


answer = 0

N = int(sys.stdin.readline())
sums = []
for _ in range(N):
    result = 0
    card = list(map(int, sys.stdin.readline().split()))
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                card_sum = card[i] + card[j] + card[k]
                card_sum_str = str(card_sum)
                result = max(result, int(card_sum_str[-1]))
    sums.append(result)

max_sums = max(sums)
for i in range(N - 1, -1, -1):
    if sums[i] == max_sums:
        answer = i + 1
        break

print(answer)
