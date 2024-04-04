import sys


code = sys.stdin.readline().rstrip()
n = len(code)

# 암호가 0으로 시작되면 잘못된 암호
if code[0] == '0':
    print(0)
    exit()

# i번째 알파벳까지 문자열로 만들 수 있는 해석의 개수
dp = [1 for _ in range(n)]

for i in range(1, n):
    if code[i] == '0':
        if code[i - 1] == '1' or code[i - 1] == '2':
            dp[i] = dp[i - 2]
        else:
            print(0)
            exit()
    elif 11 <= int(code[i - 1] + code[i]) <= 26:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
    else:
        dp[i] = dp[i - 1]

print(dp[n - 1])