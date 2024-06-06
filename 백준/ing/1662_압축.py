"""
33(562(71(9)))
123
10342(76)
0(0)
1(1(1(1(1(1(1(0(1234567890))))))))
1()66(5)
92(34)66(52(3))

19
3
8
0
0
7
24
"""
import sys
sys.stdin = open("input.txt")


answer = 0
S = sys.stdin.readline().rstrip()
print(f"S: {S}")

stack = []
for i in range(len(S)):
    if S[i] == "(":
        
    elif S[i] == ")":
        
        
print(answer)

"""
import sys
from collections import deque
sys.stdin = open("input.txt")


def get_bracket_index(string):
    stack = []
    brackets = deque()

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            brackets.append((stack.pop(), i))

    return brackets


answer = 0
S = sys.stdin.readline().rstrip()
print(f"S: {S}")

brackets = get_bracket_index(S)
print(brackets)

temp = 0

if not brackets:
    answer = len(S)

else:
    start_prev, end_prev = brackets[0][0], brackets[0][1]
    print(start_prev, end_prev)

    while brackets:
        start_cur, end_cur = brackets.popleft()
        
        if start_cur == start_prev:
            temp = end_cur - start_cur - 1

        # 포함 관계
        elif start_cur < end_prev:
            temp = int(S[start_cur - 1]) * temp
            # answer = int(S[start_cur - 1])

        # 독립 관계
        else:
            answer += temp
            temp = int(S[start_cur - 1]) * (end_cur - start_cur - 1) + (start_cur - end_prev - 1)
            # answer += int(S[start_cur - 1]) * (end_cur - start_cur - 1) + (start_cur - end_prev - 1)

        start_prev, end_prev = start_cur, end_cur

    answer += temp

print(answer)
"""

"""
# 메모리 초과
import sys
from collections import deque


for _ in range(7):
    S = list(map(str, sys.stdin.readline().rstrip()))

    stack = []
    brackets = deque()

    for i in range(len(S)):
        if S[i] == "(":
            stack.append(i)
        elif S[i] == ")":
            brackets.append((stack.pop(), i))
            
    while brackets:
        temp = ""
        start, end = brackets.popleft()
        for _ in range(int(S[start - 1])):
            temp += ''.join(i for i in S[start + 1:end])
        for i in range(start - 1, end + 1):
            S[i] = ""
        S[start + 1] = temp
    print(len(''.join(i for i in S)))
"""