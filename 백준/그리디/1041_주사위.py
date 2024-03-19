import sys


N = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
answer = 0

if N == 1:
    answer = sum(dice) - max(dice)
else:
    sum_list = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
    sum_list.sort()

    min1 = sum_list[0]
    min2 = sum_list[0] + sum_list[1]
    min3 = sum_list[0] + sum_list[1] + sum_list[2]

    side1 = 5 * N * N - 16 * N + 12
    side2 = 8 * N - 12
    side3 = 4
    
    answer += min1 * side1 + min2 * side2 + min3 * side3
    
print(answer)