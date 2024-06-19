# dp라고 ,,,?
import sys


def get_palindrome():
    dp = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    # for i in range(1, N + 1):
    #     dp[i][i] = True
    # for d in dp:
    #     print(d)


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
questions = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

get_palindrome()

"""
# 무지성 구현 -> 시간 초과



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
