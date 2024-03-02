import sys
input = sys.stdin.readline

last = 0
answer = 0

N = int(input())
lectures = []

for _ in range(N):
    start, end = map(int, input().split())
    lectures.append((start, end))
lectures.sort(key = lambda x:(x[1], x[0]))

for lecture in lectures:
    if lecture[0] >= last:
        last = lecture[1]
        print(lecture)
        answer += 1

print(answer)