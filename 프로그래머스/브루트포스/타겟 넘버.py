answer = 0


def back_tracking(cnt, n, numbers, target):
    global answer

    if cnt == len(numbers):
        if n == target:
            answer += 1
        return
    
    back_tracking(cnt + 1, n + numbers[cnt], numbers, target)
    back_tracking(cnt + 1, n - numbers[cnt], numbers, target)

        
def solution(numbers, target):
    back_tracking(0, 0, numbers, target)
    return answer