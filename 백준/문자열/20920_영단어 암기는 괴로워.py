from collections import Counter
import sys
input = sys.stdin.readline

words = []
n, m = map(int, input().split())
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)

result = sorted(Counter(words).items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
for i in range(len(result)):
    print(result[i][0])