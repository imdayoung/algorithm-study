import sys


input = sys.stdin.readline
ans = []
n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
temp = list(set(nums))
temp.sort()

dic = {}
for i in range(len(temp)):
    dic[temp[i]] = i

for num in nums:
    print(dic[num], end = " ")
