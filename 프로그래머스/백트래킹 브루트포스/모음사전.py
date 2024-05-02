def backtracking(word, target):
    global cnt
    global answer
    cnt += 1

    if word == target:
        answer = cnt
        return
    
    if len(word) == 5:
        return

    for char in ['A', 'E', 'I', 'O', 'U']:
        backtracking(word + char, target)


def solution(word):
    backtracking('', word)
    return answer

cnt = -1
answer = 0