import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().rstrip().split()
    if n > 32:
        print(0)
    else:
        ans = 99999
        for i in range(n - 2):
            for j in range(n - 1):
                for k in range(n):
                    diff = 0
                    if i == j or j == k or k == i:
                        continue
                    for x in range(4):
                        if mbti[i][x] != mbti[j][x]:
                            diff += 1
                        if mbti[j][x] != mbti[k][x]:
                            diff += 1
                        if mbti[k][x] != mbti[i][x]:
                            diff += 1
                    ans = min(ans, diff)
        print(ans)