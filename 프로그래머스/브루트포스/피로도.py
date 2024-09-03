answer = 0


def back_tracking(arr, n, d, k):
    global answer
    if len(arr) == n:
        cnt = 0
        for i in arr:
            if k >= d[i][0]:
                cnt += 1
                k -= d[i][1]
        answer = max(answer, cnt)
        return
    
    for i in range(n):
        if i not in arr:
            back_tracking(arr + [i], n, d, k)


def solution(k, dungeons):
    back_tracking([], len(dungeons), dungeons, k)
    return answer