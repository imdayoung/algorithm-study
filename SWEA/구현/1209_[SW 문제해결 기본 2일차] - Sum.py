for _ in range(10):
    nums = []
    tc = int(input())
    for _ in range(100):
        temp = list(map(int, input().split()))
        nums.append(temp)
    
    result = 0
    # 각 행
    for i in range(100):
        temp = sum(nums[i])
        if temp > result:
            result = temp
    
    # 각 열
    for i in range(100):
        temp = sum(d[i] for d in nums)
        if temp > result:
            result = temp

    # 우상향 대각선
    temp = 0
    for i in range(100):
        temp += nums[i][i]
    if temp > result:
        result = temp

    # 우하향 대각선
    temp = 0
    for i in range(100):
        temp += nums[99 - i][i]
    if temp > result:
        result = temp

    print("#{} {}".format(tc, result))