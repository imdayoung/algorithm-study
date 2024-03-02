from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

# 산술평균
print(round(sum(nums) / n))

# 중앙값
print(nums[n // 2])

# 최빈값
counts = Counter(nums).most_common()
max_count = Counter(nums).most_common()[0][1]
max_nums = []
for num in counts:
  if num[1] == max_count:
    max_nums.append(num[0])
  else:
    break
if len(max_nums) == 1:
    print(max_nums[0])
else:
    max_nums.sort()
    print(max_nums[1])
# 범위
print(nums[-1] - nums[0])