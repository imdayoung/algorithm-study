import sys
sys.stdin = open("input.txt")


N = int(sys.stdin.readline())
nums = list(map(str, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
questions = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[False for _ in range(N)] for _ in range(N)]


"""
# 정답 ..
import sys


N = int(input())
num_arr = [int(x) for x in input().split()]
M = int(input())

DP = [[0] * (N) for _ in range(N)] # DP[i][j] i부터 j까지

for i in range(N): # len == 1
    DP[i][i] = 1

for i in range(N - 1): # len == 2
    if num_arr[i] == num_arr[i + 1]:
        DP[i][i + 1] = 1

for num_len in range(2, N): # len >= 3
    for start in range(N - num_len):
        end = start + num_len
        if num_arr[start] == num_arr[end]:
            if DP[start + 1][end - 1] == 1:
                DP[start][end] = 1

for row in DP:
    print(row)

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(DP[S - 1][E - 1])
"""

"""
# 무지성 구현 -> 시간 초과
import sys


answers = []
palindrome_dict = {}

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
questions = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for S, E in questions:
    num = ''.join(str(n) for n in nums[S - 1:E])
    
    if num not in palindrome_dict:
        if num == num[::-1]:
            palindrome_dict[num] = 1
        else:
            palindrome_dict[num] = 0
    
    answers.append(palindrome_dict[num])
        
for answer in answers:
    print(answer)
"""

"""
# 무지성 구현2 -> 시간 초과
import sys


def is_palindrome(num):
    num_len = len(num)
    for i in range(num_len // 2):
        if num[i] != num[num_len - i - 1]:
            return False        
    return True


answers = []
palindrome_dict = {}

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
questions = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for S, E in questions:
    num = ''.join(str(n) for n in nums[S - 1:E])
    
    if num not in palindrome_dict:
        if is_palindrome(num):
            palindrome_dict[num] = 1
        else:
            palindrome_dict[num] = 0
    
    answers.append(palindrome_dict[num])
        
for answer in answers:
    print(answer)
"""
