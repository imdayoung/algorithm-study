import sys


def get_answer(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 3

    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    return dp[n]


answers = []

try:
    while True:
        n = int(sys.stdin.readline())
        answers.append(get_answer(n))
except:
    for answer in answers:
        print(answer)
