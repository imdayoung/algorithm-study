# 시간 초과 ,,
import sys


def calculate(nums, idx, expression):
    if idx == len(nums):
        result = eval(expression)
        possible.add(abs(result))
        return result
    
    if idx == 0:
        calculate(nums, idx + 1, expression + str(nums[idx]))
    else:
        calculate(nums, idx + 1, expression + "+" + str(nums[idx]))
        calculate(nums, idx + 1, expression + "-" + str(nums[idx]))
        

def backtracking(arr, start):
    if len(arr) != 0:
        calculate(arr, 0, "")
    
    if len(arr) == weights:
        return
    
    for i in range(start, k):
        backtracking(arr + [weights[i]], i + 1)


possible = set()

k = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))

backtracking([], 0)
print(sum(weights) - len(possible))