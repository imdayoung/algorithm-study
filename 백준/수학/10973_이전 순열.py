import sys


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

if nums == [i for i in range(1, N + 1)]:
    print(-1)

else:
    for i in range(N - 1, 0, -1):
        if nums[i] < nums[i - 1]:
            for j in range(N - 1, 0, -1):
                if nums[j] < nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    temp = sorted(nums[i:], reverse=True)
                    nums = nums[:i] + temp
                    print(*nums)
                    exit()
