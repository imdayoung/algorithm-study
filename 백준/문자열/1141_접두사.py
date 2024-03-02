import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())

words = sorted(words, key = len)
answer = words.copy()

for i in range(len(words) - 1):
    for j in range(i + 1, len(words)):
        if words[i] == words[j][:len(words[i])]:
            answer.remove(words[i])
            break

print(len(answer))