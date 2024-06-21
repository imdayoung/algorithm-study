from itertools import combinations
import sys
sys.stdin = open("input.txt")
    

for _ in range(2):
    answers = []
    possible = set()
    
    n = int(sys.stdin.readline())
    weights = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    check_weights = list(map(int, sys.stdin.readline().split()))

    for i in range(1, n + 1):
        for comb in list(combinations(weights, i)):
            print(comb)
            
    
            


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