N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N
stack = []
for i in range(len(A)):
    # 아직 오큰수를 찾지 못한 앞의 인덱스가 존재하고
    # 해당 인덱스의 값보다 이번에 넣는 값이 크면 해당 인덱스의 오큰수는 이번 값이 됨
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()
        answer[idx] = A[i]
    # 나의 오큰수를 찾기 위해 index를 스택에 넣음
    stack.append(i)

# 스택에 남아있는 인덱스는 오큰수가 없음
print(*answer)