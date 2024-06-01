import sys
sys.stdin = open("input.txt")
# 엥 걍 틀려먹었네

for tc in range(6):
    S = list(map(str, sys.stdin.readline().rstrip()))
    brackets_start = []

    start_prev, end = 0, 0
    for i in range(len(S)):
        if S[i] == "(":
            brackets_start.append(i)
        elif S[i] == ")":
            end = i
            break
        
    cur_length = 0
    print(f"====== {tc} ======")
    if not brackets_start:
        cur_length = len(S)
    else:
        
        start_prev = brackets_start.pop()
        cur_length = (end - start_prev - 1) * int(S[start_prev - 1])
        
        while brackets_start:
            # print("중간결과:", cur_length)
            start_cur = brackets_start.pop()
            cur_length = cur_length * int(S[start_cur - 1]) + (start_prev - start_cur - 1)
            start_prev = start_cur
            
        cur_length += start_prev - 1
    print(f"정답~ {cur_length}")
    

# # 메모리 초과
# import sys
# from collections import deque


# new_S = []
# S = list(map(str, sys.stdin.readline().rstrip()))

# stack = []
# brackets = deque()

# for i in range(len(S)):
#     if S[i] == "(":
#         stack.append(i)
#     elif S[i] == ")":
#         brackets.append((stack.pop(), i))
        
# while brackets:
#     temp = ""
#     start, end = brackets.popleft()
#     # print(S[start + 1:end])
#     for _ in range(int(S[start - 1])):
#         temp += ''.join(i for i in S[start + 1:end])
#     for i in range(start - 1, end + 1):
#         S[i] = ""
#     S[start + 1] = temp
# print(len(''.join(i for i in S)))