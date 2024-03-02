# round 함수의 무서움

import sys

def my_round(num):
    check = num % 1
    if check < 0.5:
        return int(num)
    return int(num) + 1

input = sys.stdin.readline

n = int(input())
ratings = [int(input()) for _ in range(n)]

if n == 0:
    print(0)
else:
    ratings.sort()
    result = 0
    rm = my_round(n * 0.15)
    
    for i in range(rm, n - rm):
        result += ratings[i]

    print(my_round(result / (n - 2 * rm)))