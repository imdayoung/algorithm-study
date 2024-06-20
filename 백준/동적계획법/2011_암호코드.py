code = input()
codes = [c for c in code]
n = len(codes)

if codes[0] == '0':
    print(0)
    exit()

dp = [1] * (n + 1)
for i in range(2, n + 1):
    if codes[i - 1] == '0':
        if codes[i - 2] == '0' or (codes[i - 2] != '1' and codes[i - 2] != '2'):
            print(0)
            exit()
        else:
            dp[i] = dp[i - 2]
    elif 10 <= int(codes[i - 2] + codes[i - 1]) <= 26:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
    else:
        dp[i] = dp[i - 1]

print(dp[n])

"""
테스트용
def solution(code):
    codes = [c for c in code]
    n = len(codes)

    if codes[0] == '0':
        print(0)
        exit()

    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        if codes[i - 1] == '0':
            if codes[i - 2] == '0' or (codes[i - 2] != '1' and codes[i - 2] != '2'):
                print(0)
                exit()
            else:
                dp[i] = dp[i - 2]
        elif 10 <= int(codes[i - 2] + codes[i - 1]) <= 26:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
        else:
            dp[i] = dp[i - 1]

    print(dp[n])

solution("20236") #2
solution("2727") #1
solution("210") #1
solution("230") #0
solution("2") #1
solution("0") #0
solution("012") #0
solution("19126") #6
solution("111111111111111111111111111111") #346269
"""