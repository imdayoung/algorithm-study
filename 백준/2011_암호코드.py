# 30M
import sys


code = sys.stdin.readline().rstrip()
n = len(code)

# 암호가 0으로 시작되면 잘못된 암호
if code[0] == '0':
    print(0)
    exit()

# i번째 알파벳까지 문자열로 만들 수 있는 해석의 개수
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    if 1 <= int(code[i]) <= 9:
        dp[i] = dp[i - 1]
    


print(dp[n - 1])