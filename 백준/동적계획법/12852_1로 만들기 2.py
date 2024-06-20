N = int(input())

dp = [0] * (N + 1)
process = []

if N == 1:
    print(0)
    print(1)

else:
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        temp = 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
            if dp[i] == dp[i // 2] + 1:
                temp = 2

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
            if dp[i] == dp[i // 3] + 1:
                temp = 3
        
        process.append(temp)

    print(dp[N])
    k = N
    while k > 0:
        print(k, end = " ")
        if process[k - 2] == 1:
            k = k - process[k - 2]
        else:
            k = k // process[k - 2]