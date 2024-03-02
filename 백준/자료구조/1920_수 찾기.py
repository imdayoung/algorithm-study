import sys
input = sys.stdin.readline

def binary_search(nums, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

nums.sort()
for target in targets:
    print(binary_search(nums, target, 0, n - 1))