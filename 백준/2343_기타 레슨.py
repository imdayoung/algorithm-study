import sys


N, M = map(int, sys.stdin.readline().split())
lessons = list(map(int, sys.stdin.readline().split()))

# 구하려는 것: 블루레이의 크기의 최소
start = max(lessons)
end = sum(lessons)
answer = end

while start <= end:    
    mid = (start + end) // 2
    # 블루레이의 크기를 mid로 설정했을 때 필요한 블루레이의 개수
    cnt = 1
    # 현재 블루레이에 담긴 영상의 길이
    cur_length = 0

    for i in range(N):
        # 다음 블루레이로 넘어가야 함
        if cur_length + lessons[i] > mid:
            cnt += 1
            cur_length = lessons[i]
        else:
            cur_length += lessons[i]

    if cnt > M:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)