# 시간 초과
def backtracking(cur, length, target):
    global cnt
    global answer

    if cnt == int(target):
        answer = cur
        # return

    if len(cur) == length:
        cnt += 1
        return
    
    for i in ['1', '2', '4']:
        backtracking(cur + i, length, target)


def solution(n):
    idx = 1
    while answer == '':
        backtracking('', idx, str(n))
        idx += 1
    return answer


answer = ''
cnt = 1


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))