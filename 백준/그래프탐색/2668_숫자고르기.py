import sys
input = sys.stdin.readline

def dfs(target, x):
    global answer
    visited[x] = True
    
    if not visited[nums[x]]:
        dfs(target, nums[x])

    elif visited[nums[x]] and nums[x] == target:
        answer.append(target)


answer = []
N = int(input())
nums = [0] + [int(input()) for _ in range(N)]

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)

print(len(answer))
for a in answer:
    print(a)





# # 백트래킹 -> 시간초과
# import sys
# input = sys.stdin.readline


# def back_tracking(idx, arr):
#     global cnt
#     global answers
#     x = [a[0] for a in arr]
#     y = [a[1] for a in arr]
#     y.sort()

#     if idx == N:
#         return
    
#     arr.append(table[idx])
    
#     if x == y and len(x) > cnt:
#         cnt = len(x)
#         answers = x

#     back_tracking(idx + 1, arr)
#     arr.pop()
#     back_tracking(idx + 1, arr)
    

# N = int(input())
# table = [(i, int(input())) for i in range(1, N + 1)]

# cnt = 0
# answers = []
# back_tracking(0, [])
# print(cnt)
# for answer in answers:
#     print(answer)