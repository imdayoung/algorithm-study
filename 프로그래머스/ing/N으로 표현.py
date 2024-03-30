def solution(N, number):
    dp = []
    max_use = 8

    # i개의 N으로 표현 가능한 수
    for i in range(1, max_use + 1):
        nums = set([int(str(N) * i)])
        for j in range(i // 2):
            for x in dp[j]:
                for y in dp[i - j - 2]:
                    nums.add(x - y)
                    nums.add(x + y)
                    nums.add(x * y)
                    if y != 0:
                        nums.add(x // y)
                    if x != 0:
                        nums.add(y // x)
        
        if number in nums:
            return i
        
        dp.append(nums)

    return -1


print(solution(5, 12))
# 4
print(solution(2, 11))
# 3