# 메모리 초과
import sys
from itertools import combinations
    

def get_possible_weights(arr, n):
    sum_arr = sum(arr)
    dp = [False for _ in range(sum_arr + 1)]
    # 합으로 구할 수 잇는 거 구하고 for문으로 돌면서 뺀 값도 true로 만들어주면 되지 않을까
    for i in range(1, n + 1):
        for comb in list(combinations(arr, i)):
            dp[sum(comb)] = True

    for i in range(sum_arr, 0, -1):
        for j in range(i - 1, -1, -1):
            if dp[i] and dp[j]:
                dp[i - j] = True
                
    return dp


answers = []

n = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check_weights = list(map(int, sys.stdin.readline().split()))

dp = get_possible_weights(weights, n)

for check in check_weights:
    if dp[check]:
        answers.append("Y")
    else:
        answers.append("N")
        
print(*answers)
    

"""
# 시간 초과
import sys


def backtracking(total, start):
    if start > n:
        return
    
    if start == n:
        if total > 0:
            possible.add(total)
    else:
        backtracking(total, start + 1)
        backtracking(total - weights[start], start + 1)
        backtracking(total + weights[start], start + 1)
        

answers = []
possible = set()

n = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check_weights = list(map(int, sys.stdin.readline().split()))

backtracking(0, 0)

for check_weight in check_weights:
    if check_weight in possible:
        answers.append("Y")
    else:
        answers.append("N")
        
print(*answers)
"""