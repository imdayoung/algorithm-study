import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
words = sorted(list(set(words)))
words.sort(key = len)

for word in words:
    print(word)