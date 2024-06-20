import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
friend = [[] for _ in range(n + 2)]
invite = set()

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

if len(friend[1]) == 0:
    print(0)
else:
    for i in friend[1]:
        invite.add(i)
        for j in friend[i]:
            invite.add(j)
    print(len(invite) - 1)