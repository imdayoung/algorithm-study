def _round(n):
    check = n % 1
    if check < 0.5:
        return int(n)
    return int(n) + 1

T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    nums.sort()
    nums = nums[1:9]
    print(f"#{tc} {_round(sum(nums) / 8)}")